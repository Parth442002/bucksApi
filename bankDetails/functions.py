import requests


def getIfsc(ifsc):
    url = "https://ifsc.razorpay.com"
    try:
        r = requests.get(f'{url}/{ifsc}')
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    return r.json()
