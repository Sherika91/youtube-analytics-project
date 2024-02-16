import json
import os

from dotenv import load_dotenv
from googleapiclient.discovery import build

# Load environment variables from a .env file
load_dotenv()

# Get the YouTube API key from environment variables
api_key = os.getenv("YT_API_KEY")

# Create a resource object for interacting with the YouTube API
youtube = build('youtube', 'v3', developerKey=api_key)


class Video:
    """
    A class to reresent a video from YouTube channel.

    Attributes
    video_id: str
        The unique identifier of the YouTube video.
    video: dict
        The information about the Video fetched from the YouTube API.
    video_titile: str
        The name of the YouTube Video.
    video_url: str
        The url of the YouTube Video.
    view_count: int
        The total number of views.
    like_count: int
        The total number of likes.

    Methods
    -------
    print_info():
        Prints the video information in JSON format.
    """

    @property
    def video_id(self):
        """ The unique identifier of the YouTube video. """
        return self._video_id

    def __init__(self, video_id: str) -> None:
        """
        Constructs all the necessary attributes for the Video object.

        Parameters
        ----------
            video_id: str
                    The unique identifier of the YouTube video.
        """
        self._video_id = video_id
        self.video = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                           id=self.video_id
                                           ).execute()
        self.video_title: str = self.video['items'][0]['snippet']['title']
        self.video_url: str = f"https://www.youtube.com/watch?v={self.video_id}"
        self.view_count: int = self.video['items'][0]['statistics']['viewCount']
        self.like_count: int = self.video['items'][0]['statistics']['likeCount']

    def __str__(self):
        """ Returns the title of the YouTube video. """
        return self.video_title

    def print_info(self):
        """ Prints the video information in JSON format. """
        print(json.dumps(self.video, indent=2, ensure_ascii=False))


class PLVideo(Video):
    """
    A class to represent a video from a YouTube playlyst.
    Inherites from the Video class.

    Attributes
    ----------
    playlist_id : str
        The unique identifiref of the YouTube playlist.
    """

    def __init__(self, video_id: str, playlist_id: str):
        """
        Comstucts all the necessary attributes for the PLVideo objects.

        Parameters
        ----------
            video_id : str
                The uniqie identifier of the YouTube video.
            playlist_id : str
                The niqie identifier of the YouTube playlist.
        """
        super().__init__(video_id)
        self.playlist_id = playlist_id
