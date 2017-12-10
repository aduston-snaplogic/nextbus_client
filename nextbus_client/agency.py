"""
agency.py - Class models an Agency from the NextBus API

Author: Adam Duston
License: BSD-3-Clause
"""

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
