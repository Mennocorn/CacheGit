from MediaManager import FileMaker
import json


class Cache:

    def __init__(self, file: str):
        self.file = FileMaker(file)
        self.file.is_json()
        self._cache = None

    def load(self) -> None:
        with open(str(self.file)) as file_to_load_from:
            self._cache = json.load(file_to_load_from)

    async def save(self):
        async with open(str(self.file), 'w') as file_to_save_to:
            json.dump(self._cache, file_to_save_to, indent=4)

    @property
    def cache(self):
        return self._cache

    @cache.setter
    def cache(self, value):
        self._cache = value

