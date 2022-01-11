from typing import Dict


class MyDict(Dict):
    def get(self, key, default=0):
        super().get(key, default)

