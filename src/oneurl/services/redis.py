from redis import Redis


def check_if_default_settings_exists():
    r = Redis("localhost", decode_responses=True)
    res = r.hexists("settings:general", "delay")
    if not res:
        r.hset("settings:general", mapping={"delay": "3000"})
