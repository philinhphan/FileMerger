# FileMerger

**FileMerger** is a user-friendly web application designed to help you effortlessly merge multiple code files into a single consolidated document. Whether you're a beginner or an experienced developer, FileMerger streamlines the process of combining files of various programming languages and formats, enhancing your productivity and organization.

---

## 📌 Table of Contents

- [Features](#features)
- [Supported File Types](#supported-file-types)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Usage](#usage)
  - [Uploading Files](#uploading-files)
  - [Merging Files](#merging-files)
  - [Downloading the Merged File](#downloading-the-merged-file)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 🚀 Features

- **Multiple File Uploads**: Upload multiple code files simultaneously.
- **Wide Range of Supported Formats**: Merge files from various programming languages and formats.
- **File Validation**: Ensures only supported file types and sizes are uploaded.
- **Syntax Highlighting**: Preview uploaded files with syntax highlighting for better readability.
- **Secure File Handling**: Utilizes secure methods to handle file uploads and storage.
- **User-Friendly Interface**: Intuitive design suitable for users of all experience levels.

---

## 📝 Supported File Types

FileMerger supports a diverse range of file extensions, ensuring versatility for different coding projects. Below is the list of supported file types:

- `.txt` - Plain Text
- `.java` - Java
- `.xml` - XML
- `.kt` - Kotlin
- `.py` - Python
- `.js` - JavaScript
- `.jsx` - JavaScript XML
- `.json` - JSON
- `.html` - HTML
- `.css` - CSS
- `.unity` - Unity Configuration Files
- `.cs` - C#
- `.md` - Markdown

**Note**: Each file type is handled appropriately to maintain the integrity and readability of the merged output.

---

## 🛠 Getting Started

Follow these instructions to set up and run FileMerger on your local machine.

### 📋 Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.7 or higher**: [Download Python](https://www.python.org/downloads/)
- **pip**: Python package installer (comes with Python)
- **Git**: Version control system (optional, for cloning the repository)

### 📥 Installation

1. **Clone the Repository**

   Open your terminal or command prompt and execute the following command to clone the repository:

   ```bash
   git clone https://github.com/philinhphan/FileMerger.git
   ```

   Alternatively, you can download the ZIP file from the [GitHub repository](https://github.com/philinhphan/FileMerger) and extract it to your desired location.

2. **Navigate to the Project Directory**

   ```bash
   cd FileMerger
   ```

3. **Create a Virtual Environment (Optional but Recommended)**

   Creating a virtual environment helps manage dependencies and avoid conflicts.

   ```bash
   python -m venv venv
   ```

   Activate the virtual environment:

   - **Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **macOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**

   Install the required Python packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

   **Note**: If `requirements.txt` is not present, you can install the necessary packages manually:

   ```bash
   pip install Flask werkzeug PyYAML
   ```

   Additionally, if you plan to handle Markdown conversions, install the `markdown` module:

   ```bash
   pip install markdown
   ```

### 🏃 Running the Application

1. **Start the Flask Server**

   Ensure you're in the project directory and the virtual environment is activated. Then, run:

   ```bash
   python app.py
   ```

   You should see output similar to:

   ```
   * Serving Flask app 'app' (lazy loading)
   * Environment: production
     WARNING: Do not use the development server in a production environment.
     Use a production WSGI server instead.
   * Debug mode: on
   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
   ```

2. **Access the Application**

   Open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

---

## 🎉 Usage

Using FileMerger is straightforward. Follow the steps below to merge your code files seamlessly.

### 📂 Uploading Files

1. **Select Files**

   - Click on the **"Choose Files"** button or the file input area.
   - Select one or multiple files from your computer. Supported file types include `.txt`, `.java`, `.xml`, `.kt`, `.py`, `.js`, `.jsx`, `.json`, `.html`, `.css`, `.unity`, `.cs`, and `.md`.
   - **Note**: Each file must not exceed **5MB** in size.

2. **Review Selected Files**

   - The selected files will appear under the **"Selected Files"** section.
   - Invalid files (unsupported types or oversized) will be highlighted in red with an appropriate error message.
   - You can remove individual files by clicking the **"Remove"** button next to each file or remove all files by clicking the **"Remove All Files"** button.

### 🔀 Merging Files

1. **Specify Output Filename**

   - In the **"Output File Name"** input field, specify the desired name for your merged file. By default, it's set to `merged_output.txt`.
   - You can change the extension (e.g., `.md`, `.html`) based on your preference.

2. **Initiate Merge**

   - Click the **"Merge Files"** button.
   - A progress bar will appear, indicating the upload and merging process.

3. **Completion**

   - Upon successful merging, a success message will appear.
   - The **"Download Merged File"** button will become visible, allowing you to download the consolidated file.
   - All selected files will be cleared from the list automatically.

### 💾 Downloading the Merged File

1. **Download**

   - Click the **"Download Merged File"** button.
   - The merged file will be downloaded to your computer with the specified filename.

2. **Verify**

   - Open the downloaded file to ensure that all your selected files have been merged correctly.

---

## 🛠 Troubleshooting

Encountering issues? Here are some common problems and their solutions:

1. **Unsupported File Type Error**

   - **Cause**: Attempting to upload a file with an unsupported extension.
   - **Solution**: Ensure that the file has one of the supported extensions listed above.

2. **File Too Large Error**

   - **Cause**: Uploading a file larger than 5MB.
   - **Solution**: Compress the file or choose a different file within the size limit.

3. **Server Not Running**

   - **Cause**: The Flask server isn't active.
   - **Solution**: Navigate to the project directory in your terminal and run `python app.py` to start the server.

4. **MIME Type Validation Error**

   - **Cause**: The server detects an invalid MIME type for the uploaded file.
   - **Solution**: Ensure that the file content matches its extension and is a valid text-based file.

5. **Unicode Decode Error**

   - **Cause**: The uploaded file contains characters that cannot be decoded as UTF-8.
   - **Solution**: Verify that the file is a valid text file encoded in UTF-8.

6. **Merged File Not Downloading**

   - **Cause**: An issue with the session or temporary file cleanup.
   - **Solution**: Restart the Flask server and try the merging process again. Ensure that no errors are present in the terminal.

---

## 🤝 Contributing

Contributions are welcome! Whether you're fixing a bug, improving documentation, or adding new features, your efforts help make FileMerger better for everyone.

### 📋 Steps to Contribute

1. **Fork the Repository**

   Click the **"Fork"** button at the top right of the repository page to create your own copy.

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/your-username/FileMerger.git
   ```

3. **Navigate to the Project Directory**

   ```bash
   cd FileMerger
   ```

4. **Create a New Branch**

   ```bash
   git checkout -b feature/YourFeatureName
   ```

5. **Make Your Changes**

   - Implement your feature or fix.
   - Ensure your code follows the project's coding standards.

6. **Commit Your Changes**

   ```bash
   git add .
   git commit -m "Add feature: YourFeatureName"
   ```

7. **Push to Your Fork**

   ```bash
   git push origin feature/YourFeatureName
   ```

8. **Create a Pull Request**

   - Navigate to your fork on GitHub.
   - Click the **"Compare & pull request"** button.
   - Provide a clear description of your changes.
   - Submit the pull request.

### 📝 Guidelines

- **Code Quality**: Ensure your code is clean, well-documented, and follows best practices.
- **Commit Messages**: Write clear and concise commit messages.
- **Testing**: Test your changes thoroughly before submitting.
- **Respect**: Be respectful and considerate in your interactions.

---

## 📝 License

This project is licensed under the [MIT License](https://github.com/philinhphan/FileMerger/blob/main/LICENSE).

---

## 📧 Contact

Have questions or need support? Reach out!

- **Email**: [philinh@gmail.com](philinh@gmail.com)
- **GitHub Issues**: [Open an Issue](https://github.com/philinhphan/FileMerger/issues)

---

Thank you for using **FileMerger**! We hope it enhances your coding workflow and simplifies your file management tasks.

Happy Coding! 🚀