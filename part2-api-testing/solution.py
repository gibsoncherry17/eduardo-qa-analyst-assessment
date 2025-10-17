#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 15:59:04 2025

@author: chedm
"""

import requests
import json

class TestJSONPlaceholderAPI:
    base_url = "https://jsonplaceholder.typicode.com/"  # Base URL of the JSONPlaceholder API
    
    def test_fetch_user_successfully(self):       
        url = f"{self.base_url}/users/1"                # Construct the full URL for user with ID = 1
        response = requests.get(url)                    # Send a GET request to the URL and store the response
        print(f"GET {url}")                             # Print the URL being requested 
        print(f"Status Code: {response.status_code}")   # Print the HTTP status code    
        print(f"Response: {response.json()}")           # Print the response body parsed as a JSON dictionary
        
    def test_create_new_post(self, title, body, userId):
        url = f"{self.base_url}/posts"                     
        data = {                                        # Define the data payload for the POST request (title, body, userId)
                "title": title,
                "body": body,
                "userId": userId
                }
        headers = {"Content-Type" : "application/json"} 
        response = requests.post(url, headers=headers,  # Convert the data into a JSON-formatted string before sending
                                 data=json.dumps(data))
        print(f"POST {url}")                            # Print the POST URL being called
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")          
        
    def test_handle_nonexistent_user(self):
        url = f"{self.base_url}/users/999"              # Use an invalid/nonexistent user ID (999)
        response = requests.get(url)                    # Send a GET request to fetch the nonexistent user
        print(f"GET {url}")                             # Print the requested URL
        print(f"Status Code: {response.status_code}") 
        print(f"Response: {response.json()}")           
        
#This is where to run tests for each of the test functions
if __name__ == "__main__":
    testInstance = TestJSONPlaceholderAPI()
    testInstance.test_fetch_user_successfully()
    testInstance.test_create_new_post("gone with the wind", "bartender", 81)
    testInstance.test_handle_nonexistent_user()
    

