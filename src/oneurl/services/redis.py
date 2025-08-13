import os

from redis import Redis
from dotenv import load_dotenv

load_dotenv()

r = Redis(
    os.getenv("REDIS_HOST", "localhost"),
    int(os.getenv("REDIS_PORT", "6379")),
    int(os.getenv("REDIS_DB", "0")),
    decode_responses=True,
)


def check_if_default_settings_exists():
    res = r.hexists("settings:general", "delay")
    if not res:
        r.hset("settings:general", mapping={"delay": "3000"})
