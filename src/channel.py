from googleapiclient.discovery import build
import os
import json

api_key = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""
    __youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = self.__youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @property
    def title(self):
        return (self.channel['items'][0]['snippet']["title"])

    @property
    def video_count(self):
        return (self.channel['items'][0]['statistics']['videoCount'])

    @property
    def url(self):
        return (self.channel['items'][0]['snippet']['thumbnails']['default']['url'])

    @property
    def channel_id(self):
        return self.__channel_id

    @classmethod
    def get_service(cls):
        """класс-метод , возвращающий объект для работы с YouTube API"""
        return cls.__youtube

    def to_json(self, file_name: str) -> None:
        """метод, сохраняющий в файл значения атрибутов экземпляра Channel"""
        data = json.dumps(self.channel)
        with open (file_name, 'w', encoding='UTF-8') as file_json:
            file_json.write(data)
