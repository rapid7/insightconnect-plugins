# Description

[Maxmind's minFraud](https://www.maxmind.com/en/minfraud-services) service provides fraud intelligence data. The minFraud service queries the insights service
via its API and provides relevant data on the transaction data provided, including an overall risk score. The
actions have been broken down into each top-level request field.

This plugin utilizes the minFraud API and implements all of its available lookups.

# Key Features

* Fraudulent Transactions Detection

# Requirements

* License

# Documentation

## Setup

A valid user ID and license key are required to authenticate to the minFraud API.
The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user|integer|None|True|User ID number|None|
|license|credential_secret_key|None|True|License key|None|

## Technical Details

### Actions

#### Payment Lookup

This action can be used to retrieve intelligence information for a given payment processor.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|address|string|None|True|IP address to query|None|
|payment_processor|string|None|False|Payment process ued for transaction|['none', 'adyen', 'altapay', 'amazon_payments', 'authorizenet', 'balanced', 'beanstream', 'bluepay', 'braintree', 'ccnow', 'chase_paymentech', 'cielo', 'collector', 'compropago', 'concept_payments', 'conekta', 'cuentadigital', 'dalpay', 'dibs', 'digital_river', 'ecomm365', 'elavon', 'epay', 'eprocessing_network', 'eway', 'first_data', 'global_payments', 'ingenico', 'internetsecure', 'intuit_quickbooks_payments', 'iugu', 'mastercard_payment_gateway', 'mercadopago', 'merchant_esolutions', 'mirjeh', 'mollie', 'moneris_solutions', 'nmi', 'openpaymx', 'optimal_payments', 'orangepay', 'other', 'pacnet_services', 'payfast', 'paygate', 'payone', 'paypal', 'payplus', 'paystation', 'paytrace', 'paytrail', 'payture', 'payu', 'payulatam', 'pinpayments', 'princeton_payment_solutions', 'psigate', 'qiwi', 'quickpay', 'raberil', 'rede', 'redpagos', 'rewardspay', 'sagepay', 'simplify_commerce', 'skrill', 'smartcoin', 'sps_decidir', 'stripe', 'telerecargas', 'towah', 'usa_epay', 'verepay', 'vindicia', 'virtual_card_services', 'vme', 'worldpay']|
|payment_was_authorized|boolean|None|False|Payment authorized\: true/false|None|
|payment_decline_code|string|None|False|Payment decline code|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_score|string|False|Overall risk score|

#### Credit Card Lookup

This action can be used to retrieve intelligence information for a given credit card.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|bank_phone_country_code|string|None|False|Phone country code for bank|None|
|avs_result|string|None|False|Address Verification System result|None|
|cvv_result|string|None|False|Card Verification Value code|None|
|card_issuer_id_number|string|None|False|Issuer ID number for the credit card|None|
|card_bank_name|string|None|False|Issuing bank of the credit card|None|
|address|string|None|True|IP address to query|None|
|card_token|string|None|False|Token representing the credit card|None|
|bank_phone_number|string|None|False|Phone number for bank|None|
|card_last_4_digits|string|None|False|Last 4 digits of credit card|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_score|string|False|Overall risk score|
|credit_card_result|credit_card|False|Result for credit card|

#### Shopping Cart Lookup

This action can be used to retrieve intelligence information for a given shopping cart item.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|item_id|string|None|False|Internal ID for the item|None|
|price|string|None|False|Item price|None|
|address|string|None|True|IP address to query|None|
|item_category|string|None|False|Category of the item|None|
|quantity|integer|None|False|Item quantity|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_score|string|False|Overall risk score|

#### Account Lookup

This action can be used to retrieve intelligence information for a given end-user account.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id|string|None|False|ID associated with the end-user|None|
|username_md5|string|None|False|MD5 hash of the username|None|
|address|string|None|True|IP address to query|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_score|string|False|Overall risk score|

#### Billing Address Lookup

This action can be used to retrieve intelligence information for a given billing name or address.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|billing_address|string|None|False|Billing address line 1|None|
|billing_city|string|None|False|City of billing address|None|
|billing_region|string|None|False|Subdivision code in billing address|None|
|billing_first_name|string|None|False|First name in billing info|None|
|billing_postal|string|None|False|Postal Code in billing address|None|
|billing_address_2|string|None|False|Billing address line 2|None|
|billing_company|string|None|False|Company name in billing info|None|
|address|string|None|True|IP address to query|None|
|billing_phone_country_code|string|None|False|Country code for phone number|None|
|billing_phone_number|string|None|False|Phone number without country code|None|
|billing_country|string|None|False|Two character country code|None|
|billing_last_name|string|None|False|Last name in billing info|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_score|string|False|Overall risk score|
|billing_result|billing|False|Results for billing|

#### Master Lookup

This action can be used to retrieve intelligence information for all query items from the minFraud services.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|False|Domain of email used in transaction|None|
|event_type|string|None|False|Type of event|['none', 'account_creation', 'account_login', 'email_change', 'password_reset', 'purchase', 'recurring_purchase', 'referral']|
|billing_region|string|None|False|Subdivision code in billing address|None|
|cvv_result|string|None|False|Card Verification Value code|None|
|order_affiliate_id|string|None|False|ID of the affiliate|None|
|billing_city|string|None|False|City of billing address|None|
|shop_id|string|None|False|Internal ID for the shop|None|
|order_has_gift_message|boolean|None|False|Order has gift message|None|
|order_amount|string|None|False|Total order amount|None|
|card_token|string|None|False|Token representing the credit card|None|
|shipping_phone_country_code|string|None|False|Country code for phone number|None|
|order_currency|string|None|False|Currency code for the currency used|None|
|billing_country|string|None|False|Two character country code|None|
|payment_was_authorized|boolean|None|False|Payment authorized\: true/false|None|
|billing_last_name|string|None|False|Last name in billing info|None|
|user_id|string|None|False|ID associated with the end-user|None|
|shipping_delivery_speed|string|None|False|Shipping Delivery Speed|['none', 'same_day', 'overnight', 'expedited', 'standard']|
|billing_phone_number|string|None|False|Phone number without country code|None|
|shipping_last_name|string|None|False|Last name in shipping info|None|
|shipping_region|string|None|False|Subdivision code in shipping address|None|
|billing_phone_country_code|string|None|False|Country code for phone number|None|
|payment_processor|string|None|False|Payment process ued for transaction|['none', 'adyen', 'altapay', 'amazon_payments', 'authorizenet', 'balanced', 'beanstream', 'bluepay', 'braintree', 'ccnow', 'chase_paymentech', 'cielo', 'collector', 'compropago', 'concept_payments', 'conekta', 'cuentadigital', 'dalpay', 'dibs', 'digital_river', 'ecomm365', 'elavon', 'epay', 'eprocessing_network', 'eway', 'first_data', 'global_payments', 'ingenico', 'internetsecure', 'intuit_quickbooks_payments', 'iugu', 'mastercard_payment_gateway', 'mercadopago', 'merchant_esolutions', 'mirjeh', 'mollie', 'moneris_solutions', 'nmi', 'openpaymx', 'optimal_payments', 'orangepay', 'other', 'pacnet_services', 'payfast', 'paygate', 'payone', 'paypal', 'payplus', 'paystation', 'paytrace', 'paytrail', 'payture', 'payu', 'payulatam', 'pinpayments', 'princeton_payment_solutions', 'psigate', 'qiwi', 'quickpay', 'raberil', 'rede', 'redpagos', 'rewardspay', 'sagepay', 'simplify_commerce', 'skrill', 'smartcoin', 'sps_decidir', 'stripe', 'telerecargas', 'towah', 'usa_epay', 'verepay', 'vindicia', 'virtual_card_services', 'vme', 'worldpay']|
|time|string|None|False|Time of event|None|
|email|string|None|False|Email address used in transaction|None|
|transaction_id|string|None|False|Transaction ID|None|
|billing_address|string|None|False|Billing address line 1|None|
|shipping_city|string|None|False|City of shipping address|None|
|billing_first_name|string|None|False|First name in billing info|None|
|order_is_gift|boolean|None|False|Order is gift|None|
|price|string|None|False|Item price|None|
|shipping_postal|string|None|False|Postal Code in shipping address|None|
|card_bank_name|string|None|False|Issuing bank of the credit card|None|
|card_issuer_id_number|string|None|False|Issuer ID number for the credit card|None|
|billing_address_2|string|None|False|Billing address line 2|None|
|order_referrer_uri|string|None|False|URI of the referring site|None|
|bank_phone_country_code|string|None|False|Phone country code for bank|None|
|accept_language|string|None|False|HTTP Accept-Language header|None|
|address|string|None|True|IP address to query|None|
|item_id|string|None|False|Internal ID for the item|None|
|payment_decline_code|string|None|False|Payment decline code|None|
|billing_postal|string|None|False|Postal Code in billing address|None|
|bank_phone_number|string|None|False|Phone number for bank|None|
|username_md5|string|None|False|MD5 hash of the username|None|
|shipping_address_2|string|None|False|Shipping address line 2|None|
|card_last_4_digits|string|None|False|Last 4 digits of credit card|None|
|item_category|string|None|False|Category of the item|None|
|shipping_first_name|string|None|False|First name in shipping info|None|
|order_discount_code|string|None|False|Discount code applied to transaction|None|
|shipping_country|string|None|False|Two character country code|None|
|user_agent|string|None|False|HTTP User-Agent header|None|
|billing_company|string|None|False|Company name in billing info|None|
|shipping_address|string|None|False|Shipping address line 1|None|
|order_subaffiliate_id|string|None|False|ID of the subaffiliate|None|
|shipping_company|string|None|False|Company name in shipping info|None|
|shipping_phone_number|string|None|False|Phone number without country code|None|
|avs_result|string|None|False|Address Verification System result|None|
|quantity|integer|None|False|Item quantity|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_score|string|False|Overall risk score|
|all_result|all|False|Result for all|

#### Event Lookup

This action can be used to retrieve intelligence information for a given transaction event.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|address|string|None|True|IP address to query|None|
|shop_id|string|None|False|Internal ID for the shop|None|
|event_type|string|None|False|Type of event|['none', 'account_creation', 'account_login', 'email_change', 'password_reset', 'purchase', 'recurring_purchase', 'referral', 'survey']|
|transaction_id|string|None|False|Transaction ID|None|
|time|string|None|False|Time of event|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_score|string|False|Overall risk score|

#### Email Lookup

This action can be used to retrieve intelligence information for a given email address, email domain, or MD5 email hash.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|False|Domain of email used in transaction|None|
|email|string|None|False|Email address used in transaction|None|
|address|string|None|True|IP address to query|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|email_result|email|False|Results for email|
|risk_score|string|False|Overall risk score|

#### Shipping Address Lookup

This action can be used to retrieve intelligence information for a given shipping name or address.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|shipping_last_name|string|None|False|Last name in shipping info|None|
|shipping_city|string|None|False|City of shipping address|None|
|shipping_first_name|string|None|False|First name in shipping info|None|
|shipping_region|string|None|False|Subdivision code in shipping address|None|
|shipping_postal|string|None|False|Postal Code in shipping address|None|
|shipping_delivery_speed|string|None|False|Shipping Delivery Speed|['none', 'same_day', 'overnight', 'expedited', 'standard']|
|shipping_address_2|string|None|False|Shipping address line 2|None|
|shipping_address|string|None|False|Shipping address line 1|None|
|shipping_company|string|None|False|Company name in shipping info|None|
|shipping_phone_country_code|string|None|False|Country code for phone number|None|
|shipping_phone_number|string|None|False|Phone number without country code|None|
|shipping_country|string|None|False|Two character country code|None|
|address|string|None|True|IP address to query|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_score|string|False|Overall risk score|
|shipping_result|shipping|False|Results for shipping|

#### Device Lookup

This action can be used to retrieve intelligence information for a given IP address.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_agent|string|None|False|HTTP User-Agent header|None|
|accept_language|string|None|False|HTTP Accept-Language header|None|
|address|string|None|True|IP address to query|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ip_result|ip|False|Results for ip|
|risk_score|string|False|Overall risk score|
|device_result|device|False|Results for device|

#### Order Lookup

This action can be used to retrieve intelligence information for a given order transaction.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|order_is_gift|boolean|None|False|Order is gift|None|
|order_affiliate_id|string|None|False|ID of the affiliate|None|
|order_amount|string|None|False|Total order amount|None|
|order_referrer_uri|string|None|False|URI of the referring site|None|
|order_has_gift_message|boolean|None|False|Order has gift message|None|
|address|string|None|True|IP address to query|None|
|order_subaffiliate_id|string|None|False|ID of the subaffiliate|None|
|order_currency|string|None|False|Currency code for the currency used|None|
|order_discount_code|string|None|False|Discount code applied to transaction|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_score|string|False|Overall risk score|

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Make sure you supply a valid license key and user ID as an integer. Also, be sure that the correct items for each input are given.
Refer to the minFraud API documentation for explicit details.

# Version History

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types | Rename actions
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [minFraud](https://www.maxmind.com/en/minfraud-services)
* [minFraud API](https://dev.maxmind.com/minfraud/)

