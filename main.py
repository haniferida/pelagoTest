# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import requests
import json
from jsonschema import validate

numOfTest = 0
numOfPass = 0
numOfFail = 0

query = "query product($productId: String!) {\n product(productId: $productId) {\n ... on Product {\n productId\n " \
        "productName\n destinationId\n mediaData\n cancellationType\n cancellationWindow\n minGroupSize\n duration\n " \
        "openDateTicket\n collectPhysicalTicket\n confirmationType\n voucherType\n guideLanguages\n priceRangeFrom\n " \
        "priceRangeTo\n latitude\n longitude\n address\n }\n ... on PelagoError {\n errorMessage\n " \
        "code\n }\n }\n} "

productSchema = {
    "type": "object",
    "properties": {
        "productId": {"type": "string"},
        "productName": {"type": "string"},
        "destinationId": {"type": "string"},
        "cancellationType": {"type": "string"},
        "cancellationWindow": {"type": "number"},
        "minGroupSize": {"type": ["number", "null"]},
        "duration": {"type": "string"},
        "openDateTicket": {"type": "boolean"},
        "collectPhysicalTicket": {"type": "boolean"},
        "confirmationType": {"type": "string"},
        "voucherType": {"type": "string"},
        "guideLanguages": {"type": "string"},
        "priceRangeFrom": {"type": "number"},
        "priceRangeTo": {"type": "number"},
        "latitude": {"type": "string"},
        "longitude": {"type": "string"},
        "address": {"type": "string"},
    },
}


def test_first():
    response = requests.post("https://traveller-core.dev.pelago.co/graphql",
                             json={'query': query, "variables": {"productId": "p417p"}})
    # print(response.json())
    response_body = response.json()
    assert response.status_code == 200
    # assert response_body['data']['product']['destinationId'] == "singapore", "destinationId is not singapore"
    productResponse = response_body['data']['product']
    isValid = validate(instance=productResponse, schema=productSchema)
    print("Test first is passed")


if __name__ == '__main__':
    test_first()
