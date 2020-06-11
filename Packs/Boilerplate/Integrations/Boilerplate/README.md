This is a Boilerplate integration for getting started.
This integration was integrated and tested with version xx of Boilerplate
## Configure Boilerplate on Cortex XSOAR

1. Navigate to **Settings** > **Integrations** > **Servers & Services**.
2. Search for Boilerplate.
3. Click **Add instance** to create and configure a new integration instance.

| **Parameter** | **Description** | **Required** |
| --- | --- | --- |
| url | Your server URL | True |
| apikey | API Key | True |
| insecure | Trust any certificate \(not secure\) | False |
| proxy | Use system proxy settings | False |

4. Click **Test** to validate the URLs, token, and connection.
## Commands
You can execute these commands from the Demisto CLI, as part of an automation, or in a playbook.
After you successfully execute a command, a DBot message appears in the War Room with the command details.
### boilerplate-get-alert
***
Retrieve alert by ID


#### Base Command

`boilerplate-get-alert`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| alert_id | Alert ID to retrieve. | Required | 


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Boilerplate.Alert.alert_id | String | Alert ID. | 
| Boilerplate.Alert.created | Date | Boilerplate created time. Format is ISO8601 \(i.e. '2020\-04\-30T10:35:00.000Z'\). | 
| Boilerplate.Alert.description | String | Alert description. | 
| Boilerplate.Alert.device_id | String | ID of the device involved in the alert. | 
| Boilerplate.Alert.device_ip | String | IP Address of the device involved in the alert. | 
| Boilerplate.Alert.location | String | Location of the device involved in the alert. | 
| Boilerplate.Alert.user | String | User involved in the alert. | 


#### Command Example
``` ```

#### Human Readable Output


