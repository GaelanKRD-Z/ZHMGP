import requests
import os

# Define the URLs of proxy lists to update from
PROXY_LIST_URLS = [
    "https://www.proxy-list.download/api/v1/get?type=https",
    "https://www.proxy-list.download/api/v1/get?type=socks4",
    "https://www.proxy-list.download/api/v1/get?type=socks5"
]

# Define the paths where the proxies will be saved
FILE_PATHS = {
    "https": "proxy_list_https.txt",
    "socks4": "proxy_list_socks4.txt",
    "socks5": "proxy_list_socks5.txt"
}

def update_proxy_list(url, file_path):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        proxies = response.text.strip().split("\r\n")
        with open(file_path, 'w') as file:
            file.write("\n".join(proxies))
        print(f"Updated {file_path} with {len(proxies)} proxies.")
    except requests.RequestException as e:
        print(f"Failed to update {file_path}: {e}")

def main():
    for proxy_type, url in zip(FILE_PATHS.keys(), PROXY_LIST_URLS):
        file_path = FILE_PATHS[proxy_type]
        update_proxy_list(url, file_path)

if __name__ == "__main__":
    main()
