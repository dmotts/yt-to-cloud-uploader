# YouTube to Google Drive Uploader

This application allows users to download YouTube videos or playlists and upload them directly to their Google Drive. It leverages yt-dlp for downloading, Streamlit for the web interface, and the Google Drive API for file uploads.

## Features
- **Google Sign-In**: Users can authenticate with their Google account to grant the app access to their Google Drive.
- **Download YouTube Content**: Supports downloading individual videos or entire playlists.
- **Organize and Upload**: Automatically creates a 'Youtube Videos' folder in Google Drive and organizes playlist videos into subdirectories.

## Technologies Used
- **yt-dlp**: For downloading videos and playlists from YouTube.
- **Streamlit**: For creating a user-friendly web interface.
- **Google Drive API**: For managing and uploading files to Google Drive.
- **OAuth2**: For Google user authentication and permissions.

## Prerequisites

- Python 3.x
- Google Cloud Project with the Drive API enabled
- OAuth 2.0 credentials from Google (client_id.json, token.json)
- Streamlit

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dmotts/yt-to-gdrive-uploader.git
   cd yt-to-gdrive-uploader
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure OAuth 2.0 credentials:**
   

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

5. **Access the Streamlit app:**
   Open your web browser and go to `http://localhost:8501` to use the application.

## Usage

- **Authenticate with Google**: On first run, click on the "Sign in with Google" button to authenticate and authorize the application to access your Google Drive.
- **Download and Upload**: Enter the URL of the YouTube video or playlist, click "Download and Upload", and the app will download the content and upload it to your Google Drive in a 'Youtube Videos' folder.

## Contributions

Contributions are welcome! It only takes five (5) steps!

To contribute:

1) Fork the repository.

2) Create a new branch: `git checkout -b my-feature-branch`.

3) Make your changes and commit them: `git commit -m 'Add some feature'`.

4) Push to the branch: `git push origin my-feature-branch`.

5) Open a pull request.

Please ensure your code follows the project's coding standards and includes tests where appropriate.

## Let's Connect 🤝

If you find this project useful, please consider connecting with me on GitHub:

[Daley Mottley (dmotts)](https://github.com/dmotts)
