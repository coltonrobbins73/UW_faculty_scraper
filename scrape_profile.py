import requests
from bs4 import BeautifulSoup
import webbrowser
import re
import pandas as pd

# The URL to open if keywords are found
link_to_open = 'https://example-link-if-keywords-found.com'

def scrape_and_search(url):
    keyword = 'Is this lab accepting permanent students? Yes'
    datagram = {}

    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract all text from the webpage
            text = soup.get_text()
            
            # Check for each keyword in the keyword_dict if its associated value exactly matches text on the webpage
            if keyword in text:
                

                
                # For extracting text from an h1 element within a div under the element with id="profile-block-1"
                profile_header = soup.select_one('#profile-block-1 > div:nth-of-type(2) > h1')
                if profile_header:
                    datagram['header'] = profile_header.text
                    print("Profile Header:", profile_header.text)
                else:
                    print("Profile Header not found.")
                # For extracting text from the second paragraph within the element with id="profile-block-1"
                profile_paragraph = soup.select_one('#profile-block-1 > p:nth-of-type(1)')
                if profile_paragraph:
                    datagram['paragraph_1'] = profile_paragraph.text
                    print("Profile Paragraph:", profile_paragraph.text)
                else:
                    print("Profile Paragraph not found.")
                # For extracting text from the second paragraph within the element with id="profile-block-1"
                profile_paragraph = soup.select_one('#profile-block-1 > p:nth-of-type(2)')
                if profile_paragraph:
                    datagram['paragraph_2'] = profile_paragraph.text
                    print("Profile Paragraph:", profile_paragraph.text)
                else:
                    print("Profile Paragraph not found.")
                # Extract the lab website URL
                lab_website_url = soup.find('a', class_='button', href=True)               
                if lab_website_url:
                    # Update the datagram with the keyword and the lab website link
                    datagram['link'] = lab_website_url['href']
            else:
                # This else part is associated with the for loop and executes when the loop completes without hitting a break statement
                print("No matching keywords found.")
        else:
            print(f"Failed to retrieve webpage. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    # Optionally, return the datagram if you need to use it outside this function
    return datagram

# Example call (replace 'your_url_here' with the actual URL you want to scrape)
# Ensure you define 'url' or pass it directly as an argument here
# datagram = scrape_and_search('your_url_here')
# print(datagram)
