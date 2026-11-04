class CacheKeeper:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Refresh the key's recency by popping and re-inserting it at the end
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            # Pop the oldest (least recently used) item from the front
            self.cache.popitem(last=False)

        self.cache[key] = value
