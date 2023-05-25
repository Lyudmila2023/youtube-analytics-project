import os
import json
from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel_info = self.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = self.channel_info['items'][0]['snippet']['title']
        self.url = self.channel_info['items'][0]['snippet']['thumbnails']["default"]["url"]
        self.description = self.channel_info['items'][0]['snippet']['description']
        self.subscriberCount = int(self.channel_info['items'][0]['statistics']['subscriberCount'])
        self.video_count = self.channel_info['items'][0]['statistics']['videoCount']
        self.viewCount = self.channel_info['items'][0]['statistics']['viewCount']

    def __str__(self):
        return f"{self.title} - {self.url}"

    def __add__(self, other):
        return self.subscriberCount + other.subscriberCount

    def __sub__(self, other):
        return self.subscriberCount - other.subscriberCount

    def __lt__(self, other):
        return self.subscriberCount < other.subscriberCount

    def __le__(self, other):
        return self.subscriberCount <= other.subscriberCount

    def __gt__(self, other):
        return self.subscriberCount > other.subscriberCount

    def __ge__(self, other):
        return self.subscriberCount >= other.subscriberCount

    def __eq__(self, other):
        return self.subscriberCount == other.subscriberCount


    @property
    def channel_id(self):
        return self.__channel_id()

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        service = build('youtube', 'v3', developerKey=api_key)
        return service

    def to_json(self, title):
        file_json = Channel.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        with open(title, "w", encoding="UTF-8") as file:
            json.dump(file_json, file)





