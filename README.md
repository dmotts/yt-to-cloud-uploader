<h1 align="center">  📽️📥 YouTube to Cloud Uploader 🪂🌥️ </h1>

<p align="center">
<a href="https://github.com/dmotts/yt-to-cloud-uploader/issues/new?assignees=&labels=enhancement&projects=&template=feature_request.yml&title=%5BFeature+Request%5D+">Request Feature</a>
     ·
    <a href="https://github.com/dmotts/yt-to-cloud-uploader/issues/new?assignees=&labels=bug&projects=&template=bug_report.yml&title=%5BBug%5D+">Report Bug</a>
 
</p>

<div align="center">
<p>

[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)
![GitHub forks](https://img.shields.io/github/forks/dmotts/yt-to-cloud-uploader)
![GitHub Repo stars](https://img.shields.io/github/stars/dmotts/yt-to-cloud-uploader)
![GitHub contributors](https://img.shields.io/github/contributors/dmotts/yt-to-cloud-uploader)
![GitHub last commit](https://img.shields.io/github/last-commit/dmotts/yt-to-cloud-uploader)
![GitHub repo size](https://img.shields.io/github/repo-size/dmotts/yt-to-cloud-uploader)
![GitHub total lines](https://sloc.xyz/github/dmotts/yt-to-cloud-uploader)
![Github](https://img.shields.io/github/license/dmotts/yt-to-cloud-uploader)
![GitHub issues](https://img.shields.io/github/issues/dmotts/yt-to-cloud-uploader)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/dmotts/yt-to-cloud-uploader)
![GitHub pull requests](https://img.shields.io/github/issues-pr/dmotts/yt-to-cloud-uploader)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/dmotts/yt-to-cloud-uploader)
</p>
</div>

This application allows users to download YouTube videos or playlists and upload them directly to their Google Drive. 

## Features 📰
✅ **Google Sign-In**: Users can authenticate with their Google account to grant the app access to their Google Drive.

✅ **Download YouTube Content**: Supports downloading individual videos or entire playlists.

✅ **Organize and Upload**: Automatically creates a 'Youtube Videos' folder in Google Drive and organizes playlist videos into subdirectories.

## Technologies Used 🛸 
- [**yt-dlp**](https://github.com/yt-dlp/yt-dlp#readme): For downloading videos and playlists from YouTube.
- [**Streamlit**](https://docs.streamlit.io/): For creating a user-friendly web interface.
- [**Google Drive API**](https://developers.google.com/drive/api): For managing and uploading files to Google Drive.
- [**OAuth2**](https://oauth.net/2/): For Google user authentication and permissions.


## Prerequisites 🐣

- Python 3.x
- Google Cloud Project with the Drive API enabled
- OAuth 2.0 credentials from Google (client_id.json, token.json)
- Streamlit

## Setup Instructions 📜

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dmotts/yt-to-cloud-uploader.git
   cd yt-to-cloud-uploader
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure OAuth 2.0 credentials:**
   

4. **Run the application:**
   ```bash
   streamlit run main.py
   ```

5. **Access the Streamlit app:**
   Open your web browser and go to `http://localhost:8501` to use the application.

## Usage 🕹️

- **Authenticate with Google**: On first run, click on the "Sign in with Google" button to authenticate and authorize the application to access your Google Drive.
- **Download and Upload**: Enter the URL of the YouTube video or playlist, click "Download and Upload", and the app will download the content and upload it to your Google Drive in a 'Youtube Videos' folder.

## Help Wanted 🪧

- [ ] **OneDrive API Setup**: Add OneDrive as a cloud storage option.
- [ ] **Dropbox API Setup**: Add Dropbox as a cloud storage option.
- [ ] **Landing Page**: Convert the frontend from streamlit to a user-friendly, attractive and simple landing page.
- [ ] **Authentication**: Add user sign in authentication.

## Report A Bug 🪰

If you encounter any issues or have questions, feel free to [open an issue](https://github.com/dmotts/yt-to-cloud-uploader/issues/new?assignees=&labels=bug&projects=&template=bug_report.yml&title=%5BBug%5D+) or reach out to the maintainers.

## Contributions 🧑‍🔧👷‍♀️🏗️🏢

Contributions are welcome! It only takes five (5) steps!

To contribute:

1) Fork the repository.

2) Create a new branch: `git checkout -b my-feature-branch`.

3) Make your changes and commit them: `git commit -m 'Add some feature'`.

4) Push to the branch: `git push origin my-feature-branch`.

5) Open a pull request.

<p align="center" ><strong><em>Please read our <a href="https://github.com/dmotts/yt-to-cloud-uploader/blob/main/CONTRIBUTING.md" >Contributing Guidelines</a> to get started!</em></strong> 🚀</p>

<h2 name="contributors" align="center">Say 'Hi' To Our Contributors!</h2>

<p align="center">
  <a href="https://github.com/dmotts">
    <img src="https://github.com/dmotts.png" width="100" height="100" style="border-radius: 50%;" alt="dmotts"/>
  </a>
  <a href="https://github.com/Brijeshthummar02">
    <img src="https://github.com/Brijeshthummar02.png" width="100" height="100" style="border-radius: 50%;" alt="Brijeshthummar02"/>
  </a>
  <a href="https://github.com/swarupn17">
    <img src="https://github.com/swarupn17.png" width="100" height="100" style="border-radius: 50%;" alt="swarupn17"/>
  </a>
     <a href="https://github.com/HomerusJa">
    <img src="https://github.com/HomerusJa.png" width="100" height="100" style="border-radius: 50%;" alt="HomerusJa" />
  </a>
</p>

<p align="center">🫶 <em>Thank you for your support! </em>🙌 </p>
<hr>
<h2 align="center"> 🌎 Let's Stay Connected 🤜🤛 </h2>

<p align="center"> If you like this project and would like to see more features or show your support.</p>
<p align="center"> Feel free to reach out to the developer(s) and give this project a ⭐!</p>

