#!/usr/bin/env python3

import sys
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List

import requests
from bs4 import BeautifulSoup


HELIX_REFERENCE_URL = 'https://dev.twitch.tv/docs/api/reference'

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

@dataclass_json
@dataclass
class APIEndpoint:
    category: str
    name: str
    description: str

def main():
    data = requests.get(HELIX_REFERENCE_URL).text

    soup = BeautifulSoup(data, features="html.parser")

    api_reference = soup.find('h1', id='twitch-api-reference')

    if not api_reference:
        eprint("Couldn't find API reference h1 tag")
        return

    api_reference_table = api_reference.find_next_sibling('table')
    if not api_reference_table:
        eprint("Could not find API reference table")
        return

    api_endpoints: List[APIEndpoint] = []

    for api_reference_row in api_reference_table.find_all("tr"):
        api_reference_data = api_reference_row.find_all("td")
        if len(api_reference_data) != 3:
            continue

        category = api_reference_data[0].text
        name = api_reference_data[1].text
        description = api_reference_data[2].text.strip()
        api_endpoints.append(APIEndpoint(category, name, description))

    print(APIEndpoint.schema().dumps(api_endpoints, many=True))

if __name__ == "__main__":
    main()
