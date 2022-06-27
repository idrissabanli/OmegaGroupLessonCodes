import redis

class Config:
    testing = True


class RedisConfig:
    REDIS_BROKER_URL = 'redis://localhost:6379'
    CHANNEL_NAME = "events"

    @property
    def client(self):
        try:
            return redis.Redis.from_url(self.REDIS_BROKER_URL)
        except ConnectionError:
            raise ConnectionError


class EmailConfig:
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 465
    EMAIL_HOST_USER = 'idris.sabanli@gmail.com'
    EMAIL_HOST_PASSWORD = 'fpmcfzklqhzubuqb'
