"""
errors.py - Define custom errors for the client.

Author: Adam Duston
License: BSD-3-Clause
"""
import re

# In the event of an error the nextbus api may return a 200 OK with some error message in the XML attributes.
# Define some regular expressions for parsing the error messages to determine which error was sent back.
BAD_AGENCY_REGEXP = re.compile(r"\\n\s+Agency\sparameter\s+\"a=(.+)\"\sis\snot\svalid.\\n")

BAD_ROUTE_FOR_AGENCY_REGEXP = re.compile(r"\n\s+Could not get route \"(.+)\" for agency tag "
                                         r"\"(.+)\".\s+\\nOne of the tags could be bad.\\n")

BAD_STOP_FOR_ROUTE_REGEXP = re.compile(r"\\n\s+For\sagency=(.+)\sstop\ss=(.+)\sis\son\snone\sof\sthe\sdirections\sfor\s"
                                       r"r=(.+)\sso\scannot\sdetermine\swhich\sstop\sto\sprovide\sdata\sfor.\\n")


BAD_STOP_ID_INTEGER_REGEXP = re.compile(r"\\n\s+stopId \"(.+)\" is not a valid stop id integer\\n")
BAD_STOP_ID_FOR_AGENCY = re.compile(r"\\n\s+stopId=(.+)\s+is not valid for agency=(.+)\\n")
MISSING_QUERY_PARAMETER = re.compile(r"\\n\s+(.+)\sparameter\s\"(.+)\"\smust\sbe\specified\sin\squery\sstring\\n")


def parse_error_xml(error_xml):
    """
    The NextBus API will often return 200 OK with the error details in the body. Parse these and raise the
    appropriate exceptions.

    :param error_xml: The XML ElementTree for the Error.
    """

    # Check if a query parameter was missing.
    match = MISSING_QUERY_PARAMETER.match(error_xml.text)
    if match:
        raise MissingQueryParameterError()
    # Check if the error is an invalid agency tag
    match = BAD_AGENCY_REGEXP.match(error_xml.text)
    if match:
        raise InvalidAgencyError(agency=match.group(1))

    # Check if the error is a bad route for the given agency
    match = BAD_ROUTE_FOR_AGENCY_REGEXP.match(error_xml.text)
    if match:
        raise InvalidRouteForAgencyError(route=match.group(1), agency=match.group(2))

    # Check if the error is a bad stop ID for the given route
    match = BAD_STOP_FOR_ROUTE_REGEXP.match(error_xml.text)
    if match:
        raise InvalidStopForRouteError(agency=match.group(1), stop=match.group(2), route=match.group(3))

    # Check if the error is a bad stop (non-integer) stop ID
    match = BAD_STOP_ID_INTEGER_REGEXP.match(error_xml.text)
    if match:
        raise InvalidStopIdError(stop_id=match.group(1))

    # Check if the error is a bad stop for a given agency.
    print(error_xml.text)
    match = BAD_STOP_ID_FOR_AGENCY.match(error_xml.text)
    print(match)
    if match:
        raise InvalidStopIdForAgencyError(stop_id=match.group(1), agency=match.group(2))


class MissingQueryParameterError(Exception):
    """
    Exception raised when a request is missing a query parameter.

    Attributes:
          name -- Name of the query parameter
          parameter -- The missing query parameter
          message -- explanation of the error
    """

    def __init__(self, name='', parameter='', message=None):
        """
        Construct a custom Exception for MissingQueryParameterError

        :param name: Name of the query parameter
        :param parameter: The missing query parameter
        :param message: Message for the error
        """
        message = message or "{0} parameter \"{1}\" must be specified in query string".format(name, parameter)
        super().__init__(message)
        self.name = name
        self.parameter = parameter


class InvalidAgencyError(Exception):
    """
    Exception raised when the requested agency does not exist.

    Attributes:
          agency -- Tag for the requested agency.
          message -- explanation of the error.
    """

    def __init__(self, agency, message=None):
        """
        Construct the InvalidAgencyError

        :param agency: Agency tag as a string
        :param message: Message for the error.
        """
        message = message or "Agency parameter \"a={0}\" is not valid".format(agency)
        super().__init__(message)
        self.agency = agency


class InvalidRouteForAgencyError(Exception):
    """
    Exception raised when the requested route does not exist for a given agency.

    Attributes:
          agency -- Tag for the requested agency.
          route -- Tag for the requested route.
          message -- explanation of the error.
    """

    def __init__(self, agency, route, message=None):
        """
        Construct the InvalidRouteForAgencyError

        :param agency: Agency tag as a string
        :param message: Message for the error.
        """
        message = message or "Could not get route \"{0}\" for agency tag \"{1}\"".format(agency, route)
        super().__init__(message)
        self.agency = agency
        self.route = route


class InvalidStopForRouteError(Exception):
    """
    Exception raised when the requested stop does not exist for a given route.

    Attributes:
          agency -- Tag for the requested agency.
          route -- Tag for the requested route.
          stop -- ID of the requested stop.
          message -- explanation of the error.
    """

    def __init__(self, agency, route, stop, message=None):
        """
        Construct the InvalidStopForRouteError

        :param agency: Agency tag as a string
        :param message: Message for the error.
        """
        message_text = "For agency={0} stop s={1} is on none of the directions for r={2} so cannot determine which " \
            "stop to provide data for.".format(agency, stop, route)
        message = message or message_text
        super().__init__(message)
        self.agency = agency
        self.route = route
        self.stop = stop


class InvalidStopIdError(Exception):
    """
    Exception raised when the requested stop id is not valid.

    Attributes:
          stop -- ID of the requested stop.
          message -- explanation of the error.
    """

    def __init__(self, stop_id, message=None):
        """
        Construct an InvalidStopIdError

        :param stop_id: stopId tag as a string
        :param message: Message for the error.
        """
        message = message or "stopId \"{0}\" is not a valid stop id integer".format(stop_id)
        super().__init__(message)
        self.stop_id = stop_id


class InvalidStopIdForAgencyError(Exception):
    """
    Exception raised when the requested stop does not exist for a given agency.

    Attributes:
          agency -- Tag for the requested agency.
          stop -- ID of the requested stop.
          message -- explanation of the error.
    """

    def __init__(self, stop_id='', agency='', message=None):
        """
        Construct the InvalidStopIdForAgencyError

        :param stop_id: stopId tag as a string
        :param agency: agency tag as a string
        :param message: Message for the error.
        """
        message = message or "stopId={0} is not valid for agency={1}".format(stop_id, agency)
        super().__init__(message)
        self.stop_id = stop_id
