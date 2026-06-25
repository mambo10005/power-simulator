import redis

r = redis.Redis(
    host="localhost",
    port=6379
)

r.set(
    "market",
    "ercot"
)

print(
    r.get("market")
)