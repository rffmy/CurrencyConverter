import requests

from_ccy = input().lower()

xrate_cache = {}

r = requests.get(f"http://www.floatrates.com/daily/{from_ccy}.json").json()

if from_ccy != 'usd':
    xrate_cache['usd'] = float(f"{r['usd']['rate']}")
if from_ccy != 'eur':
    xrate_cache['eur'] = float(f"{r['eur']['rate']}")

while True:

    to_ccy = input().lower()

    if to_ccy == "":
        break
    else:
        from_amt = float(input())
        to_amt = None

        print("Checking the cache...")

        if not to_ccy in xrate_cache:
            print("Sorry, but it is not in the cache!")
            r = requests.get(f"http://www.floatrates.com/daily/{from_ccy}.json").json()
            xrate_cache[to_ccy] = float(f"{r[to_ccy]['rate']}")
        else:
            print("Oh! It is in the cache!")

        to_amt = from_amt * xrate_cache[to_ccy]

        print(f"You received {to_amt.__round__(2)} {to_ccy.upper()}")
