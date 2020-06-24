"""Boilerplate Integration for Cortex XSOAR - Unit Tests file

"""

import json
import io


def util_load_json(path):
    with io.open(path, mode='r', encoding='utf-8') as f:
        return json.loads(f.read())

def test_get_alert(requests_mock):
    """Tests get-alert command function.
    Configures requests_mock instance to generate the appropriate
    get_alerts API response, loaded from a local JSON file. Checks
    the output of the command function with the expected output.
    """
    from Boilerplate import Client, get_alert_command
    mock_response = util_load_json('test_data/get_alert.json')
    requests_mock.get('https://test.com/api/v1/get_alert_details?alert_id=695b3238-05d6-4934-86f5-9fff3201aeb0',
                      json=mock_response)
    client = Client(
        base_url='https://test.com/api/v1',
        verify=False,
        headers={
            'Authentication': 'Bearer some_api_key'
        }
    )
    args = {
        'alert_id': '695b3238-05d6-4934-86f5-9fff3201aeb0',
    }
    response = get_alert_command(client, args)
    # We modify the timestamp from the raw mock_response of the API, because the
    # integration changes the format from timestamp to ISO8601.
    mock_response['created'] = '2020-04-17T14:43:59.000Z'
    assert response.outputs == mock_response
    assert response.outputs_prefix == 'Boilerplate.Alert'
    assert response.outputs_key_field == 'alert_id'

