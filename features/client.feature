Feature: The NexbusClient class can perform API calls and parse the data correctly.

  Scenario: Test the agencyList API command
    given a valid sample for the XML returned by command=agencyList
    when we make an API call to agencyList with requests
    then it should return a valid list of Agency objects
    then agency contents should not be empty
    then the returned agency list should match the sample data

  Scenario: Test the routeList API command
    given a valid sample for the XML returned by command=routeList&a=sf-muni
    when we make an API call to routeList with requests
    then it should return a valid list of Route objects
    then route contents should not be empty
    then the returned route list should match the sample data

  Scenario: Test the routeConfig API command
    given a valid sample for the XML returned by command=routeConfig&a=sf-muni&r=N
    when we make an API call to routeConfig with requests
    then it should return a valid RouteConfig object
    then the RouteConfig contents should not be empty
    then the returned RouteConfig should match the sample data