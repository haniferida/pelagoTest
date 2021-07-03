# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import requests

query = "query product($productId: String!) {\n product(productId: $productId) {\n ... on Product {\n productId\n " \
        "productName\n destinationId\n shortDescription\n cancellationType\n cancellationWindow\n minGroupSize\n " \
        "openDateTicket\n collectPhysicalTicket\n confirmationType\n voucherType\n priceRangeFrom\n " \
        "priceRangeTo\n latitude\n longitude\n address\n __typename\n }\n ... on PelagoError {\n errorMessage\n " \
        "code\n __typename\n }\n __typename\n }\n} "


def test_first():
    response = requests.post("https://traveller-core.dev.pelago.co/graphql",
                             json={'query': query, "variables": {"productId": "p417p"}})
    # print(response.json())
    response_body = response.json()
    assert response.status_code == 200
    assert response_body['data']['product']['destinationId'] == "singapore", "destinationId is not singapore"


if __name__ == '__main__':
    test_first()
