# python_flask_banking_api
## Please view the readme.txt file for full explanation of service. This is the readme.md file for the repository
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

