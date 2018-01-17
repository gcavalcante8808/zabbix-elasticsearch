from urllib.parse import urlparse

import json
import argparse
import requests
import sys

def check_es_health(url, metric):
    """
    Try to get and return the specified metric
    """
    address = url.scheme + '://' + url.netloc + '/_cluster/health'
    result = requests.get(address)
    
    assert result.status_code == 200

    state = result.json()    
    
    if metric in state.keys():
        print(result.json()[metric])
        sys.exit(0)

    raise ValueError('The Key %s provided not exists on the response' %metric)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=urlparse, required=True)
    parser.add_argument('--metric', type=str, required=True)
    
    args = parser.parse_args()
    
    check_es_health(url=args.url, metric=args.metric)
