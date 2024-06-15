import os
import streamlit as st
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import yt_dlp

# Configuration for OAuth2
SCOPES = ['https://www.googleapis.com/auth/drive.file']
CLIENT_SECRETS_FILE = 'client_secrets.json'  # Path to your OAuth2 client secrets file

class GoogleAuth:
    def __init__(self):
        self.creds = None

    def sign_in(self):
        if 'token.json' in os.listdir():
            self.creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and shecreds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
                self.creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(self.creds.to_json())

    def get_credentials(self):
        return self.creds

class DriveService:
    def __init__(self, creds):
        self.service = build('drive', 'v3', credentials=creds)

    def create_folder(self, folder_name, parent_id=None):
        file_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        if parent_id:
            file_metadata['parents'] = [parent_id]
        folder = self.service.files().create(body=file_metadata, fields='id').execute()
        return folder.get('id')

    def upload_file(self, file_path, folder_id):
        file_name = os.path.basename(file_path)
        media = MediaFileUpload(file_path, resumable=True)
        file_metadata = {
            'name': file_name,
            'parents': [folder_id]
        }
        file = self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        return file.get('id')

class YouTubeDownloader:
    def __init__(self):
        self.ydl_opts = {
            'format': 'best',
            'outtmpl': './downloads/%(title)s.%(ext)s',
            'quiet': True,
            'postprocessors': [{'key': 'FFmpegVideoConvertor', 'preferedformat': 'mp4'}]
        }

    def download_video(self, url):
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            return ydl.prepare_filename(info_dict)

    def download_playlist(self, url):
        self.ydl_opts['noplaylist'] = False
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            return [ydl.prepare_filename(entry) for entry in info_dict['entries']]

class YouTubeDriveUploader:
    def __init__(self, drive_service):
        self.drive_service = drive_service

    def upload_video(self, video_path):
        folder_id = self._get_or_create_folder('Youtube Videos')
        self.drive_service.upload_file(video_path, folder_id)

    def upload_playlist(self, video_paths, playlist_title):
        parent_folder_id = self._get_or_create_folder('Youtube Videos')
        playlist_folder_id = self._get_or_create_folder(playlist_title, parent_folder_id)
        for video_path in video_paths:
            self.drive_service.upload_file(video_path, playlist_folder_id)

    def _get_or_create_folder(self, folder_name, parent_id=None):
        query = f"name = '{folder_name}' and mimeType = 'application/vnd.google-apps.folder'"
        if parent_id:
            query += f" and '{parent_id}' in parents"
        results = self.drive_service.service.files().list(q=query, fields="files(id, name)").execute()
        folders = results.get('files', [])
        if folders:
            return folders[0]['id']
        else:
            return self.drive_service.create_folder(folder_name, parent_id)

def main():
    st.title("YouTube to Google Drive Uploader")

    google_logo_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Google_%22G%22_Logo.svg/512px-Google_%22G%22_Logo.svg.png"
    if st.button("Sign in with Google", key='google-signin'):
        st.markdown(
            f'<a href="#" class="btn btn-primary"><img src="{google_logo_url}" width="20" height="20" alt="Google Sign In" /> Sign in with Google</a>',
            unsafe_allow_html=True
        )
        auth = GoogleAuth()
        auth.sign_in()
        st.success("Successfully signed in!")

    creds = auth.get_credentials()
    if creds:
        drive_service = DriveService(creds)
        youtube_downloader = YouTubeDownloader()
        uploader = YouTubeDriveUploader(drive_service)

        video_url = st.text_input("Enter YouTube Video or Playlist URL:")

        if st.button("Download and Upload"):
            if "playlist" in video_url:
                st.write("Processing playlist...")
                with st.spinner('Downloading playlist...'):
                    video_paths = youtube_downloader.download_playlist(video_url)
                uploader.upload_playlist(video_paths, "Downloaded Playlist")
                st.success("Playlist uploaded successfully!")
            else:
                st.write("Processing video...")
                with st.spinner('Downloading video...'):
                    video_path = youtube_downloader.download_video(video_url)
                uploader.upload_video(video_path)
                st.success("Video uploaded successfully!")

if __name__ == "__main__":
    main()