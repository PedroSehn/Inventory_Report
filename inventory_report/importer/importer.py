from abc import ABC, abstractclassmethod
# so pra pusher


class Importer(ABC):
    @abstractclassmethod
    def import_data(path: str):
        pass
