# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import jsonschema
import requests
from jsonschema import validate
import unittest

query = "query product($productId: String!) {\n product(productId: $productId) {\n ... on Product {\n productId\n " \
        "productName\n destinationId\n cancellationType\n cancellationWindow\n minGroupSize\n duration\n " \
        "openDateTicket\n collectPhysicalTicket\n confirmationType\n voucherType\n guideLanguages\n priceRangeFrom\n " \
        "priceRangeTo\n latitude\n longitude\n address\n }\n ... on PelagoError {\n errorMessage\n " \
        "code\n }\n }\n} "

wrongQuery = "query product($productId: String!) {\n product(productId: $productId) {\n ... on Product {\n productId\n " \
        "productName\n destinationId\n wrongType\n cancellationWindow\n minGroupSize\n duration\n " \
        "openDateTicket\n collectPhysicalTicket\n confirmationType\n voucherType\n guideLanguages\n priceRangeFrom\n " \
        "priceRangeTo\n latitude\n longitude\n address\n }\n ... on PelagoError {\n errorMessage\n " \
        "code\n }\n }\n} "

productSchema = {
    "type": "object",
    "required": [
        "productId",
        "productName",
        "destinationId",
        "cancellationType",
        "cancellationWindow",
        "minGroupSize",
        "duration",
        "openDateTicket",
        "collectPhysicalTicket",
        "confirmationType",
        "voucherType",
        "guideLanguages",
        "priceRangeFrom",
        "priceRangeTo",
        "latitude",
        "longitude",
        "address",
    ],
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

pelagoErrorSchema = {
    "type": "object",
    "required": ["errorMessage", "code"],
    "properties": {
        "errorMessage": {"type": "string"},
        "code": {"type": "number"},
    },
}


class pelago_test(unittest.TestCase):

    # Verify JSON schema for all value in the successful response
    def test_json_schema_successful_response(self):
        response = requests.post("https://traveller-core.dev.pelago.co/graphql",
                                 json={'query': query, "variables": {"productId": "p417p"}})
        response_body = response.json()
        productResponse = response_body['data']['product']
        validate(instance=productResponse, schema=productSchema)

    # Verify JSON schema for all value in the successful response but got PelagoError
    def test_json_schema_successful_response_pelago_error(self):
        response = requests.post("https://traveller-core.dev.pelago.co/graphql",
                                 json={'query': query, "variables": {"productId": "1"}})
        response_body = response.json()
        productResponse = response_body['data']['product']
        validate(instance=productResponse, schema=pelagoErrorSchema)

    # Verify 200 status code when the request sent is successful
    def test_status_code_200(self):
        response = requests.post("https://traveller-core.dev.pelago.co/graphql",
                                 json={'query': query, "variables": {"productId": "p417p"}})
        response_body = response.json()
        assert response.status_code == 200
        assert response_body['data']['product']['productId'] == "p417p"

    # Verify 400 status code when sending invalid request (wrong query)
    def test_status_code_400(self):
        response = requests.post("https://traveller-core.dev.pelago.co/graphql",
                                 json={'query': wrongQuery, "variables": {"productId": "p417p"}})
        assert response.status_code == 400

    # Verify when sending wrong productId
    def test_wrong_productID(self):
        response = requests.post("https://traveller-core.dev.pelago.co/graphql",
                                 json={'query': query, "variables": {"productId": "wrongProduct"}})
        response_body = response.json()
        assert response_body['data']['product']['errorMessage'] == "wrongProduct product not found"
        assert response_body['data']['product']['code'] == 404


if __name__ == '__main__':
    unittest.main()
