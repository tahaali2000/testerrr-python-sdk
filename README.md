
# Getting Started with PayPal REST APIs

## Introduction

An order represents a payment between two or more parties. Use the Orders API to create, update, retrieve, authorize, and capture orders., Call the Payments API to authorize payments, capture authorized payments, refund payments that have already been captured, and show payment information. Use the Payments API in conjunction with the <a href="/docs/api/orders/v2/">Orders API</a>. For more information, see the <a href="/docs/checkout/">PayPal Checkout Overview</a>., The Payment Method Tokens API saves payment methods so payers don't have to enter details for future transactions. Payers can check out faster or pay without being present after they agree to save a payment method.<br><br>The API associates a payment method with a temporary setup token. Pass the setup token to the API to exchange the setup token for a permanent token.<br><br>The permanent token represents a payment method that's saved to the vault. This token can be used repeatedly for checkout or recurring transactions such as subscriptions.<br><br>The Payment Method Tokens API is available in the US only.

Find out more here: [https://developer.paypal.com/docs/api/orders/v2/](https://developer.paypal.com/docs/api/orders/v2/)

## Install the Package

The package is compatible with Python versions `3.7+`.
Install the package from PyPi using the following pip command:

```bash
pip install testerrr-sdk==1.6.9
```

You can also view the package at:
https://pypi.python.org/pypi/testerrr-sdk/1.6.9

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](https://www.github.com/tahaali2000/testerrr-python-sdk/tree/1.6.9/doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| environment | `Environment` | The API environment. <br> **Default: `Environment.SANDBOX`** |
| http_client_instance | `HttpClient` | The Http Client passed from the sdk user for making requests |
| override_http_client_configuration | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| http_call_back | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| timeout | `float` | The value to use for connection timeout. <br> **Default: 60** |
| max_retries | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| backoff_factor | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| retry_statuses | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524, 408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT', 'GET', 'PUT']** |
| logging_configuration | [`LoggingConfiguration`](https://www.github.com/tahaali2000/testerrr-python-sdk/tree/1.6.9/doc/logging-configuration.md) | The SDK logging configuration for API calls |
| client_credentials_auth_credentials | [`ClientCredentialsAuthCredentials`](https://www.github.com/tahaali2000/testerrr-python-sdk/tree/1.6.9/doc/auth/oauth-2-client-credentials-grant.md) | The credential object for OAuth 2 Client Credentials Grant |

The API client can be initialized as follows:

```python
client = PaypalrestapisClient(
    client_credentials_auth_credentials=ClientCredentialsAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret'
    ),
    environment=Environment.SANDBOX,
    logging_configuration=LoggingConfiguration(
        log_level=logging.INFO,
        request_logging_config=RequestLoggingConfiguration(
            log_body=True
        ),
        response_logging_config=ResponseLoggingConfiguration(
            log_headers=True
        )
    )
)
```

## Environments

The SDK can be configured to use a different environment for making API calls. Available environments are:

### Fields

| Name | Description |
|  --- | --- |
| Production | PayPal Live Environment |
| Sandbox | **Default** PayPal Sandbox Environment |

## Authorization

This API uses the following authentication schemes.

* [`Oauth2 (OAuth 2 Client Credentials Grant)`](https://www.github.com/tahaali2000/testerrr-python-sdk/tree/1.6.9/doc/auth/oauth-2-client-credentials-grant.md)

## List of APIs

* [Orders](https://www.github.com/tahaali2000/testerrr-python-sdk/tree/1.6.9/doc/controllers/orders.md)
* [Payments](https://www.github.com/tahaali2000/testerrr-python-sdk/tree/1.6.9/doc/controllers/payments.md)
* [Vault](https://www.github.com/tahaali2000/testerrr-python-sdk/tree/1.6.9/doc/controllers/vault.md)

## SDK Infrastructure

### Configuration

* [AbstractLogger](https://www.github.com/tahaali2000/testerrr-python-sdk/tree/1.6.9/doc/abstract-logger.md)
* [LoggingConfiguration](https://www.github.com/tahaali2000/testerrr-python-sdk/tree/1.6.9/doc/logging-configuration.md)
* [RequestLoggingConfiguration](https://www.github.com/tahaali2000/testerrr-python-sdk/tree/1.6.9/doc/request-logging-configuration.md)
* [ResponseLoggingConfiguration](https://www.github.com/tahaali2000/testerrr-python-sdk/tree/1.6.9/doc/response-logging-configuration.md)

### HTTP

* [HttpResponse](https://www.github.com/tahaali2000/testerrr-python-sdk/tree/1.6.9/doc/http-response.md)
* [HttpRequest](https://www.github.com/tahaali2000/testerrr-python-sdk/tree/1.6.9/doc/http-request.md)

### Utilities

* [ApiHelper](https://www.github.com/tahaali2000/testerrr-python-sdk/tree/1.6.9/doc/api-helper.md)
* [HttpDateTime](https://www.github.com/tahaali2000/testerrr-python-sdk/tree/1.6.9/doc/http-date-time.md)
* [RFC3339DateTime](https://www.github.com/tahaali2000/testerrr-python-sdk/tree/1.6.9/doc/rfc3339-date-time.md)
* [UnixDateTime](https://www.github.com/tahaali2000/testerrr-python-sdk/tree/1.6.9/doc/unix-date-time.md)

