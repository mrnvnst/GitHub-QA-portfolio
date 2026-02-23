## Bag Reports
### Navigation

1. Adding product to a kit: POST /api/v1/kits/{id}/products 
- [BR-001: POST /api/v1/kits/{id}/products status 500 when productsList is missing](#br-001)
- [BR-002: POST /api/v1/kits/{id}/products status 500 when empty productsList is sent](#br-002)
- [BR-003: POST /api/v1/kits/{id}/products status 200 when product id does not exist](#br-003)
- [BR-004: POST /api/v1/kits/{id}/products status 200 when product id is missing](#br-004)
- [BR-005: POST /api/v1/kits/{id}/products status 200 when product id = 0](#br-005)
- [BR-006: POST /api/v1/kits/{id}/products status 200 when product id is negative](#br-006)
- [BR-007: POST /api/v1/kits/{id}/products status 500 product when id exceeding integer limit](#br-007)
- [BR-008: POST /api/v1/kits/{id}/products status 500 when product id is non-numeric](#br-008)
- [BR-009: POST /api/v1/kits/{id}/products status 500 when quantity is missing](#br-009)
- [BR-010: POST /api/v1/kits/{id}/products status 500 when string value in quantity](#br-010)
- [BR-011: POST /api/v1/kits/{id}/products status 200 when quantity = 0](#br-011)
- [BR-012: POST /api/v1/kits/{id}/products status 500 when quantity is decimal](#br-012)
- [BR-013: POST /api/v1/kits/{id}/products status 200 when quantity is empty string](#br-013)
- [BR-014: POST /api/v1/kits/{id}/products status 500 when quantity is negative](#br-014)
- [BR-015: POST /api/v1/kits/{id}/products status 500 when quantity exceeding integer limit](#br-015)

2. Проверка возможности доставки и ее стоимости: POST /fast-delivery/v3.1.1/calculate-delivery.xml
- [BR-016: POST /fast-delivery/v3.1.1/calculate-delivery.xml status 500 when required parameters are missing](#br-016)
- [BR-017: POST /fast-delivery/v3.1.1/calculate-delivery.xml status 200 OK for invalid productsCount values](#br-017)
- [BR-019: POST /fast-delivery/v3.1.1/calculate-delivery.xml status 200 OK for invalid productsWeight values](#br-019)
- [BR-021: POST /fast-delivery/v3.1.1/calculate-delivery.xml response body missing required attribute when deliveryTime is outside working hours](#br-021)

3. Adding products to a basket: PUT /api/v1/orders/:id
- [BR-024: PUT /api/v1/orders/:id status 200 when string is sent instead of productsList array](#br-024)
- [BR-027: PUT /api/v1/orders/:id status 500 when product id exceeds integer limit](#br-027)
- [BR-029: PUT /api/v1/orders/:id status 200 when quantity is "", 0, or null](#br-029)

4. Deleting basket: DELETE /api/v1/orders/:id 
- [BR-031: DELETE /api/v1/orders/:id status 404 when deleting existing basket](#br-031)

## BR-001
## POST /api/v1/kits/{id}/products status 500 when productsList is missing

### Description
Sending a POST request without the required productsList parameter returns 500 Internal Server Error.

Expected behavior: 400 Bad Request.

### Preconditions

1. The server is running.
2. A kit with id = 7 has been created.

### Steps to Reproduce

1. Send POST-request
 /api/v1/kits/:id/products
2. Provide the empty request body.

### Expected Result

1. 400 Bad Request.

### Actual Result  

1. 500 Internal Server Error.

### Attachments    

```
curl --location --request POST 'https://teststand.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data ''
```

### Environment
- URL: https://teststand.ru.
- API version: /api/v3.1.1.
- Tool: Postman 11.85.1.

#### Severity: Critical
#### Status: Open

---

## BR-002
## POST /api/v1/kits/{id}/products status 500 when empty productsList is sent

### Description

Empty JSON body results in 500 Internal Server Error instead of validation error.

### Preconditions

1. The server is running.
2. A kit with id = 7 has been created.

### Steps to Reproduce

1. Send POST-request 
/api/v1/kits/:id/products
2. Provide the following request body:

```json
{
  "productsList": []
}
```

### Expected Result

1. 400 Bad Request.

### Actual Result  

1. 500 Internal Server Error.

### Attachments  

```
"curl --location --request POST 'https://teststand.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
  "productsList": []
}'
```

### Environment
- URL: https://teststand.ru.
- API version: /api/v3.1.1.
- Tool: Postman 11.85.1.

#### Severity: Critical
#### Status: Open

---

## BR-003
## POST /api/v1/kits/{id}/products status 200 when product id does not exist

### Description

API allows adding product that does not exist in database.

### Preconditions

1. The server is running.
2. A kit with id = 7 has been created.

### Steps to Reproduce

1. Send POST-request 
 /api/v1/kits/:id/products
2. Provide the following request body:

```json
{
  "productsList": [
    { "id": 127, "quantity": 2 }
  ]
}
```

### Expected Result

1. 400 Bad Request.
2. The product is not added to the kit.

### Actual Result    

1. 200 OK.
2. The product is added to the kit.


### Attachments   

```
"curl --location 'https://teststand.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": 127,
            ""quantity"": 2
        }
    ]
}'"
```

### Environment
- URL: https://teststand.ru.
- API version: /api/v3.1.1.
- Tool: Postman 11.85.1.

#### Severity: Critical
#### Status: Open

---

## BR-004
## POST /api/v1/kits/{id}/products status 200 when product id is missing

### Description

Missing product id is not validated.

### Preconditions

1. The server is running.
2. A kit with id = 7 has been created.

### Steps to Reproduce

1. Send POST-request 
 /api/v1/kits/:id/products
2. Provide the following request body:

```json
{
    "productsList": [
        {
            "quantity": 3
        }
    ]
}
```

### Expected Result

1. 400 Bad Request.
2. The product is not added to the kit.

### Actual Result  

1. 200 OK.
2. The product is added to the kit:

```json
 [id:undefined; quantity:3]
```

### Attachments     

```
"curl --location 'https://teststand.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""quantity"": 3
        }
    ]
}'"
```

### Environment
- URL: https://teststand.ru.
- API version: /api/v3.1.1.
- Tool: Postman 11.85.1.

#### Severity: Critical
#### Status: Open

---

## BR-005
## POST /api/v1/kits/{id}/products status 200 when product id = 0

### Description

Zero id accepted as valid product.

### Preconditions

1. The server is running.
2. A kit with id = 7 has been created.

### Steps to Reproduce

1. Send POST-request 
 /api/v1/kits/:id/products
2. Provide the following request body:

```json
{
    "productsList": [
        {
            "id": 0,
            "quantity": 1
        }
    ]
```

### Expected Result

1. 400 Bad Request.
2. The product is not added to the kit.

### Actual Result    

1. 200 OK.
2. The product is added to the kit:

```json
 [id:0; quantity:1]
```


### Attachments     

```
"curl --location 'https://teststand.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": 0,
            ""quantity"": 1
        }
    ]
}'"
```

### Environment
- URL: https://teststand.ru.
- API version: /api/v3.1.1.
- Tool: Postman 11.85.1.

#### Severity: Critical
#### Status: Open

---

## BR-006
## POST /api/v1/kits/{id}/products status 200 when product id is negative

### Description

Negative product id is accepted.

### Preconditions

1. The server is running.
2. A kit with id = 7 has been created.

### Steps to Reproduce

1. Send POST-request 
 /api/v1/kits/:id/products
2. Provide the following request body:

```json
{
    "productsList": [
        {
            "id": -7,
            "quantity": 1
        }
    ]
}
```

### Expected Result

1. 400 Bad Request.
2. The product is not added to the kit.

### Actual Result  

1. 200 OK.
2. The product is added to the kit:

```json
 [id:-7; quantity:1]
```

---

### Attachments     

```
curl --location 'https://teststand.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    "productsList": [
        {
            "id": -7,
            "quantity": 1
        }
    ]
}'
```

### Environment
- URL: https://teststand.ru.
- API version: /api/v3.1.1.
- Tool: Postman 11.85.1.

#### Severity: Critical
#### Status: Open

---

## BR-007
## POST /api/v1/kits/{id}/products status 500 product when id exceeding integer limit

### Description

Passing product ID exceeding integer limit causes 500 Internal Server Error.

Expected: 400 Bad Request.

### Preconditions

1. The server is running.
2. A kit with id = 7 has been created.

### Steps to Reproduce

1. Send POST-request 
 /api/v1/kits/:id/products
2. Provide the following request body:

```json
{
  "productsList": [
    { "id": 2147483795, "quantity": 1 }
  ]
}
```

### Expected Result

1. 400 Bad Request.
2. The product is not added to the kit.

### Actual Result  

1. 500 Internal Server Error.

### Attachments     

```
"curl --location 'https://teststand.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": 2147483795,
            ""quantity"": 1
        }
    ]
}'"
```

### Environment
- URL: https://teststand.ru.
- API version: /api/v3.1.1.
- Tool: Postman 11.85.1.

#### Severity: Critical
#### Status: Open

---

## BR-008
## POST /api/v1/kits/{id}/products status 500 when product id is non-numeric

### Description

Non-numeric product IDs cause 500 Internal Server Error.

Expected: 400 Bad Request.

### Preconditions

1. The server is running.
2. A kit with id = 7 has been created.

### Steps to Reproduce

1. Send POST-request 
 /api/v1/kits/:id/products
2. Provide the following request body:

```json
{
    "productsList": [
        {
            "id": "тридцать",
или
            "id": "%^$",
или
            "id": true,
или
            "id": "",

            "quantity": 1
        }
    ]
}
```

### Expected Result

1. 400 Bad Request.

### Actual Result  

1. 500 Internal Server Error.

### Attachments     

```
"1. curl --location 'https://teststand.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": ""тридцать"",
            ""quantity"": 1
        }
    ]
}'

2. curl --location 'https://teststand.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": ""%^$"",
            ""quantity"": 1
        }
    ]
}'

3.  curl --location 'https://teststand.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": """",
            ""quantity"": 1
        }
    ]
}'

4. curl --location 'https://teststand.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": true,
            ""quantity"": 1
        }
    ]
}'"
```

### Environment
- URL: https://teststand.ru.
- API version: /api/v3.1.1.
- Tool: Postman 11.85.1.

#### Severity: Critical
#### Status: Open

---

## BR-009
## POST /api/v1/kits/{id}/products status 500 when quantity is missing

### Description

Missing quantity field causes 500 instead of validation error.

### Preconditions

1. The server is running.
2. A kit with id = 7 has been created.

### Steps to Reproduce

1. Send POST-request 
 /api/v1/kits/:id/products
2. Provide the following request body:

```json
{
    "productsList": [
        {
            "id": 28
        }
    ]
}
```

### Expected Result

1. 400 Bad Request.

### Actual Result 

1. 500 Internal Server Error:

```json
{"code":500,"message":"invalid input syntax for integer: \"3undefined\""}
```

### Attachments     

```
"curl --location 'https://teststand.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": 28
        }
    ]
}'"
```

### Environment
- URL: https://teststand.ru.
- API version: /api/v3.1.1.
- Tool: Postman 11.85.1.

#### Severity: Critical
#### Status: Open

---

## BR-010
## POST /api/v1/kits/{id}/products status 500 when string value in quantity

### Description

String value in quantity causes server error.

### Preconditions

1. The server is running.
2. A kit with id = 7 has been created.

### Steps to Reproduce

1. Send POST-request 
 /api/v1/kits/:id/products
2. Provide the following request body:

```json
{
    "productsList": [
        {
            "id": 3,
            "quantity": "семь"
        }
    ]
}
```

### Expected Result

1. 400 Bad Request.

### Actual Result  

1. 500 Internal Server Error.

### Attachments     

```
"curl --location 'https://teststand.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": 3,
            ""quantity"": ""семь""
        }
    ]
}'"
```

### Environment
- URL: https://teststand.ru.
- API version: /api/v3.1.1.
- Tool: Postman 11.85.1.

#### Severity: Critical
#### Status: Open

---

## BR-011
## POST /api/v1/kits/{id}/products status 200 when quantity = 0

### Description

Quantity = 0 is accepted and processed.

### Preconditions

1. The server is running.
2. A kit with id = 7 has been created.

### Steps to Reproduce

1. Send POST-request 
 /api/v1/kits/:id/products
2. Provide the following request body:

```json
{
    "productsList": [
        {
            "id": 3,
            "quantity": 0
        }
    ]
}
```

### Expected Result

1. 400 Bad Request.
2. The product is not added to the kit.

### Actual Result   

1. 200 OK.
2.  The product is added to the kit:

```json
[id:3; quantity:0]
```

### Attachments     

```
curl --location 'https://teststand.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": 3,
            ""quantity"": 0
        }
    ]
} 
```

### Environment
- URL: https://teststand.ru.
- API version: /api/v3.1.1.
- Tool: Postman 11.85.1.

#### Severity: Critical
#### Status: Open

---

## BR-012
## POST /api/v1/kits/{id}/products status 500 when quantity is decimal

### Description

Decimal quantity results in 500 Internal Server Error.

### Preconditions

1. The server is running.
2. A kit with id = 7 has been created.

### Steps to Reproduce

1. Send POST-request 
 /api/v1/kits/:id/products
2. Provide the following request body:

```json
{
    "productsList": [
        {
            "id": 12,
            "quantity": 7.4
        }
    ]
}
```

### Expected Result

1. 400 Bad Request.

### Actual Result   

1. 500 Internal Server Error:

```json
"code":500,"message":"invalid input syntax for integer: \"10.4\""
```

### Attachments     

```
curl --location 'https://144b85d2-7f95-4653-b594-be7173cae0da.serverhub.praktikum-services.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": 12,
            ""quantity"": 7.4

        }
    ]
}
```

### Environment
- URL: https://teststand.ru.
- API version: /api/v3.1.1.
- Tool: Postman 11.85.1.

#### Severity: Critical
#### Status: Open

---

## BR-013
## POST /api/v1/kits/{id}/products status 200 when quantity is empty string

### Description

Empty string quantity is accepted.

### Preconditions

1. The server is running.
2. A kit with id = 7 has been created.

### Steps to Reproduce

1. Send POST-request 
 /api/v1/kits/:id/products
2. Provide the following request body:

```json
{
    "productsList": [
        {
            "id": 12,
            "quantity": ""
        }
    ]
}
}
```

### Expected Result

1. 400 Bad Request.
2. The product is not added to the kit.

### Actual Result  

1. 500 Internal Server Error.
2. The product is added to the kit:

```json
[id:12; quantity:]
```

### Attachments     

```"curl --location 'https://teststand.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": 12,
            ""quantity"": """"
        }
    ]
}'"
```

### Environment
- URL: https://teststand.ru.
- API version: /api/v3.1.1.
- Tool: Postman 11.85.1.

#### Severity: Critical
#### Status: Open

---

## BR-014
## POST /api/v1/kits/{id}/products status 500 when quantity is negative

### Description

Negative quantity causes 500 Internal Server Error.

### Preconditions

1. The server is running.
2. A kit with id = 7 has been created.

### Steps to Reproduce

1. Send POST-request 
 /api/v1/kits/:id/products
2. Provide the following request body:

```json
{
    "productsList": [
        {
            "id": 17,
            "quantity":-3
        }
    ]
}
```

### Expected Result

1. 400 Bad Request.

### Actual Result  

1. 500 Internal Server Error:

```json
{"code":500,"message":"invalid input syntax for integer: \"3-3\""}

```

### Attachments     

```
"curl --location 'https://teststand.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": 17,
            ""quantity"":-3
        }
    ]
}'"
```

### Environment
- URL: https://teststand.ru.
- API version: /api/v3.1.1.
- Tool: Postman 11.85.1.

#### Severity: Critical
#### Status: Open

---

## BR-015
## POST /api/v1/kits/{id}/products status 500 when quantity exceeding integer limit

### Description

Quantity exceeding integer limit causes server error.

### Preconditions

1. The server is running.
2. A kit with id = 7 has been created.

### Steps to Reproduce

1. Send POST-request 
 /api/v1/kits/:id/products
2. Provide the following request body:

```json
{
    "productsList": [
        {
            "id": 25,
            "quantity":2147483647
        }
    ]
}
```

### Expected Result

1. 400 Bad Request.

### Actual Result   

1. 500 Internal Server Error:

```json

{"code":500,"message":"value \"32147483647\" is out of range for type integer"}
```

### Attachments     

```
"curl --location 'https://144b85d2-7f95-4653-b594-be7173cae0da.serverhub.praktikum-services.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": 25,
            ""quantity"":2147483647
        }
    ]
}'
```

### Environment
- URL: https://teststand.ru.
- API version: /api/v3.1.1.
- Tool: Postman 11.85.1.

#### Severity: Critical
#### Status: Open

---

## BR-016
## POST /fast-delivery/v3.1.1/calculate-delivery.xml status 500 when required parameters are missing

### Description

When sending a POST request to the fast delivery endpoint without required parameters (productsCount, productsWeight, deliveryTime), the API returns 500 Internal Server Error.

According to the specification, the API must return 400 Bad Request when required parameters are missing.

### Preconditions

The server is running.

### Steps to Reproduce

1. Send POST-request
/fast-delivery/v3.1.1/calculate-delivery.xml
2. Provide the empty request body.


### Expected Result

1. 400 Bad Request.
2. Delivery is impossible and calculation is not performed.

### Actual Result  

1. 500 Internal Server Error.


### Attachments     

```
"curl --location 
--request POST 'https://teststand.ru/fast-delivery/v3.1.1/calculate-delivery.xml' \
--data ''"
```

### Environment
- URL: https://teststand.ru.
- API version: /api/v3.1.1.
- Tool: Postman 11.85.1.

#### Severity: Critical
#### Status: Open

---

## BR-017
## POST /fast-delivery/v3.1.1/calculate-delivery.xml status 200 OK for invalid productsCount values

### Description

When sending invalid values in productsCount:
- 0
- negative numbers
- string values
- empty value
- value exceeding INT range

The API returns 200 OK and calculates delivery, instead of returning validation error.

### Preconditions

The server is running.

### Steps to Reproduce

1. Send POST-request
/fast-delivery/v3.1.1/calculate-delivery.xml

2. Provide the empty request body (0):

```xml
<InputModel>
    <productsCount>0</productsCount>
    <productsWeight>0.1</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>
```
or (negative numbers):

```xml
<InputModel>
    <productsCount>-1</productsCount>
    <productsWeight>0.1</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>
```
or (empty value):

```xml
<InputModel>
    <productsCount>""</productsCount>
    <productsWeight>0.1</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>
```
or (string values):

```xml
<InputModel>
    <productsCount>шесть</productsCount>
    <productsWeight>0.1</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>
```
or (value exceeding INT range):

```xml
<InputModel>
    <productsCount>2147483700</productsCount>
    <productsWeight>0.1</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>
```

### Expected Result

1. 400 Bad Request
2. Delivery is impossible and calculation is not performed.

### Actual Result  

1. 200 OK, response body:
    ```
    <response name="Привезём быстро" isItPossibleToDeliver="true"
    ```

2. Delivery is possible and calculation performed.


### Attachments     

```
1. curl --location 'https://teststand.ru/fast-delivery/v3.1.1/calculate-delivery.xml' \
--header 'Content-Type: application/xml' \
--data '<InputModel>
    <productsCount>0</productsCount>
    <productsWeight>0.1</productsWeight>    
    <deliveryTime>7</deliveryTime>
</InputModel>'

---

2. curl --location 'https://teststand.ru/fast-delivery/v3.1.1/calculate-delivery.xml' \
--header 'Content-Type: application/xml' \
--data '<InputModel>
    <productsCount>-1</productsCount>
    <productsWeight>0.1</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>'

---

3. curl --location 'https://teststand.ru/fast-delivery/v3.1.1/calculate-delivery.xml' \
--header 'Content-Type: application/xml' \
--data '<InputModel>
    <productsCount>""""</productsCount>
    <productsWeight>0.1</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>'

---

4. curl --location 'https://teststand.ru/fast-delivery/v3.1.1/calculate-delivery.xml' \
--header 'Content-Type: application/xml' \
--data '<InputModel>
    <productsCount>шесть</productsCount>
    <productsWeight>0.1</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>'

---

5. curl --location 'https://teststand.ru/fast-delivery/v3.1.1/calculate-delivery.xml' \
--header 'Content-Type: application/xml' \
--data '<InputModel>
    <productsCount>2147483700</productsCount>
    <productsWeight>0.1</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>'"
```

### Environment
- URL: https://teststand.ru.
- API version: /api/v3.1.1.
- Tool: Postman 11.85.1.

#### Severity: Critical
#### Status: Open

---

## BR-019
## POST /fast-delivery/v3.1.1/calculate-delivery.xml status 200 OK for invalid productsWeight values

### Description

When sending invalid values in productsWeight:
- 0
- negative numbers
- string values
- empty value
- value exceeding INT range

The API returns 200 OK and calculates delivery, instead of returning validation error.

### Preconditions

The server is running.

### Steps to Reproduce

1. Send POST-request
/fast-delivery/v3.1.1/calculate-delivery.xml
2. Provide the empty request body (0):

```xml
<InputModel>
    <productsCount>1</productsCount>
    <productsWeight>0</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>
```
or (missing value):

```xml
<InputModel>
    <productsCount>1</productsCount>
    <productsWeight></productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>
```
or (empty value):

```xml
<InputModel>
    <productsCount>1</productsCount>
    <productsWeight>""</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>
```
or (string):

```xml
<InputModel>
    <productsCount>1</productsCount>
    <productsWeight>два</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>
```
or (value exceeding INT range):

```xml
<InputModel>
    <productsCount>1</productsCount>
    <productsWeight>2147483700</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>
```

### Expected Result

1. 400 Bad Request
2. Delivery is impossible and calculation is not performed.

### Actual Result     

1. 200 OK, response body:

    ```xml
    <response name="Привезём быстро" isItPossibleToDeliver="true">
    ```
2. Delivery is possible and calculation performed.

### Attachments  

```
1. curl --location 'https://teststand.ru/fast-delivery/v3.1.1/calculate-delivery.xml' \
--header 'Content-Type: application/xml' \
--data '<InputModel>
    <productsCount>1</productsCount>
    <productsWeight>0</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>'

2. curl --location 'https://teststand.ru/fast-delivery/v3.1.1/calculate-delivery.xml' \
--header 'Content-Type: application/xml' \
--data '<InputModel>
    <productsCount>1</productsCount>
    <productsWeight></productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>'

3. curl --location 'https://teststand.ru/fast-delivery/v3.1.1/calculate-delivery.xml' \
--header 'Content-Type: application/xml' \
--data '<InputModel>
    <productsCount>1</productsCount>
    <productsWeight>""""</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>'

4. curl --location 'https://teststand.ru/fast-delivery/v3.1.1/calculate-delivery.xml' \
--header 'Content-Type: application/xml' \
--data '<InputModel>
    <productsCount>1</productsCount>
    <productsWeight>два</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>'

5. curl --location 'https://teststand.ru/fast-delivery/v3.1.1/calculate-delivery.xml' \
--header 'Content-Type: application/xml' \
--data '<InputModel>
    <productsCount>1</productsCount>
    <productsWeight>2147483700</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>'"
```

### Environment
- URL: https://teststand.ru.
- API version: /api/v3.1.1.
- Tool: Postman 11.85.1.

#### Severity: Critical
#### Status: Open

---

## BR-021
## POST /fast-delivery/v3.1.1/calculate-delivery.xml response body missing required attribute when deliveryTime is outside working hours

### Description

When deliveryTime is outside the courier service working hours, the API returns HTTP 200, but the response body is missing the required attribute isItPossibleToDeliver.

### Preconditions

The server is running.

### Steps to Reproduce

1. Send POST-request
/fast-delivery/v3.1.1/calculate-delivery.xml
2. Provide the following request body:
```xml
<InputModel>
    <productsCount>1</productsCount>
    <productsWeight>0.1</productsWeight>
    <deliveryTime>6</deliveryTime>
</InputModel>
```

### Expected Result

1. 200 OK, response body:

    ```
    <response name="Привезём быстро" isItPossibleToDeliver="false"/>
    ```

### Actual Result  

1. 200 OK, response body:

    ```
    <response name="Привезём быстро"/>
    ```

### Attachments  

```
curl --location \
'https://teststand.ru/fast-delivery/v3.1.1/calculate-delivery.xml' \
--header 'Content-Type: application/xml' \
--data '<InputModel>
    <productsCount>1</productsCount>
    <productsWeight>0.1</productsWeight>
    <deliveryTime>6</deliveryTime>
</InputModel>'
```

### Environment
- URL: https://teststand.ru.
- API version: /api/v3.1.1.
- Tool: Postman 11.85.1.

#### Severity: Critical
#### Status: Open

---

## BR-024
## PUT /api/v1/orders/:id status 200 when string is sent instead of productsList array

### Description

When productsList is sent as a string instead of an array, the API returns 200 OK.

### Preconditions

1. The server is running.
2. A basket with id = 6 has been created.

### Steps to Reproduce

1. Send PUT-request
 /api/v1/orders/:id
2. Provide the following request body:
```json
{
  "productsList": ""
}
```

### Expected Result

1. 409 OK, response body:

    ```json
    "message": «Нет склада, способного обработать Ваш заказ»
    ```

### Actual Result 

1. 200 OK.

### Attachments  

```
curl --location --request PUT \
'https://teststand.ru/api/v1/orders/6' \
--header 'Content-Type: application/json' \
--data '{"productsList": ""}'
```

### Environment
- URL: https://teststand.ru.
- API version: /api/v3.1.1.
- Tool: Postman 11.85.1.

#### Severity: Critical
#### Status: Open

---

## BR-027
## PUT /api/v1/orders/:id status 500 when product id exceeds integer limit

### Description

Large integer overflow in product id causes 500 error instead of 409 Conflict.

### Preconditions

1. The server is running.
2. A basket with id = 2 has been created.

### Steps to Reproduce

1. Send PUT-request
 /api/v1/orders/:id
2. Provide the following request body:
```json
{
  "productsList": [
    {
      "id": 2147483948,
      "quantity": 3
    }
  ]
}
```

### Expected Result

1. 409 OK, сообщение:

    ```json
    "message": «Нет склада, способного обработать Ваш заказ»
    ```

### Actual Result    

1. 500 Internal Server Error.

### Attachments  

```
curl --location --request PUT \
'https://<host>/api/v1/orders/2' \
--header 'Content-Type: application/json' \
--data '{"productsList":[{"id":2147483948,"quantity":3}]}'
```

### Environment
- URL: https://teststand.ru.
- API version: /api/v3.1.1.
- Tool: Postman 11.85.1.

#### Severity: Critical
#### Status: Open

---

## BR-029
## PUT /api/v1/orders/:id 200 when quantity is "", 0, or null

### Description

Invalid quantity values ("", 0, null) are accepted and processed successfully.

### Preconditions

1. The server is running.
2. A basket id = 6 has been created.

### Steps to Reproduce

1. Send PUT-request
 /api/v1/orders/:id
2. Provide the following request body:
```json
{
    "productsList": [
        {
            "id": 7,
            "quantity": ""

или

           "quantity": 0

или

            "quantity": null


        }
    ]
}
```

### Expected Result

1. 409 OK, response body:

    ```json
    "message": «Нет склада, способного обработать Ваш заказ»
    ```

### Actual Result    

1. 200 OK.
2. The product is added to the basket.

### Attachments  

```
1. curl --location --request PUT 'https://teststand.ru/api/v1/orders/6' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": 7,
            ""quantity"": ""
        }
    ]
}'

2. curl --location --request PUT 'https://teststand.ru/api/v1/orders/6' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": 7,
            ""quantity"": 0
        }
    ]
}'

3. curl --location --request PUT 'https://teststand.ru/api/v1/orders/6' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": 7,
            ""quantity"": null
        }
    ]
}'
```

### Environment
- URL: https://teststand.ru.
- API version: /api/v3.1.1.
- Tool: Postman 11.85.1.

#### Severity: Critical
#### Status: Open

---

## BR-031
## DELETE /api/v1/orders/:id status 404 when deleting existing basket

### Description

Deleting an existing order returns 404 Not Found instead of 200 OK.

### Preconditions

1. The server is running.
2. A basket id = 6 has been created.

### Steps to Reproduce

1. Send DELETE-request
 /api/v1/orders/6

### Expected Result

1. 200 OK. 
2. The basket is deleted.

### Actual Result   

1. 404 Not Found.
2. The basket is not deleted.

### Attachments  

```
curl --location --request DELETE 'https://teststand.ru/api/v1/orders/6'
```

### Environment
- URL: https://teststand.ru.
- API version: /api/v3.1.1.
- Tool: Postman 11.85.1.

#### Severity: Critical
#### Status: Open