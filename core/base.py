"""Defines the various interfaces used in the application."""

from typing import Protocol


class Auth(Protocol):
    def sign_in(self):
        ...

    def get_credentials(self):
        ...


class Service(Protocol):
    def create_folder(self, folder_name, parent_id=None):
        ...

    def upload_file(self, file_path, folder_id):
        ...


class Downloader(Protocol):
    def download_video(self, url):
        ...

    def download_playlist(self, url):
        ...


class Uploader(Protocol):
    def upload_video(self, video_path):
        ...

    def upload_playlist(self, video_paths, playlist_title):
        ...
