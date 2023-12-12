# Using FastAPI

To Start the server for FastAPI run the following command:
```bash
uvicorn main:app --reload
```

test with this curl command to insert an item and retrive entire list:
```bash
curl -X POST -H "Content-Type: application/json" "http://127.0.0.1:8000/items?item=apple"
```
To test get an item by id, use this cURL command:

```bash
curl -X GET -H "Content-Type: application/json" "http://127.0.0.1:8000/items/1"
```

To test with pydantic models use this Curl command:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"text": "apple"}' "http://127.0.0.1:8000/items"

```