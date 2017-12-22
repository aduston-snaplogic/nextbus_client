"""
step_client.py - Behave test steps for the client module

Author: Adam Duston
License: BSD-3-Clause
"""
from behave import given, when, then
import requests_mock
import nextbus_client
import pickle

# Steps for the agency_list method


@given('a valid sample for the XML returned by command=agencyList')
def step_get_agency_list_xml_data(context):
    with open('./features/mocks/agency_list.xml', 'rb') as xml_file:
        context.agencyListXML = xml_file.read()


@when('we make an API call to agencyList with requests')
def step_mock_agency_list_request(context):
    context.m = requests_mock.mock()
    context.m.get("{0}/?command=agencyList".format(context.base_url),
                  headers=context.headers,
                  content=context.agencyListXML)
    

@then('it should return a valid list of Agency objects')
def step_get_agency_list(context):
    context.agency_list = context.client.agency_list()
    assert type(context.agency_list) == list
    assert all(type(a) == nextbus_client.Agency for a in context.agency_list)


@then('agency contents should not be empty')
def step_agencies_have_data(context):
    assert all(a.tag != '' for a in context.agency_list)
    assert all(a.title != '' for a in context.agency_list)
    assert all(a.region_title != '' for a in context.agency_list)
    
    
@then('the returned agency list should match the sample data')
def step_compare_agency_lists(context):
    agency_list_sample = pickle.load(open('./features/mocks/agency_list.p', 'rb'))
    set_a = set(a.tag for a in agency_list_sample)
    set_b = set(a.tag for a in context.agency_list)
    # Ensure the lists have the same contents.
    assert len(set_a ^ set_b) == 0

# Steps for the route_list method


@given('a valid sample for the XML returned by command=routeList&a=sf-muni')
def step_get_route_list_xml_data(context):
    with open('./features/mocks/route_list_sf-muni.xml', 'rb') as xml_file:
        context.routeListXML = xml_file.read()


@when('we make an API call to routeList with requests')
def step_mock_route_list_request(context):
    context.m = requests_mock.mock()
    context.m.get("{0}/?command=routeList&a=sf-muni".format(context.base_url),
                  headers=context.headers,
                  content=context.routeListXML)


@then('it should return a valid list of Route objects')
def step_get_route_list(context):
    context.route_list = context.client.route_list('sf-muni')
    assert type(context.route_list) == list
    assert all(type(r) == nextbus_client.Route for r in context.route_list)


@then('route contents should not be empty')
def step_routes_have_data(context):
    assert all(r.tag != '' for r in context.route_list)
    assert all(r.title != '' for r in context.route_list)


@then('the returned route list should match the sample data')
def step_compare_route_lists(context):
    route_list_sample = pickle.load(open('./features/mocks/route_list_sf-muni.p', 'rb'))
    set_a = set(r.tag for r in route_list_sample)
    set_b = set(r.tag for r in context.route_list)
    # Ensure the lists have the same contents.
    assert len(set_a ^ set_b) == 0
    
# Steps for the routeConfig command


@given('a valid sample for the XML returned by command=routeConfig&a=sf-muni&r=N')
def step_get_route_config_xml_data(context):
    with open('./features/mocks/route_config_sf-muni_N.xml', 'rb') as xml_file:
        context.routeConfigXML = xml_file.read()


@when('we make an API call to routeConfig with requests')
def step_mock_route_config_request(context):
    context.m = requests_mock.mock()
    context.m.get("{0}/?command=routeConfig&a=sf-muni&r=N".format(context.base_url),
                  headers=context.headers,
                  content=context.routeConfigXML)


@then('it should return a valid RouteConfig object')
def step_get_route_config(context):
    context.route_config = context.client.route_config('sf-muni', 'N')
    assert type(context.route_config) == nextbus_client.route_config.RouteConfig
    

@then('the RouteConfig contents should not be empty')
def step_route_has_data(context):
    assert context.route_config.tag != ''
    assert context.route_config.title != ''
    # Colors should be valid hex values.
    assert int(context.route_config.color, 16)
    assert int(context.route_config.opposite_color, 16)
    # Lat & lon should be values taht convert to float.
    assert float(context.route_config.lat_min)
    assert float(context.route_config.lat_max)
    assert float(context.route_config.lon_min)
    assert float(context.route_config.lon_max)
    # Certain attributes should be lists of non-zero length
    assert type(context.route_config.directions) is list
    assert len(context.route_config.directions) > 0
    assert type(context.route_config.stops) is list
    assert len(context.route_config.stops) > 0
    assert type(context.route_config.paths) is list
    assert len(context.route_config.paths) > 0
   

@then('the returned RouteConfig should match the sample data')
def step_compare_route_configs(context):
    route_config_sample = pickle.load(open('./features/mocks/route_config_sf-muni_N.p', 'rb'))
    # Ensure the lists have the same contents.
    assert route_config_sample.tag == context.route_config.tag
