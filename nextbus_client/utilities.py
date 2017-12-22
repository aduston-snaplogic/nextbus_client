"""
agency.py - Class models an Agency from the NextBus API

Author: Adam Duston
License: BSD-3-Clause
"""
from xml.etree.ElementTree import Element


def validate_xml_element(element, tag):
    """
    Make sure that the given XML element is the right type of object with the correct tag.

    Just raises exceptions if the element is the incorrect type or has the wrong tag.

    :param element: The XML element
    :param tag: The expected value for the tag attribute
    """

    if isinstance(element, Element):
        if element.tag != tag:
            raise ValueError("xml_element must be an xml.etree.ElementTree.Element with tag '{0}'".format(tag))
    else:
        raise TypeError("xml_element must be of type xml.etree.ElementTree.Element Got {0}.".format(type(element)))
