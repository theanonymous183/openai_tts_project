

import requests
from bs4 import BeautifulSoup
from difflib import SequenceMatcher

def fetch_web_content(url):
    response = requests.get(url)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    return soup.get_text()

def check_plagiarism(text1, text2, threshold=0.8):
    similarity_ratio = SequenceMatcher(None, text1, text2).ratio()
    if similarity_ratio >= threshold:
        return True
    return False

# Example usage
project_text = "Your project text here"

# Fetch web content for comparison
web_url = "https://example.com"
web_content = fetch_web_content(web_url)

# Check for plagiarism
is_plagiarized = check_plagiarism(project_text, web_content)

if is_plagiarized:
    print("Plagiarism detected!")
else:
    print("No plagiarism detected.")
