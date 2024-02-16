import json
import os

from dotenv import load_dotenv
from googleapiclient.discovery import build

# Load environment variables from a .env file
load_dotenv()

# Get the YouTube API key from the environment variables
api_key = os.getenv("YT_API_KEY")

# Create a YouTube API client
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """
    A class to represent a YouTube channel.

    Attributes
    ----------
    _channel_id : str
        The id of the YouTube channel.
    channel : dict
        The information about the YouTube channel fetched from the YouTube API.
    title : str
        The name of the YouTube channel.
    channel_description : str
        The description of the YouTube channel.
    url : str
        The URL of the YouTube channel.
    subscribers : int
        The number of subscribers of the YouTube channel.
    video_count : int
        The number of videos uploaded on the YouTube channel.
    view_count : int
        The total number of views across all videos on the YouTube channel.

    Methods
    -------
    print_info():
        Prints the information about the YouTube channel in a JSON-like format.
    Get_service():
        Returns an object for working with the YouTube API.
    To_json():
        Writes the channel information to a JSON file.
    """

    @property
    def channel_id(self):
        """ Returns the channel id. """
        return self._channel_id

    def __init__(self, channel_id: str) -> None:
        """
        Constructs all the necessary attributes for the Channel object.

        Parameters
        ----------
            channel_id : str
                The id of the YouTube channel.
        """
        self._channel_id = channel_id
        self.channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.url = f"https://www.youtube.com/channel/{self.channel['items'][0]['id']}"
        self.subscribers = int(self.channel['items'][0]['statistics']['subscriberCount'])
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.view_count = self.channel['items'][0]['statistics']['viewCount']

    def print_info(self) -> None:
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        """ Returns an object for working with the YouTube API. """
        return youtube

    def to_json(self, filename):
        """
        Writes the channel information to a JSON file.

        Parameters
        ----------
            filename : str
                The name of the file to write to.
        """
        data = {
            'id': self.channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscribers': self.subscribers,
            'video_count': self.video_count,
            'view_count': self.view_count
        }

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(json.dumps(data, indent=2, ensure_ascii=False))

    def __str__(self):
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        return self.subscribers + other.subscribers

    def __sub__(self, other):
        return self.subscribers - other.subscribers

    def __gt__(self, other):
        return self.subscribers > other.subscribers

    def __ge__(self, other):
        return self.subscribers >= other.subscribers

    def __lt__(self, other):
        return self.subscribers < other.subscribers

    def __le__(self, other):
        return self.subscribers <= other.subscribers

    def __eq__(self, other):
        return self.subscribers == other.subscribers
