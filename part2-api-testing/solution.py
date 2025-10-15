#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 15:59:04 2025

@author: chedm
"""

import requests
import json

class TestJSONPlaceholderAPI:
    base_url = "https://jsonplaceholder.typicode.com/"
    
    def test_fetch_user_successfully(self):
        url = f"{self.base_url}/users/1"
        response = requests.get(url)
        print(f"GET {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
    def test_create_new_post(self, title, body, userId):
        url = f"{self.base_url}/posts"
        data = {
                "title": title,
                "body": body,
                "userId": userId
                }
        headers = {"Content-Type" : "application-json"}
        response = requests.post(url, headers=headers, data=json.dumps(data))
        print(f"POST {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
    def test_handle_nonexistent_user(self):
        url = f"{self.base_url}/users/999"
        response = requests.get(url)
        print(f"GET {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        

if __name__ == "__main__":
    testInstance = TestJSONPlaceholderAPI()
    testInstance.test_fetch_user_successfully()
    testInstance.test_create_new_post("gone", "bar", 8)
    testInstance.test_handle_nonexistent_user()
    

