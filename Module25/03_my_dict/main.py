class MyDict(dict):
    def get(self, key):
        super().get(key, 0)
