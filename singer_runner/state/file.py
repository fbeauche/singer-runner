import json

from smart_open import smart_open

from singer_runner.state.base import BaseStateStorage

class FileStateStorage(BaseStateStorage):
    def __init__(self, filepath, *args, **kwargs):
        self.filepath = filepath
        super(FileStatePersister, self).__init__(*args, **kwargs)

    def dump(self, state):
        with smart_open(self.filepath, 'w') as file:
            json.dump(state, file)
        self.state = state

    def load(self):
        with smart_open(self.filepath, 'r') as file:
            state = json.load(self.file)
        self.state = state
        return state