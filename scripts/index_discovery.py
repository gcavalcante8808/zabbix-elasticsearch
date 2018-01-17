from urllib.parse import urlparse

import json
import argparse
import requests


def discover_es_index(url):
    """
    Return all ES indexes.
    """
    address = url.scheme + '://' + url.netloc + '/_cat/indices?format=json'
    result = requests.get(address)
    
    assert result.status_code == 200

    state = result.json()
    
    result = [{"{#ES_INDEX}":item["index"], "{#ES_UUID}": item["uuid"]} for item in state ]
    print(json.dumps({'data':result}))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=urlparse, required=True)
    
    args = parser.parse_args()
    
    discover_es_index(url=args.url)
