import os
import subprocess

# Define the URLs of proxy lists to update from
PROXY_LIST_URLS = {
    "https": "https://www.proxy-list.download/api/v1/get?type=https",
    "socks4": "https://www.proxy-list.download/api/v1/get?type=socks4",
    "socks5": "https://www.proxy-list.download/api/v1/get?type=socks5"
}

# Define the paths where the proxies will be saved
FILE_PATHS = {
    "https": "proxy_list_https.txt",
    "socks4": "proxy_list_socks4.txt",
    "socks5": "proxy_list_socks5.txt"
}

def update_proxy_list(url, file_path):
    try:
        # Use curl to download the file with retries
        subprocess.run([
            'curl', '--retry', '3', '-s', '-L', url, '-o', file_path
        ], check=True)
        with open(file_path, 'r') as file:
            proxies = file.readlines()
        proxies = [proxy.strip() for proxy in proxies if proxy.strip()]
        with open(file_path, 'w') as file:
            file.write("\n".join(proxies))
        print(f"Updated {file_path} with {len(proxies)} proxies.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to update {file_path}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    for proxy_type, url in PROXY_LIST_URLS.items():
        file_path = FILE_PATHS[proxy_type]
        update_proxy_list(url, file_path)

if __name__ == "__main__":
    main()
