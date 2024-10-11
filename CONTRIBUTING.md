# Contributing to YouTube to Cloud Uploader

Thank you for considering contributing to the **YouTube to Cloud Uploader** project! We appreciate your help in improving this application and making it more useful for everyone.

## How to Contribute

Follow these steps to contribute to the project:

### 1. Fork the Repository

Click the "Fork" button on the top right of the repository to create a copy in your own GitHub account.

Clone your fork to your local machine:

```bash
git clone https://github.com/your-username/yt-to-cloud-uploader.git
cd yt-to-cloud-uploader
```

### 2. Create a Branch

Create a new branch for your feature, bug fix, or improvement:

 ```bash
   git checkout -b feature/my-new-feature
   ```

### 3. Make Your Changes

Make sure to test your changes thoroughly.

• If you are adding new features, update the documentation (README.md).
• Follow the code style guidelines used in the project.
• Ensure that your code works with Python 3.x.

### 4. Commit Your Changes

Once you’re satisfied with your work, commit your changes with a meaningful message:

 ```bash
   git commit -m "Add my awesome new feature"

   ```

### 5. Push to GitHub

Push your branch to GitHub:

 ```bash
     git push origin feature/my-new-feature

   ```

### 6. Submit a Pull Request (PR)

Submit a pull request through GitHub:

1. Go to the repository on GitHub and click on the "Pull requests" tab.
2. Click on the "New pull request" button.
3. Select your branch from the dropdown menu and compare it with the main branch.
4. Provide a description of your changes and click on "Create pull request."

## Please ensure that

• You have followed the steps outlined in this guide.
• Your code adheres to the existing codebase.
• You have tested the functionality thoroughly.

We’ll review your PR as soon as possible.

### Reporting Issues

If you encounter a bug, performance issue, or have a feature request, feel free to create an issue. Please provide the following information when submitting an issue:

• A clear title and description.
• Steps to reproduce the issue (if applicable).
• Any error logs or screenshots to help identify the problem.

### Code Style

Please adhere to the following code style guidelines:

• Use clear, descriptive variable and function names.
• Use consistent indentation and whitespace (4 spaces per indentation level).
• Follow the existing structure and organization of the codebase.

### Development Setup

1. Clone the repository and navigate to the project directory:

   ```bash
   git clone https://github.com/dmotts/yt-to-cloud-uploader.git
   cd yt-to-cloud-uploader

   ```

2. Install the required dependencies by running:

   ```bash
   pip install -r requirements.txt

   ```

3. Configure OAuth 2.0 credentials:

  • Place your client_id.json and token.json files in the project directory.
  • Ensure your Google Cloud Project has the Drive API enabled.

Run the application:

   ```bash
   streamlit run app.py
   ```

Access the app in your browser at <http://localhost:8501>.

** Pull Request Guidelines

When submitting a pull request, make sure to:

• Include a clear description of your changes.
• Reference any related issue numbers (e.g., Fixes #123).
• Add or update tests if necessary.
• Update documentation if you’ve introduced new features or significant changes.

** Feature Requests

We welcome feature requests! If you have an idea for a new feature, feel free to open an issue with the tag "feature request" and describe your idea. We’ll discuss it with the community and decide on the next steps.

### License

By contributing to this repository, you agree that your contributions will be licensed under the MIT License.

Thank you again for your interest in improving YouTube to Cloud Uploader. We look forward to your contributions!
