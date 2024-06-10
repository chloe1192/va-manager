from .airports import Airports
import requests

class Dispatch(Airports):

    def __init__(self):
        pass

    def request_dispatch_to_simbrief(self, flt_plan_data):
        pass

    def request_latest_ofp(self, username):
        url = f"https://www.simbrief.com/api/xml.fetcher.php?username={username}&json=1"
        res = requests.request("POST", url)
        print(res.json())
        return res