from urllib.parse import urlparse

import json
import argparse
import requests
import sys


class InspectIndex():
    """ Stub """

    def __init__(self):
        """ Stub """
        self.value = None

    def get_index_metric(self, url, index, metric):
        """
        Return specific metric for the especified index.
        """
        address = url.scheme + '://' + url.netloc + '/_cat/indices/%s?format=json' % index
        result = requests.get(address)
        
        assert result.status_code == 200

        state = result.json()[0]
        
        if metric in state.keys():
            print(state[metric])
            sys.exit(0)

        raise ValueError('The Key %s provided not exists on the response' %metric)        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=urlparse, required=True)
    parser.add_argument('--index', type=str, required=True)
    parser.add_argument('--metric', type=str, required=True)
    
    args = parser.parse_args()
    
    index = InspectIndex()
    index.get_index_metric(args.url, args.index, args.metric)

