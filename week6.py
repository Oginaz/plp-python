import requests
import os
import hashlib
from urllib.parse import urlparse
from datetime import datetime

def fetch_images(urls):
    """
    Download multiple images from a list of URLs while:
    - Avoiding duplicates
    - Checking safe headers
    - Respecting Ubuntu principles of community and sharing
    """
    print("Ubuntu Image Fetcher")
    print('"A person is a person through other persons."\n')

    # Create directory if it doesn't exist
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    # Track already downloaded images (by hash)
    downloaded_hashes = set()

    for url in urls:
        try:
            print(f"Fetching: {url}")
            response = requests.get(url, timeout=10, stream=True)
            response.raise_for_status()

            # --- Precaution: Check important HTTP headers ---
            content_type = response.headers.get("Content-Type", "")
            if not content_type.startswith("image/"):
                print(f"Skipped: {url} (Not an image, Content-Type: {content_type})")
                continue

            # Extract filename or generate one
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)

            if not filename:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"image_{timestamp}.jpg"

            filepath = os.path.join(save_dir, filename)

            # Compute file hash to prevent duplicates
            file_bytes = response.content
            file_hash = hashlib.md5(file_bytes).hexdigest()

            if file_hash in downloaded_hashes:
                print(f"Duplicate skipped: {filename}")
                continue
            downloaded_hashes.add(file_hash)

            # Save the image
            with open(filepath, "wb") as f:
                f.write(file_bytes)

            print(f"✅ Saved: {filename} -> {filepath}\n")

        except requests.exceptions.RequestException as e:
            print(f"❌ Connection error for {url}: {e}")
        except Exception as e:
            print(f"❌ Unexpected error for {url}: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A mindful tool for community sharing\n")

    # Accept multiple URLs
    urls_input = input("Enter image URLs (separated by commas): ")
    urls = [u.strip() for u in urls_input.split(",") if u.strip()]

    if urls:
        fetch_images(urls)
    else:
        print("❌ No valid URLs provided.")

if __name__ == "__main__":
    main()
