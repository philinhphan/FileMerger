from flask import Flask, request, send_file, jsonify, session
from werkzeug.utils import secure_filename
import json
import os
import tempfile
import mimetypes
import traceback
import uuid
import yaml
from yaml.loader import SafeLoader

app = Flask(__name__)
app.secret_key = os.urandom(24)  # For session handling

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
ALLOWED_EXTENSIONS = {'.txt', '.java', '.xml', '.kt', '.py', '.js', '.html', '.css', '.unity', '.cs', '.jsx', '.json'}

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/merge', methods=['POST'])
def merge_files():
    try:
        if 'files' not in request.files:
            return jsonify({'error': 'No files uploaded'}), 400

        files = request.files.getlist('files')
        output_filename = request.form.get('output_filename', 'merged_output.txt')

        if not files:
            return jsonify({'error': 'No files selected'}), 400

        temp_file = tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.txt', encoding='utf-8')
        try:
            for file in files:
                filename = secure_filename(file.filename)
                file_ext = os.path.splitext(filename)[1].lower()

                if file_ext not in ALLOWED_EXTENSIONS:
                    return jsonify({'error': f'Unsupported file type: {filename}'}), 400

                content = file.read()
                if len(content) > MAX_FILE_SIZE:
                    return jsonify({'error': f'File too large: {filename}'}), 400

                mime_type, _ = mimetypes.guess_type(filename)
                app.logger.info(f"File: {filename}, MIME type: {mime_type}")  # Log MIME type

                # Special handling for XML, Unity, and JSON files
                if file_ext in ['.xml', '.unity', '.json']:
                    if file_ext == '.json':
                        mime_type = 'application/json'
                    else:
                        mime_type = 'application/xml'
                elif file_ext == '.cs':
                    mime_type = 'text/plain'
                elif file_ext == '.jsx':
                    mime_type = 'application/javascript'

                if not mime_type or (not mime_type.startswith('text') and mime_type not in ['application/xml', 'application/json', 'application/javascript']):
                    return jsonify({'error': f'Invalid file type: {filename} (MIME: {mime_type})'}), 400

                try:
                    if file_ext == '.unity':
                        # Custom parsing for Unity files
                        content = content.decode('utf-8')
                        # Remove potential Unity-specific headers
                        content = '\n'.join(line for line in content.split('\n') if not line.startswith('%'))
                        try:
                            # Try parsing as YAML
                            parsed_content = yaml.load(content, Loader=SafeLoader)
                            content = yaml.dump(parsed_content, default_flow_style=False)
                        except yaml.YAMLError:
                            # If YAML parsing fails, keep the original content
                            pass
                    elif file_ext == '.json':
                        # Pretty-print JSON content
                        content = content.decode('utf-8')
                        try:
                            parsed_json = json.loads(content)
                            content = json.dumps(parsed_json, indent=4)
                        except json.JSONDecodeError:
                            # If JSON parsing fails, keep the original content
                            pass
                    else:
                        content = content.decode('utf-8')
                except UnicodeDecodeError:
                    return jsonify({'error': f'Unable to decode file: {filename}. Ensure it\'s a text file.'}), 400

                temp_file.write(f"File: {filename}\n")
                temp_file.write(content)
                temp_file.write('\n\n')

            temp_file.close()
            file_id = str(uuid.uuid4())
            session[file_id] = {
                'path': temp_file.name,
                'filename': output_filename
            }
            return jsonify({'success': True, 'file_id': file_id})
        except Exception as e:
            if not temp_file.closed:
                temp_file.close()
            os.unlink(temp_file.name)
            raise e
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}")
        app.logger.error(traceback.format_exc())
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/download/<file_id>', methods=['GET'])
def download_file(file_id):
    if file_id not in session:
        return jsonify({'error': 'Invalid file ID'}), 400

    file_info = session[file_id]
    try:
        return send_file(file_info['path'], as_attachment=True, download_name=file_info['filename'])
    except TypeError:
        # Fallback for older Flask versions
        return send_file(file_info['path'], as_attachment=True, attachment_filename=file_info['filename'])

@app.after_request
def cleanup(response):
    # This function is intended to clean up temporary files after the response
    # However, using request.view_args may not cover all routes
    file_id = None
    if request.endpoint == 'download_file' and 'file_id' in request.view_args:
        file_id = request.view_args.get('file_id')

    if file_id and file_id in session:
        file_info = session.pop(file_id)
        try:
            os.unlink(file_info['path'])
        except Exception as e:
            app.logger.error(f"Error deleting file {file_info['path']}: {str(e)}")
    return response

if __name__ == '__main__':
    app.run(debug=True)
