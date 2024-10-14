"""Defines the various interfaces used in the application."""

from typing import Protocol


class Auth(Protocol):
    def sign_in(self):
        ...

    def get_credentials(self):
        ...


class StorageService(Protocol):
    def create_folder(self, folder_name: str, parent_id=None):
        ...

    def upload_file(self, file_path: str, folder_id):
        ...


class VideoDownloader(Protocol):
    def download_video(self, url: str):
        ...

    def download_playlist(self, url: str):
        ...


class VideoUploader(Protocol):
    def upload_video(self, video_path: str):
        ...

    def upload_playlist(self, video_paths: str, playlist_title: str):
        ...
