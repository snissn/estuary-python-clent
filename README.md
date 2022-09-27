# swagger-client
This is the API for the Estuary application.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen
For more information, please visit [https://docs.estuary.tech/feedback](https://docs.estuary.tech/feedback)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearerAuth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))

try:
    # Get API keys for a user
    api_response = api_instance.user_api_keys_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_api_keys_get: %s\n" % e)

# Configure API key authorization: bearerAuth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
key = 'key_example' # str | Key

try:
    # Revoke a User API Key.
    api_instance.user_api_keys_key_delete(key)
except ApiException as e:
    print("Exception when calling UserApi->user_api_keys_key_delete: %s\n" % e)

# Configure API key authorization: bearerAuth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))

try:
    # Create API keys for a user
    api_response = api_instance.user_api_keys_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_api_keys_post: %s\n" % e)

# Configure API key authorization: bearerAuth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))

try:
    # Export user data
    api_response = api_instance.user_export_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_export_get: %s\n" % e)

# Configure API key authorization: bearerAuth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))

try:
    # Create API keys for a user
    api_response = api_instance.user_stats_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_stats_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *//api.estuary.tech/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*UserApi* | [**user_api_keys_get**](docs/UserApi.md#user_api_keys_get) | **GET** /user/api-keys | Get API keys for a user
*UserApi* | [**user_api_keys_key_delete**](docs/UserApi.md#user_api_keys_key_delete) | **DELETE** /user/api-keys/{key} | Revoke a User API Key.
*UserApi* | [**user_api_keys_post**](docs/UserApi.md#user_api_keys_post) | **POST** /user/api-keys | Create API keys for a user
*UserApi* | [**user_export_get**](docs/UserApi.md#user_export_get) | **GET** /user/export | Export user data
*UserApi* | [**user_stats_get**](docs/UserApi.md#user_stats_get) | **GET** /user/stats | Create API keys for a user
*AdminApi* | [**admin_peering_peers_delete**](docs/AdminApi.md#admin_peering_peers_delete) | **DELETE** /admin/peering/peers | Remove peers on Peering Service
*AdminApi* | [**admin_peering_peers_get**](docs/AdminApi.md#admin_peering_peers_get) | **GET** /admin/peering/peers | List all Peering peers
*AdminApi* | [**admin_peering_peers_post**](docs/AdminApi.md#admin_peering_peers_post) | **POST** /admin/peering/peers | Add peers on Peering Service
*AdminApi* | [**admin_peering_start_post**](docs/AdminApi.md#admin_peering_start_post) | **POST** /admin/peering/start | Start Peering
*AdminApi* | [**admin_peering_status_get**](docs/AdminApi.md#admin_peering_status_get) | **GET** /admin/peering/status | Check Peering Status
*AdminApi* | [**admin_peering_stop_post**](docs/AdminApi.md#admin_peering_stop_post) | **POST** /admin/peering/stop | Stop Peering
*AdminApi* | [**admin_system_config_get**](docs/AdminApi.md#admin_system_config_get) | **GET** /admin/system/config | Get systems(estuary/shuttle) config
*AdminApi* | [**admin_users_get**](docs/AdminApi.md#admin_users_get) | **GET** /admin/users | Get all users
*AutoretrieveApi* | [**admin_autoretrieve_init_post**](docs/AutoretrieveApi.md#admin_autoretrieve_init_post) | **POST** /admin/autoretrieve/init | Register autoretrieve server
*AutoretrieveApi* | [**admin_autoretrieve_list_get**](docs/AutoretrieveApi.md#admin_autoretrieve_list_get) | **GET** /admin/autoretrieve/list | List autoretrieve servers
*AutoretrieveApi* | [**autoretrieve_heartbeat_post**](docs/AutoretrieveApi.md#autoretrieve_heartbeat_post) | **POST** /autoretrieve/heartbeat | Marks autoretrieve server as up
*CollectionsApi* | [**collections_coluuid_commit_post**](docs/CollectionsApi.md#collections_coluuid_commit_post) | **POST** /collections/{coluuid}/commit | Produce a CID of the collection contents
*CollectionsApi* | [**collections_coluuid_delete**](docs/CollectionsApi.md#collections_coluuid_delete) | **DELETE** /collections/{coluuid} | Deletes a collection
*CollectionsApi* | [**collections_coluuid_get**](docs/CollectionsApi.md#collections_coluuid_get) | **GET** /collections/{coluuid} | Get contents in a collection
*CollectionsApi* | [**collections_coluuid_post**](docs/CollectionsApi.md#collections_coluuid_post) | **POST** /collections/{coluuid} | Add contents to a collection
*CollectionsApi* | [**collections_fs_add_post**](docs/CollectionsApi.md#collections_fs_add_post) | **POST** /collections/fs/add | Add a file to a collection
*CollectionsApi* | [**collections_get**](docs/CollectionsApi.md#collections_get) | **GET** /collections/ | List all collections
*CollectionsApi* | [**collections_post**](docs/CollectionsApi.md#collections_post) | **POST** /collections/ | Create a new collection
*ContentApi* | [**content_add_car_post**](docs/ContentApi.md#content_add_car_post) | **POST** /content/add-car | Add Car object
*ContentApi* | [**content_add_ipfs_post**](docs/ContentApi.md#content_add_ipfs_post) | **POST** /content/add-ipfs | Add IPFS object
*ContentApi* | [**content_add_post**](docs/ContentApi.md#content_add_post) | **POST** /content/add | Add new content
*ContentApi* | [**content_aggregated_content_get**](docs/ContentApi.md#content_aggregated_content_get) | **GET** /content/aggregated/{content} | Get aggregated content stats
*ContentApi* | [**content_all_deals_get**](docs/ContentApi.md#content_all_deals_get) | **GET** /content/all-deals | Get all deals for a user
*ContentApi* | [**content_bw_usage_content_get**](docs/ContentApi.md#content_bw_usage_content_get) | **GET** /content/bw-usage/{content} | Get content bandwidth
*ContentApi* | [**content_create_post**](docs/ContentApi.md#content_create_post) | **POST** /content/create | Add a new content
*ContentApi* | [**content_deals_get**](docs/ContentApi.md#content_deals_get) | **GET** /content/deals | Content with deals
*ContentApi* | [**content_ensure_replication_datacid_get**](docs/ContentApi.md#content_ensure_replication_datacid_get) | **GET** /content/ensure-replication/{datacid} | Ensure Replication
*ContentApi* | [**content_failures_content_get**](docs/ContentApi.md#content_failures_content_get) | **GET** /content/failures/{content} | List all failures for a content
*ContentApi* | [**content_importdeal_post**](docs/ContentApi.md#content_importdeal_post) | **POST** /content/importdeal | Import a deal
*ContentApi* | [**content_list_get**](docs/ContentApi.md#content_list_get) | **GET** /content/list | List all pinned content
*ContentApi* | [**content_read_cont_get**](docs/ContentApi.md#content_read_cont_get) | **GET** /content/read/{cont} | Read content
*ContentApi* | [**content_staging_zones_get**](docs/ContentApi.md#content_staging_zones_get) | **GET** /content/staging-zones | Get staging zone for user
*ContentApi* | [**content_stats_get**](docs/ContentApi.md#content_stats_get) | **GET** /content/stats | Get content statistics
*ContentApi* | [**content_status_id_get**](docs/ContentApi.md#content_status_id_get) | **GET** /content/status/{id} | Content Status
*DealsApi* | [**deal_estimate_post**](docs/DealsApi.md#deal_estimate_post) | **POST** /deal/estimate | Estimate the cost of a deal
*DealsApi* | [**deal_info_dealid_get**](docs/DealsApi.md#deal_info_dealid_get) | **GET** /deal/info/{dealid} | Get Deal Info
*DealsApi* | [**deal_proposal_propcid_get**](docs/DealsApi.md#deal_proposal_propcid_get) | **GET** /deal/proposal/{propcid} | Get Proposal
*DealsApi* | [**deal_query_miner_get**](docs/DealsApi.md#deal_query_miner_get) | **GET** /deal/query/{miner} | Query Ask
*DealsApi* | [**deal_status_by_proposal_propcid_get**](docs/DealsApi.md#deal_status_by_proposal_propcid_get) | **GET** /deal/status-by-proposal/{propcid} | Get Deal Status by PropCid
*DealsApi* | [**deal_status_miner_propcid_get**](docs/DealsApi.md#deal_status_miner_propcid_get) | **GET** /deal/status/{miner}/{propcid} | Deal Status
*DealsApi* | [**deal_transfer_in_progress_get**](docs/DealsApi.md#deal_transfer_in_progress_get) | **GET** /deal/transfer/in-progress | Transfer In Progress
*DealsApi* | [**deal_transfer_status_post**](docs/DealsApi.md#deal_transfer_status_post) | **POST** /deal/transfer/status | Transfer Status
*DealsApi* | [**deals_failures_get**](docs/DealsApi.md#deals_failures_get) | **GET** /deals/failures | Get storage failures for user
*DealsApi* | [**deals_make_miner_post**](docs/DealsApi.md#deals_make_miner_post) | **POST** /deals/make/{miner} | Make Deal
*DealsApi* | [**deals_status_deal_get**](docs/DealsApi.md#deals_status_deal_get) | **GET** /deals/status/{deal} | Get Deal Status
*DealsApi* | [**public_deals_failures_get**](docs/DealsApi.md#public_deals_failures_get) | **GET** /public/deals/failures | Get storage failures
*DealsApi* | [**public_miners_storage_query_miner_get**](docs/DealsApi.md#public_miners_storage_query_miner_get) | **GET** /public/miners/storage/query/{miner} | Query Ask
*MetricsApi* | [**public_metrics_deals_on_chain_get**](docs/MetricsApi.md#public_metrics_deals_on_chain_get) | **GET** /public/metrics/deals-on-chain | Get deal metrics
*MinerApi* | [**public_miners_deals_miner_get**](docs/MinerApi.md#public_miners_deals_miner_get) | **GET** /public/miners/deals/{miner} | Get all miners deals
*MinerApi* | [**public_miners_stats_miner_get**](docs/MinerApi.md#public_miners_stats_miner_get) | **GET** /public/miners/stats/{miner} | Get miner stats
*NetApi* | [**net_addrs_get**](docs/NetApi.md#net_addrs_get) | **GET** /net/addrs | Net Addrs
*NetApi* | [**public_miners_failures_miner_get**](docs/NetApi.md#public_miners_failures_miner_get) | **GET** /public/miners/failures/{miner} | Get all miners
*NetApi* | [**public_miners_get**](docs/NetApi.md#public_miners_get) | **GET** /public/miners | Get all miners
*NetApi* | [**public_net_addrs_get**](docs/NetApi.md#public_net_addrs_get) | **GET** /public/net/addrs | Net Addrs
*NetApi* | [**public_net_peers_get**](docs/NetApi.md#public_net_peers_get) | **GET** /public/net/peers | Net Peers
*PeeringApi* | [**admin_peering_peers_delete**](docs/PeeringApi.md#admin_peering_peers_delete) | **DELETE** /admin/peering/peers | Remove peers on Peering Service
*PeeringApi* | [**admin_peering_peers_get**](docs/PeeringApi.md#admin_peering_peers_get) | **GET** /admin/peering/peers | List all Peering peers
*PeeringApi* | [**admin_peering_peers_post**](docs/PeeringApi.md#admin_peering_peers_post) | **POST** /admin/peering/peers | Add peers on Peering Service
*PeeringApi* | [**admin_peering_start_post**](docs/PeeringApi.md#admin_peering_start_post) | **POST** /admin/peering/start | Start Peering
*PeeringApi* | [**admin_peering_status_get**](docs/PeeringApi.md#admin_peering_status_get) | **GET** /admin/peering/status | Check Peering Status
*PeeringApi* | [**admin_peering_stop_post**](docs/PeeringApi.md#admin_peering_stop_post) | **POST** /admin/peering/stop | Stop Peering
*PeersApi* | [**admin_peering_peers_delete**](docs/PeersApi.md#admin_peering_peers_delete) | **DELETE** /admin/peering/peers | Remove peers on Peering Service
*PeersApi* | [**admin_peering_peers_get**](docs/PeersApi.md#admin_peering_peers_get) | **GET** /admin/peering/peers | List all Peering peers
*PeersApi* | [**admin_peering_peers_post**](docs/PeersApi.md#admin_peering_peers_post) | **POST** /admin/peering/peers | Add peers on Peering Service
*PeersApi* | [**admin_peering_start_post**](docs/PeersApi.md#admin_peering_start_post) | **POST** /admin/peering/start | Start Peering
*PeersApi* | [**admin_peering_status_get**](docs/PeersApi.md#admin_peering_status_get) | **GET** /admin/peering/status | Check Peering Status
*PeersApi* | [**admin_peering_stop_post**](docs/PeersApi.md#admin_peering_stop_post) | **POST** /admin/peering/stop | Stop Peering
*PinningApi* | [**pinning_pins_get**](docs/PinningApi.md#pinning_pins_get) | **GET** /pinning/pins | List all pin status objects
*PinningApi* | [**pinning_pins_pinid_delete**](docs/PinningApi.md#pinning_pins_pinid_delete) | **DELETE** /pinning/pins/{pinid} | Delete a pinned object
*PinningApi* | [**pinning_pins_pinid_get**](docs/PinningApi.md#pinning_pins_pinid_get) | **GET** /pinning/pins/{pinid} | Get a pin status object
*PinningApi* | [**pinning_pins_pinid_post**](docs/PinningApi.md#pinning_pins_pinid_post) | **POST** /pinning/pins/{pinid} | Replace a pinned object
*PinningApi* | [**pinning_pins_post**](docs/PinningApi.md#pinning_pins_post) | **POST** /pinning/pins | Add and pin object
*PublicApi* | [**public_by_cid_cid_get**](docs/PublicApi.md#public_by_cid_cid_get) | **GET** /public/by-cid/{cid} | Get Content by Cid
*PublicApi* | [**public_info_get**](docs/PublicApi.md#public_info_get) | **GET** /public/info | Get public node info
*PublicApi* | [**public_metrics_deals_on_chain_get**](docs/PublicApi.md#public_metrics_deals_on_chain_get) | **GET** /public/metrics/deals-on-chain | Get deal metrics
*PublicApi* | [**public_miners_deals_miner_get**](docs/PublicApi.md#public_miners_deals_miner_get) | **GET** /public/miners/deals/{miner} | Get all miners deals
*PublicApi* | [**public_miners_failures_miner_get**](docs/PublicApi.md#public_miners_failures_miner_get) | **GET** /public/miners/failures/{miner} | Get all miners
*PublicApi* | [**public_miners_get**](docs/PublicApi.md#public_miners_get) | **GET** /public/miners | Get all miners
*PublicApi* | [**public_miners_stats_miner_get**](docs/PublicApi.md#public_miners_stats_miner_get) | **GET** /public/miners/stats/{miner} | Get miner stats
*PublicApi* | [**public_net_addrs_get**](docs/PublicApi.md#public_net_addrs_get) | **GET** /public/net/addrs | Net Addrs
*PublicApi* | [**public_net_peers_get**](docs/PublicApi.md#public_net_peers_get) | **GET** /public/net/peers | Net Peers
*PublicApi* | [**public_stats_get**](docs/PublicApi.md#public_stats_get) | **GET** /public/stats | Public stats

## Documentation For Models

 - [ContentAddBody](docs/ContentAddBody.md)
 - [MainCollection](docs/MainCollection.md)
 - [MainCreateCollectionBody](docs/MainCreateCollectionBody.md)
 - [MainEstimateDealBody](docs/MainEstimateDealBody.md)
 - [MainGetApiKeysResp](docs/MainGetApiKeysResp.md)
 - [MainImportDealBody](docs/MainImportDealBody.md)
 - [MainUserStatsResponse](docs/MainUserStatsResponse.md)
 - [UtilContentAddIpfsBody](docs/UtilContentAddIpfsBody.md)
 - [UtilContentAddResponse](docs/UtilContentAddResponse.md)
 - [UtilHttpError](docs/UtilHttpError.md)

## Documentation For Authorization


## bearerAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author


