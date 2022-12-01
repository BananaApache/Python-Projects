
import requests
import json
import sys
import os
from colorama import Fore as F

try:
    print("\n" + F.WHITE)

    baseurl = "https://rickandmortyapi.com/api/"
    endpoint = "character"

    def main_request(baseurl, endpoint, page):
        response = requests.get(baseurl + endpoint + f'?page={page}')
        return response.json()

    # print(json.dumps(___, indent=4))

    def list_characters(response):
        char_lst = []
        for item in response['results']:
            if item['type'] == "":
                char_lst.append(item['name'], "is a normal human.")
            else:
                char_lst.append(item['name'], "is a", str(item['type']) + ".")

        return char_lst

    def episode_appearance(response):
        ep_lst = []
        for item in response['results']:
            ep_lst.append(str(item['name']) + " appeared in " + str(len(
                item['episode'])) + "episodes.")

        return ep_lst

    def get_pages():
        return main_request(baseurl, endpoint, 1)['info']['pages']

    output_lst = []
    data = main_request(baseurl, endpoint, 1)
    for x in range(1, int(get_pages()) + 1):
       output_lst.extend(episode_appearance(main_request(baseurl, endpoint, x)))

    print(output_lst)
    
    # list_characters()
    # episode_appearance()

except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(F.LIGHTRED_EX, e, "\n", exc_type, fname,
          "\n", "Line:", exc_tb.tb_lineno, F.RESET)

print("\n" + F.RESET)
