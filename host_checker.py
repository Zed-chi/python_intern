import argparse
from urllib.parse import urlparse, urlunparse
import requests


def is_alive_host(hostname):
    """Проверить, что запрашиваемый хост возвращает http status 100<=x<400."""
    try:
        response = requests.head(hostname)
        status = response.status_code
        print(f"{hostname} {status}")
        return status < 400 and status > 100
    except Exception as e:
        return False


def get_host():
    parser = argparse.ArgumentParser(description='Host checker')
    parser.add_argument(dest="host", help="url to check")
    args = parser.parse_args()
    return args.host


def check_and_correct_host(host):    
    parsed_url = urlparse(host)
    if not parsed_url.scheme:        
        return urlunparse(['https', host, '/', '', '', ''])
    return host


def main():
    host = get_host()
    host = check_and_correct_host(host)
    host_status = is_alive_host(host)
    print(f"{host} is {'alive' if host_status else 'not alive'}")


if __name__ == "__main__":
    main()
