from collections import deque

class LRUCache:
    def __init__(self, capacity):
        """
        Initializes the cache with a given capacity.
        :param capacity: The maximum number of items the cache can hold.
        """
        self.capacity = capacity
        self.cache = {}  # Stores key-value pairs
        self.order = deque()  # Stores keys in order of use (most recent at the end)

    def get(self, key):
        """
        Retrieves an item from the cache.
        If the key exists, it updates its position to be the most recently used.
        :param key: The key of the item to retrieve.
        :return: The value associated with the key, or None if not found.
        """
        if key not in self.cache:
            return None
        
        # Move the accessed key to the end (most recently used)
        self.order.remove(key)
        self.order.append(key)
        
        return self.cache[key]

    def put(self, key, value):
        """
        Adds or updates an item in the cache.
        If the cache is at capacity, it evicts the least recently used item.
        :param key: The key of the item.
        :param value: The value of the item.
        """
        if key in self.cache:
            # If the key exists, remove it from its current position in the order
            self.order.remove(key)
        
        elif len(self.cache) >= self.capacity:
            # If at capacity, evict the least recently used key (from the front)
            lru_key = self.order.popleft()
            del self.cache[lru_key]
        
        # Add the new or updated item to the cache and the order
        self.cache[key] = value
        self.order.append(key)