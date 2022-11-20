from urllib.parse import urlsplit
from utils import get_setting


def get_db_port():
    url = get_setting("DATABASE_URL")
    if not url:
        return "--- no database configured ---"

    url = urlsplit(url)
    port = int(url.port or 5432)
    return port


def main():
    port = get_db_port()
    print(port)


if __name__ == "__main__":
    main()
