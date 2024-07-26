import requests
import json
import webbrowser
import time

# Load cookies from a JSON file
with open('cookie.json', 'r') as file:
    cookies_json = json.load(file)

# Convert the JSON cookies to a dictionary
cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies_json}

# Specify the URL
url = "https://omkarcloud-googlemapssc-buc9a6k9pi0.ws-eu115.gitpod.io/"

# Send a request to the URL with the loaded cookies
response = requests.get(url, cookies=cookies_dict)

# Print the response status code and content
print(f"Status Code: {response.status_code}")
print(f"Response Content: {response.content.decode('utf-8')}")

# Wait for 5 seconds to allow for initial page load
print("Waiting for 5 seconds before opening the browser...")
time.sleep(5)

# Open the URL in the default web browser
print(f"Opening {url} in your default web browser...")
webbrowser.open(url)

print("Script completed. The browser should now be opening the URL.")