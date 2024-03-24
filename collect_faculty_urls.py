import requests
from bs4 import BeautifulSoup

# The URL of the webpage you want to scrape
url = 'https://mcb-seattle.edu/directory/faculty/?_sft_aoi=computational-biology'

def extract_faculty_urls(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')
            # Find all <a> tags with the specified class attribute
            links = soup.find_all('a', class_='cl-element-featured_media__anchor')
            # Extract the URLs from the href attribute of each tag
            urls = [link['href'] for link in links if 'href' in link.attrs]
            print(f"Found URLs: {urls}")
            return urls
        else:
            print(f"Failed to retrieve webpage. Status code: {response.status_code}")
            return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Call the function with the URL
extracted_urls = extract_faculty_urls(url)

# If you need to process the extracted URLs further, you can do so here.
# For example, print them one by one:
for url in extracted_urls:
    print(url)
