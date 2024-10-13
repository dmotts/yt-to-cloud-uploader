"""Implementations of the protocols for downloading and uploading YouTube videos.

Mapping of the protocols to the classes and methods in this module:
Downloader -> YouTubeDownloader
Uploader -> YouTubeDriveUploader
"""

import yt_dlp


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
