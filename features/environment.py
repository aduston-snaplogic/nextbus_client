"""
environment.py - Set up the environment for the behave tests.
"""
import nextbus_client
import pickle


def before_all(context):
    # Configure the client
    context.client = nextbus_client.Client()
    context.base_url = context.client.api_url
    context.headers = context.client.headers
    

def before_feature(context, feature):
    if 'client' in feature.tags:
        context.mocks_directory = './features/mocks/client'
        
        
def before_tag(context, tag):
    if tag == 'agencyList':
        pickle_file = "{0}/{1}".format(context.mocks_directory, 'agency_list.p')
        context.agency_list_sample = pickle.load(open(pickle_file, 'rb'))

    if tag == 'routeList':
        pickle_file = "{0}/{1}".format(context.mocks_directory, 'route_list_sf-muni.p')
        context.route_list_sample = pickle.load(open(pickle_file, 'rb'))
    
    if tag == 'routeConfig':
        pickle_file = "{0}/{1}".format(context.mocks_directory, 'route_config_sf-muni_N.p')
        context.route_config_sample = pickle.load(open(pickle_file, 'rb'))
    
    if tag == 'predictions':
        pickle_file = "{0}/{1}".format(context.mocks_directory, 'predictions_sf-muni_N_5205.p')
        context.predictions_sample = pickle.load(open(pickle_file, 'rb'))
    
    if tag == 'predictionsForMultiStops':
        pickle_file = "{0}/{1}".format(context.mocks_directory, 'multi_stop_predictions_sf-muni_N_6997_3909.p')
        context.multi_stop_predictions_sample = pickle.load(open(pickle_file, 'rb'))
