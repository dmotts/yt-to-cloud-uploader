import streamlit as st

from core.gcloud import GoogleAuth, GoogleDriveService
from core.youtube import YouTubeDownloader, YouTubeDriveUploader

CLIENT_SECRETS_FILE = 'client_secrets.json'  # Path to your OAuth2 client secrets file


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
        drive_service = GoogleDriveService(creds)
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
