# MobileFactoryFanztar

A map is created in the constnats to store type, price and description of any component. We evaluate the total_price using the price stored, description is stored to display this in the response and type is used to verify the logic the each component is used only once.

Curl to run create-order:

```
curl --location --request POST 'http://127.0.0.1:8000/api/v1/create-order' \
--header 'Content-Type: application/json' \
--data-raw '{
    "components": [
        "I",
        "A",
        "D",
        "F",
        "K"
    ]
}'
```

```
Response:
{
    "status": 0,
    "message": "Success",
    "data": {
        "order_id": 39,
        "total": 142.3,
        "parts": [
            "Android OS",
            "LED Screen",
            "Wide-Angle Camera",
            "USB-C Port",
            "Metallic Body"
        ]
    }
}
```
