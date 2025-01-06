from src.config import config
from src.services.cache.dto import Weather


class WeatherCacheService:
    def __init__(self, max_cache_size: int = config.max_cache_size, cache_ttl: int = config.cache_ttl):
        self.cache: dict[str, Weather] = dict()
        self.max_cache_size = max_cache_size
        self.cache_ttl = cache_ttl

    def get(self, city: str) -> Weather | None:
        cached_item = self.cache.get(city)
        if cached_item is not None and cached_item.is_expired(self.cache_ttl):
            self.cache.pop(city)
            return None
        return cached_item

    def set(self, city, value: Weather):
        if len(self.cache) >= self.max_cache_size:
            self._drop_oldest()
        return self.cache.update({city: value})

    def _drop_oldest(self):
        oldest = min(self.cache, key=lambda k: self.cache[k].timestamp)
        self.cache.pop(oldest)