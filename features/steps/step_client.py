"""
step_client.py - Behave test steps for the client module
"""
from behave import given, when, then
import requests_mock
import nextbus_client

# Steps for the agency_list method


@given('a valid sample for the XML returned by command=agencyList')
def step_get_agency_list_xml_data(context):
    with open('./features/mocks/client/agency_list.xml', 'rb') as xml_file:
        context.agencyListXML = xml_file.read()


@when('we make an API call to agencyList with requests')
def step_mock_agency_list_request(context):
    with requests_mock.mock() as m:
        m.get("{0}?command=agencyList".format(context.base_url),
              headers=context.headers, content=context.agencyListXML)
        context.agency_list = context.client.agency_list()
        

@then('it should return a valid list of Agency objects')
def step_get_agency_list(context):
    assert type(context.agency_list) == list
    assert all(isinstance(a, nextbus_client.agency.Agency) for a in context.agency_list)


@then('agency contents should not be empty')
def step_agencies_have_data(context):
    assert all(a.tag != '' for a in context.agency_list)
    assert all(a.title != '' for a in context.agency_list)
    assert all(a.region_title != '' for a in context.agency_list)
    
    
@then('the returned agency list should match the sample data')
def step_compare_agency_lists(context):
    set_a = set(a.tag for a in context.agency_list_sample)
    set_b = set(a.tag for a in context.agency_list)
    # Ensure the lists have the same contents.
    assert len(set_a ^ set_b) == 0

# Steps for the route_list method


@given('a valid sample for the XML returned by command=routeList&a=sf-muni')
def step_get_route_list_xml_data(context):
    with open('./features/mocks/client/route_list_sf-muni.xml', 'rb') as xml_file:
        context.routeListXML = xml_file.read()


@when('we make an API call to routeList with requests')
def step_mock_route_list_request(context):
    with requests_mock.mock() as m:
        m.get("{0}?command=routeList&a=sf-muni".format(context.base_url),
              headers=context.headers, content=context.routeListXML)
        context.route_list = context.client.route_list('sf-muni')


@then('it should return a valid list of Route objects')
def step_get_route_list(context):
    assert type(context.route_list) == list
    assert all(isinstance(r, nextbus_client.route.Route) for r in context.route_list)


@then('route contents should not be empty')
def step_routes_have_data(context):
    assert all(r.tag != '' for r in context.route_list)
    assert all(r.title != '' for r in context.route_list)


@then('the returned route list should match the sample data')
def step_compare_route_lists(context):
    set_a = set(r.tag for r in context.route_list_sample)
    set_b = set(r.tag for r in context.route_list)
    # Ensure the lists have the same contents.
    assert len(set_a ^ set_b) == 0
    
# Steps for the routeConfig command


@given('a valid sample for the XML returned by command=routeConfig&a=sf-muni&r=N')
def step_get_route_config_xml_data(context):
    with open('./features/mocks/client/route_config_sf-muni_N.xml', 'rb') as xml_file:
        context.routeConfigXML = xml_file.read()


@when('we make an API call to routeConfig with requests')
def step_mock_route_config_request(context):
    with requests_mock.mock() as m:
        m.get("{0}?command=routeConfig&a=sf-muni&r=N".format(context.base_url),
              headers=context.headers, content=context.routeConfigXML)
        context.route_config = context.client.route_config('sf-muni', 'N')


@then('it should return a valid RouteConfig object')
def step_get_route_config(context):
    context.route_config = context.client.route_config('sf-muni', 'N')
    assert isinstance(context.route_config, nextbus_client.route_config.RouteConfig)
    

@then('the RouteConfig contents should not be empty')
def step_route_has_data(context):
    assert context.route_config.tag != ''
    assert context.route_config.title != ''
    # Colors should be valid hex values.
    assert int(context.route_config.color, 16)
    assert int(context.route_config.opposite_color, 16)
    # Lat & lon should be values that convert to float.
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
    # Ensure the lists have the same contents.
    assert context.route_config_sample.tag == context.route_config.tag
    assert context.route_config_sample.title == context.route_config.title
    assert context.route_config_sample.color == context.route_config.color
    assert context.route_config_sample.opposite_color == context.route_config.opposite_color
    assert context.route_config_sample.lat_max == context.route_config.lat_max
    assert context.route_config_sample.lat_min == context.route_config.lat_min
    assert context.route_config_sample.lon_max == context.route_config.lon_max
    assert context.route_config_sample.lon_min == context.route_config.lon_min
    assert len(context.route_config_sample.directions) == len(context.route_config.directions)
    assert len(context.route_config_sample.stops) == len(context.route_config.stops)
    assert len(context.route_config_sample.paths) == len(context.route_config.paths)


