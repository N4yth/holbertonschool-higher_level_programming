#!/usr/bin/env python3
import csv
import requests
import json

base_url = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    req = requests.get(base_url)
    print("Status Code: {}".format(req.status_code))
    if req.status_code == 200:
        text = req.json()
        for element in text:
            print(element["title"])


def fetch_and_save_posts():
    listed_data = []
    req = requests.get(base_url)
    if req.status_code == 200:
        data = req.json()
        for element in data:
            listed_data.append({
                "id": element["id"],
                "title": element["title"],
                "body": element["body"]
            })
        with open("posts.csv", "w", encoding="utf-8") as file:
            json.dump(listed_data, file)
