import requests

def do_search(bookstore_url, params):
    # pass
    return requests.get(bookstore_url, params=params)

