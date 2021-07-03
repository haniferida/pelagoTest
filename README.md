# **Pelago SDET Problem**

In this challenge I am using standard python code with unittest tools. I am not using any testing tools since my knowledge about GraphQL API testing using python is very limited for now. This is really a challenge since I never actually create API test from scratch and never code with Python as well. Not only that, I just learn about GraphQL from the last Interview with Pelago.

## Test Scenario
- Verify JSON schema for all value in the successful response
- Verify JSON schema for all value in the successful response but got PelagoError
- Verify JSON schema for all value in the unsuccessful response
- Verify 200 status code when the request sent is successful
- Verify 400 status code when sending invalid request (wrong query)
- Verify when sending wrong productId


## Set Up and How to run
This test can be run by using standard python command
`python3 main.py`

We can also run it using PyCharm IDE. Just open the project on PyCharm, then open main.py file. From there we can run single test by click play button on the left of each test, or run all by click play button on the left of pelago_test class

## Assumptions
I made some assumption for the API specification. Here is the list:
- duration is string not integer
- no shortDescription in sample response so not testing it
- latitude & longitude is string not integer

## Future Work
There are still many limitations and improvement that I can make for this API test. Here is some that I have in mind:
- I will research some testing tools and implement it since the current implementation is quite hard to maintain 
- Apart from testing tools, I will need to implement reporting tools as well
- Completing schema validation with maximum or minimum length for string and also maximum or minimum value for number/integer
- Completing schema validation with nullable or not nullable for each value
- The test still don't have capability to run on parallel, need to implement it in the future