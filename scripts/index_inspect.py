from urllib.parse import urlparse

import json
import argparse
import requests

class InspectIndex():
    """ Stub """

    def __init__(self):
        """ Stub """
        self.value = None

    def get_nested_attr(self, container, attr):
        # Function to traverse dictionaries and print when value is 
        # not a dict (instead it's a str)

        if isinstance(attr, str):
            keys = attr.split('.')
        else:
            keys = attr

        for key in keys:
            value = container[key]
            if isinstance(value, dict):
                keys.pop(0)
                if keys:
                    self.get_nested_attr(value, keys)
            elif value is not None:
                #TODO: Verify what is happening to value.
                self.value = value
#                return self.value
            else:
                return('Not Encountered Value')

    
    def get_index_metric(self, url, index, metric):
        """
        Return specific metric for the especified index.
        """
        address = url.scheme + '://' + url.netloc + '/%s/_stats' % index
        result = requests.get(address)
        
        assert result.status_code == 200

        state = result.json()
        
        self.get_nested_attr(state, metric)
        print(self.value)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=urlparse, required=True)
    parser.add_argument('--index', type=str, required=True)
    parser.add_argument('--metric', type=str, required=True)
    
    args = parser.parse_args()
    
    index = InspectIndex()
    index.get_index_metric(args.url, args.index, args.metric)

