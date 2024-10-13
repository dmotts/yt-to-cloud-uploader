"""Implementation of the protocols defined in base.py for the Gooogle Cloud Platform.

Here is a mapping of the protocols to the classes and methods in this module:
Auth -> GoogleAuth
Service -> GoogleDriveService
"""

import os

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Configuration for OAuth2
SCOPES = ['https://www.googleapis.com/auth/drive.file']


class GoogleAuth:
    def __init__(self, client_secrets_file: str):
        self.creds = None
        self.client_secrets_file = client_secrets_file

    def sign_in(self):
        if 'token.json' in os.listdir():
            self.creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and shecreds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.client_secrets_file, SCOPES)
                self.creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(self.creds.to_json())

    def get_credentials(self):
        return self.creds


class GoogleDriveService:
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
