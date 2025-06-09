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
    req = requests.get(base_url)
    print("Status Code: {}".format(req.status_code))
    if req.status_code == 200:
        with open("posts.csv", "w", encoding="utf-8") as file:
            json.dump(req.json(), file)
