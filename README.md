# **Pelago SDET Problem**

In this challenge I am using standard python code with unittest tools. I am not using any testing tools since my knowledge about GraphQL API testing using python is very limited for now. This is really a challenge since I never actually create API test from scratch and never code with Python as well. Not only that, I just learn about GraphQL from the last Interview with Pelago.

## Test Scenario
- Verify JSON schema for all value in the Product response
- Verify JSON schema for all value in the PelagoError response
- Verify JSON schema for all value when invalid query passed
- Verify 200 status code when the request sent is successful
- Verify 400 status code when sending invalid request (wrong query)
- Verify when sending wrong productId
- Verify when sending wrong URL
- Verify when sending empty query


## Set Up and How to run
To run this test, simply clone this project or download the zip file and then unzip it to your local.

This test can be run in command line by using standard python command
`python3 main.py`

We can also run it using PyCharm IDE. Just open the project on PyCharm, then open main.py file. From there we can run single test by click play button on the left of each test, or run all by click play button on the left of pelago_test class

## Assumptions
I made some assumption for the API specification. Here is the list:
- duration is string not integer
- some field that is not provided on sample response for example shortDescription are not tested. Tried to use Introspection, but it is disabled
- latitude & longitude is string not integer
- mediaData & content JSON is not validated since I don't know the exact specifications

## Future Work
There are still many limitations and improvement that I can make for this API test. Here is some that I have in mind:
- I will research some testing tools and implement it since the current implementation is quite hard to maintain 
- Apart from testing tools, I will need to implement reporting tools as well
- Completing schema validation with maximum or minimum length for string and also maximum or minimum value for number/integer
- Completing schema validation with nullable or not nullable for each value
- The test still don't have capability to run on parallel, need to implement it in the future