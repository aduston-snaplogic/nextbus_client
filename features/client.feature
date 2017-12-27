@client
Feature: The NexbusClient class can perform API calls and parse the XML data correctly

  @agencyList
  Scenario: Making a call to the agencyList API command
    given a valid sample for the XML returned by command=agencyList
    when we make an API call to agencyList with requests
    then it should return a valid list of Agency objects
    then agency contents should not be empty
    then the returned agency list should match the sample data

  @routeList
  Scenario: Making a call to routeList endpoint for the 'sf-muni' agency
    given a valid sample for the XML returned by command=routeList&a=sf-muni
    when we make an API call to routeList with requests
    then it should return a valid list of Route objects
    then route contents should not be empty
    then the returned route list should match the sample data

  @routeConfig
  Scenario: Making a call to the routeConfig command for route N of the agency sf-muni
    given a valid sample for the XML returned by command=routeConfig&a=sf-muni&r=N
    when we make an API call to routeConfig with requests
    then it should return a valid RouteConfig object
    then the RouteConfig contents should not be empty
    then the returned RouteConfig should match the sample data

  @predictions
  Scenario: Making a call to the predictions command for stop 5205 of Route N of agency sf-muni
    given a valid sample for the XML returned by command=predictions&a=sf-muni&r=N&s=5205
    when we make an API call to predictions with requests
    then it should return a valid Predictions object
    then Predictions attributes should not be empty
    then the returned Predictions should match the sample data

  @predictionsForMultiStops
  Scenario: Making a call to the predictions command for stops 6997 and 3909 of Route N of agency sf-muni
    given a valid sample for the XML returned by command=predictionsForMultiStops&a=sf-muni&stops=F|6997&stops=F|3909
    when we make an API call to predictionsForMultiStops with requests
    then it should return a valid list of Predictions objects
    then Multi Stop Predictions attributes should not be empty
    then the returned Predictions list should match the sample data