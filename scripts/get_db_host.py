from urllib.parse import urlsplit

from utils import get_setting


def get_db_host():
    url = get_setting("DATABASE_URL")
    if not url:
        return "--- no database configured ---"

    url = urlsplit(url)
    host = url.hostname
    return host


def main():
    host = get_db_host()
    print(host)


if __name__ == "__main__":
    main()
