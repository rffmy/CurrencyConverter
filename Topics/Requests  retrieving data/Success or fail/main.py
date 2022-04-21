import requests


def check_success(url):
    r = requests.get(url)
    if r:
        return "Success"
    # Found useless returning else statement
    # else:
        # return "Fail"
    return "Fail"

    # Better:
    # return "Success" if requests.get(url) else "Fail"
