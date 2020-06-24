"""Boilerplate Integration for Cortex XSOAR (aka Demisto)

"""

import demistomock as demisto
from CommonServerPython import *
from CommonServerUserPython import *

import requests
import traceback
from typing import Any, Dict

# Disable insecure warnings
requests.packages.urllib3.disable_warnings()


''' CONSTANTS '''


DATE_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
HELLOWORLD_SEVERITIES = ['Low', 'Medium', 'High', 'Critical']

''' CLIENT CLASS '''


class Client(BaseClient):
    """Client class to interact with the service API

    This Client implements API calls, and does not contain any Demisto logic.
    Should only do requests and return data.
    It inherits from BaseClient defined in CommonServer Python.
    Most calls use _http_request() that handles proxy, SSL verification, etc.
    For this  implementation, no special attributes defined
    """

    def get_alert(self, alert_id: str) -> Dict[str, Any]:

        return self._http_request(
            method='GET',
            url_suffix=f'/get_alert_details',
            params={
                'alert_id': alert_id
            }
        )


''' HELPER FUNCTIONS '''

# No helper functions yet


''' COMMAND FUNCTIONS '''


def test_module(client: Client) -> str:
    """Tests API connectivity and authentication'

    Returning 'ok' indicates that the integration works like it is supposed to.
    Connection to the service is successful.
    Raises exceptions if something goes wrong.

    :type client: ``Client``
    :param Client: client to use

    :return: 'ok' if test passed, anything else will fail the test.
    :rtype: ``str``
    """

    try:
        client.get_alert(alert_id='something')
    except DemistoException as e:
        if 'Forbidden' in str(e):
            return 'Authorization Error: make sure API Key is correctly set'
        else:
            raise e
    return 'ok'

def get_alert_command(client: Client, args: Dict[str, Any]) -> CommandResults:

    alert_id = args.get('alert_id', None)
    if not alert_id:
        raise ValueError('alert_id not specified')

    alert = client.get_alert(alert_id)

    # convert the date to ISO
    if 'created' in alert:
        created_time_ms = int(alert.get('created', '0')) * 1000
        alert['created'] = timestamp_to_datestring(created_time_ms)

    return CommandResults(
        outputs_prefix='Boilerplate.Alert',
        outputs_key_field='alert_id',
        outputs=alert
    )

''' MAIN FUNCTION '''


def main() -> None:
    """main function, parses params and runs command functions

    :return:
    :rtype:
    """

    api_key = demisto.params().get('apikey')

    # get the service API url
    base_url = urljoin(demisto.params()['url'], '/api/v1')

    # if your Client class inherits from BaseClient, SSL verification is
    # handled out of the box by it, just pass ``verify_certificate`` to
    # the Client constructor
    verify_certificate = not demisto.params().get('insecure', False)

    # if your Client class inherits from BaseClient, system proxy is handled
    # out of the box by it, just pass ``proxy`` to the Client constructor
    proxy = demisto.params().get('proxy', False)

    demisto.debug(f'Command being called is {demisto.command()}')
    try:
        headers = {
            'Authorization': f'Bearer {api_key}'
        }
        client = Client(
            base_url=base_url,
            verify=verify_certificate,
            headers=headers,
            proxy=proxy)

        if demisto.command() == 'test-module':
            # This is the call made when pressing the integration Test button.
            result = test_module(client)
            return_results(result)
        
        elif demisto.command() == 'boilerplate-get-alert':
            return_results(get_alert_command(client, demisto.args()))

    # Log exceptions and return errors
    except Exception as e:
        demisto.error(traceback.format_exc())  # print the traceback
        return_error(f'Failed to execute {demisto.command()} command.\nError:\n{str(e)}')


''' ENTRY POINT '''


if __name__ in ('__main__', '__builtin__', 'builtins'):
    main()