# Steps for the predictions method
@given('a valid sample for the XML returned by command=predictions&a=sf-muni&r=N&s=5205')
def step_get_predictions_xml_data(context):
    with open('./features/mocks/client/predictions_sf-muni_N_5205.xml', 'rb') as xml_file:
        context.predictionsXML = xml_file.read()


@when('we make an API call to predictions with requests')
def step_mock_predictions_request(context):
    with requests_mock.mock() as m:
        m.get("{0}?command=predictions&a=sf-muni&r=N&s=5205".format(context.base_url),
              headers=context.headers, content=context.predictionsXML)
        context.predictions = context.client.predictions(agency_tag='sf-muni', route_tag='N', stop_tag='5205')


@then('it should return a valid Predictions object')
def step_validate_predictions(context):
    assert isinstance(context.predictions, nextbus_client.predictions.Predictions)


@then('Predictions attributes should not be empty')
def step_predictions_have_data(context):
    assert context.predictions.agency_title != ''
    assert context.predictions.route_tag != ''
    assert context.predictions.stop_title != ''
    assert len(context.predictions.directions) > 0
    assert len(context.predictions.messages) > 0


@then('the returned Predictions should match the sample data')
def step_compare_predictions(context):
    assert context.predictions_sample.agency_title == context.predictions.agency_title
    assert context.predictions_sample.route_tag == context.predictions.route_tag
    assert context.predictions_sample.route_code == context.predictions.route_code
    assert context.predictions_sample.stop_title == context.predictions.stop_title
    assert len(context.predictions_sample.directions) == len(context.predictions.directions)
    assert len(context.predictions_sample.messages) == len(context.predictions.messages)


# Steps for the multi_stop_predictions method
@given('a valid sample for the XML returned by command=predictionsForMultiStops&a=sf-muni&stops=F|6997&stops=F|3909')
def step_get_multi_stop_predictions_xml_data(context):
    with open('./features/mocks/client/multi_stop_predictions_sf-muni_N_6997_3909.xml', 'rb') as xml_file:
        context.multiStopPredictionsXML = xml_file.read()


@when('we make an API call to predictionsForMultiStops with requests')
def step_mock_multi_stop_predictions_request(context):
    with requests_mock.mock() as m:
        m.get("{0}?command=predictionsForMultiStops&a=sf-muni&stops=N|6997&stops=N|3909".format(context.base_url),
              headers=context.headers, content=context.multiStopPredictionsXML)
        context.multi_stop_predictions = context.client.multi_stop_predictions('sf-muni', 'N', '6997', '3909')
        
        
@then('it should return a valid list of Predictions objects')
def step_validate_multi_stop_predictions(context):
    assert all(isinstance(p, nextbus_client.predictions.Predictions) for p in context.multi_stop_predictions)
    
    
@then('Multi Stop Predictions attributes should not be empty')
def step_multi_stop_predictions_have_data(context):
    for p in context.multi_stop_predictions:
        assert p.agency_title != ''
        assert p.route_tag != ''
        assert p.stop_title != ''
        assert len(p.directions) > 0
        assert len(p.messages) > 0


@then('the returned Predictions list should match the sample data')
def compare_multi_stop_predictions(context):
    # Sort the two lists so the objects can be compared 
    predictions = sorted(context.multi_stop_predictions,
                         key=lambda x: "{0}{1}{2}".format(x.agency_title, x.route_tag, x.stop_title))
    
    sample_predictions = sorted(context.multi_stop_predictions_sample, 
                                key=lambda x: "{0}{1}{2}".format(x.agency_title, x.route_tag, x.stop_title))
    
    for s, p in zip(sample_predictions, predictions):
        assert s.agency_title == p.agency_title
        assert s.route_tag == p.route_tag
        assert s.route_code == p.route_code
        assert s.stop_title == p.stop_title
        assert len(s.directions) == len(p.directions)
        assert len(s.messages) == len(p.messages)
