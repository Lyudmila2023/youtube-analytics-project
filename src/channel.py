import os
from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.channel_data = channel['items'][0]
        print(f"название канала: {self.channel_data['snippet']['title']}")
        print(f"Описание: {self.channel_data['snippet']['description']}")
        print(f"Колличество подписчиков: {self.channel_data['statistics']['subscriberCount']}")
        print(f"Колличество просмотров: {self.channel_data['statistics']['viewCount']}")
        print(f"Дата создания: {self.channel_data['snippet']['publishedAt']}")
