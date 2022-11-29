import requests

response = requests.post("https://petstore.swagger.io/v2/pet", json={
  "id": 228,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "python",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)


response = requests.put("https://petstore.swagger.io/v2/pet", json={
  "id": 228,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "python",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})



response = requests.get("https://petstore.swagger.io/v2/pet/228", json={
  "id": 228,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "python",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})