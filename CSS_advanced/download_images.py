import requests
import os
from urllib.parse import urlparse

def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Successfully downloaded {filename}")
    else:
        print(f"Failed to download {filename}")

def main():
    # Create images directory if it doesn't exist
    if not os.path.exists('images'):
        os.makedirs('images')

    # Dictionary of image URLs and their corresponding filenames
    images = {
        # About section
        'https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05': 'pic-about-01.jpg',
        
        # Work section
        'https://images.unsplash.com/photo-1461988320302-91bde64fc8e4': 'pic-work-01.jpg',
        'https://images.unsplash.com/photo-1461749280684-dccba630e2f6': 'pic-work-02.jpg',
        'https://images.unsplash.com/photo-1498050108023-c5249f4df085': 'pic-work-03.jpg',
        
        # Article section
        'https://images.unsplash.com/photo-1525609004556-c46c7d6cf023': 'pic-article-01.jpg',
        'https://images.unsplash.com/photo-1504384764586-bb4cdc1707b0': 'pic-article-02.jpg',
        'https://images.unsplash.com/photo-1476357471311-43c0db9fb2b4': 'pic-article-03.jpg',
        
        # Team/Testimonial section
        'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d': 'pic-person-01.jpg',
        'https://images.unsplash.com/photo-1438761681033-6461ffad8d80': 'pic-person-02.jpg',
        'https://images.unsplash.com/photo-1519345182560-3f2917c472ef': 'pic-person-03.jpg',
    }

    # Download each image
    for url, filename in images.items():
        download_image(url, os.path.join('images', filename))

if __name__ == "__main__":
    main() 