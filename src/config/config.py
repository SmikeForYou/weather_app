import os


class Config:
    cache_ttl: int = 3600
    max_retries: int = 3
    max_cache_size: int = 1000
    request_timeout: int = 10
    log_level: str = 'INFO'
    wtrr_api_url: str = 'http://wttr.in'
    origin_server_url: str = 'http://localhost:3000'
    __instance = None


    @classmethod
    def from_env(cls) -> "Config":
        if cls.__instance is None:
            cls.__instance = cls()
            cls.__instance.cache_ttl = int(os.environ.get('CACHE_TTL', cls.__instance.cache_ttl))
            cls.__instance.max_retries = int(os.environ.get('MAX_RETRIES', cls.__instance.max_retries))
            cls.__instance.max_cache_size = int(os.environ.get('MAX_CACHE_SIZE', cls.__instance.max_cache_size))
            cls.__instance.request_timeout = int(os.environ.get('REQUEST_TIMEOUT', cls.__instance.request_timeout))
            cls.__instance.log_level = os.environ.get('LOG_LEVEL', cls.__instance.log_level)
            cls.__instance.wtrr_api_url = os.environ.get('WTRR_API_URL', cls.__instance.wtrr_api_url)
            cls.__instance.origin_server_url = os.environ.get('ORIGIN_SERVER_URL', cls.__instance.origin_server_url)
        return cls.__instance


config = Config.from_env()


