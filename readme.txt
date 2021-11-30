Bank Account API 

This service is a simple HTTP API that emulates basic operations associated with
a bank account. 

Flask is utilized as the main library to implement this API, due to it being lightweight
while also feature rich. The Content-Type header for the application is
defined as application/json.

The app.py file is where the each of the endpoint code is contained for simplicity.
See the Endpoints diagram for the endpoint, its params, and response codes.

Each endpoint fuction defines the permissible methods and internally checks
the included parameters in the request body. Internal logic determines the 
validity of the requests and returns the corresponding HTTP status code.

ALLOW_OVERDRAFT:bool - this constant emulates the real-world ability to overdraft from an 
account. Though inadvisable due to high fees (no penalties in this API because I want to be nice),
it seemed wise to include this functionality. The constant defaulted to False, but by flipping it to True, 
a negative balance is allowed when withdrawing funds.

accounts:list - the data structure to store all account data is a list of accounts
consisting of individual dictionaries. 3 entries are already in place for testing. 
The dictionaries contain "name" and "balance"keys. 

While a list structure like this is not the most performant when searching for 
an internal key within the dict at each index, the collection is not large enough
to necessitate a faster data structure.  Linear time is not really a problem in this case.


Endpoints
=========
GET /account/:name
Response Body Params - "name", "amount"
200 - OK
404 - Not Found

POST /account
201 - Created
400 - Bad Request

POST /account/:name/deposit
Request Body Params - "amount"
200 - OK
404 - Not Found
400 - Bad Request

POST /account/:name/withdraw
Request Body Params - "amount"
200 - OK
404 - Not Found
400 - Bad Request


Assumptions & Constraints
=========================
Some situations are not described in the instructions and I wanted to be sure 
to explain some of the assumptions I made and how I handled certain edge cases:

- I have opted not to create any HTML templates for this exercise. They were not listed
and since this appears to be a purely backend exercise, I didn't see it valuable.
- I used the round() function to limit the floats to 2 decimal places
when processed after being passed in as part of the request body. 
This emulates cents in standard currency calculations.
- I have converted account names to lower case and limited account names to 
alphanumeric characters. If the account name is not valid, a 400 Bad Request is returned.
- If an account already exists, a 400 Bad Request is returned with error message. This could
work like some of the other error messages returning `abort(<err_code>)`, but for some of these
minor errors, I preferred a more explicit response returning `jsonify({"msg":"msg"}), err_code`. 
- Instead of using a more complex implementation of an argument parser or module for
stricter type checking of request body arguments, I am simply checking if the
named parameter exists and checking its validity. This made sense given the 
simple nature of this API and no database connection. My preferred argument parser
would be flask-restful, but it unnecessarily abstracted the handling of the endpoints.
- No class-based schemas were defined for each account. I felt this would be overkill
and it was easier to use a list of dictionaries for accounts and balances.
- The API code is within a single file and not abstracted out, except for the test module. 
For a lightweight API like this, splitting functionality is still possible, but didn't seem
like it would make anything clearer.


Setup
=====
While the dependencies for this service can be installed globally via pip/pip3, this 
project implements Pipenv to avoid the common issues associated with Python environment
management. Flask, Pytest and requests are the only needed modules, which are often globally installed.

See Pipenv documentation for more details: https://pipenv.pypa.io/en/latest/basics/

Instructions:
If pipenv is not installed, use `pip install pipenv` to install.
Run `pipenv install`. The contained Pipfile.lock and Pipfile store the dependencies
for the service and the proper packages will be downloaded and installed with this command.
Activate the Pipenv shell with `pipenv shell`

Inside the folder with the service, run the following two shell commands.
This sets FLASK_APP to app.py and also sets the application to debug mode:

export FLASK_APP=app.py
export FLASK_ENV=development

Run the command `python app.py` (or `flask run`)

The default port number is 5000 and the base url for the service is http://127.0.0.1:5000/ 


Testing
=======
tests.py includes a collection of 16 tests to verify API functionality using the pytest and requests modules.
Run `pyest tests.py` to initiate the test suite.

Alternatively, one could use curl. Below are a few example curl commands that could be used.

curl -X POST -H "Content-Type: application/json" -d '{"name":"401k"}' http://127.0.0.1:5000/account/
curl -X POST -H "Content-Type: application/json" -d '{"amount":50}' http://127.0.0.1:5000/account/401k/deposit
curl http://127.0.0.1:5000/account/401k
curl -X POST -H "Content-Type: application/json" -d '{"amount":25}' http://127.0.0.1:5000/account/401k/withdraw
curl http://127.0.0.1:5000/account/401k

curl -X POST -H "Content-Type: application/json" -d '{"amount":50}' http://127.0.0.1:5000/account/checking/deposit
curl -X POST -H "Content-Type: application/json" -d '{"amount":10000}' http://127.0.0.1:5000/account/checking/withdraw
curl http://127.0.0.1:5000/account/checking
