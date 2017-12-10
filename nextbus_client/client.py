"""
client.py - Python module for making calls to the NextBus API

Author: Adam Duston
License: BSD-3-Clause
"""
from xml.etree import ElementTree as et
from requests import get
from requests.compat import urljoin


class Client(object):
    
    DEFAULT_URL = 'http://webservices.nextbus.com/service/publicXMLFeed'
    DEFAULT_HEADERS = {'Accept-Encoding' : 'gzip, deflate'}
    
    def __init__(self, api_url=DEFAULT_URL, headers=DEFAULT_HEADERS):
        self._api_url = api_url
        self._headers = headers
        
    def _api_call(self, command):
        """
        Make a call to the API and parse the XML values to a dictionary
        
        :param command: String containing the api command to call
        :return: Returned elements as an ElementTree
        """
        
        request_url = urljoin(self._api_url, "?command={}".format(command))
        response = get(request_url)
        
        return et.fromstring(response.content).getchildren()
        
    def agency_list(self):
        """
        Returns the list of agencies
        :return: A list of Agency objects parsed from the returned XML.
        """
        agency_list = self._api_call('agencyList')
        agencies = list()
        for agency in agency_list:
            agencies.append(Agency(agency))
            
        return agencies
        

class Agency(object):
    def __init__(self, **kwargs):
        self.tag = kwargs.get('tag')
        self.title = kwargs.get('title')
        self.region_title = kwargs.get('regionTitle')
        self.short_title = kwargs.get('shortTitle')
        
    def __init__(self, element):
        """
        Parse values form XML element.
        :param element: xml.etree.ElementTree.Element for the Agency
        """
        self.tag = element.get('tag')
        self.title = element.get('title')
        self.region_title = element.get('regionTitle')
        self.short_title = element.get('shortTitle')
        
        
    def _dict__(self):
        """
        Parse the Agency to a dictionary.
        
        :return: Dictionary of Agency attributes
        """
        return {'tag': self.tag,
                'title': self.title,
                'regionTitle': self.region_title,
                'shortTitle': self.short_title}
