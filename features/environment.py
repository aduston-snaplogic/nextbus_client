"""
environment.py - Set up the environment for the behave tests.
"""
import nextbus_client
    
    
def before_all(context):
    # Configure the client
    context.client = nextbus_client.Client()
    context.base_url = context.client.api_url
    context.headers = context.client.headers
