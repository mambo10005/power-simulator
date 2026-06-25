import redis


def main():

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


if __name__ == "__main__":
    main()