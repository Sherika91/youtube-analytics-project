import json
import os

from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

api_key = os.getenv("YT_API_KEY")

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """
    A class to represent a YouTube channel.

    ...

    Attributes
    ----------
    channel_id : str
        the id of the channel

    Methods
    -------
    print_info():
        Output channel info in json-like format
    """

    def __init__(self, channel_id: str) -> None:
        self.channel_id = channel_id

    def print_info(self) -> None:
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))
