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