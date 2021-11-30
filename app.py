"""This service is a simple HTTP API that emulates basic operations associated with
a bank account."""
from flask import Flask, request, jsonify, abort

app = Flask(__name__)
app.config["DEBUG"] = True

ALLOW_OVERDRAFT = False

accounts = [
    {"name": "checking", "balance": 50.00},
    {"name": "savings", "balance": 100.00},
    {"name": "brokerage", "balance": 2000.00}
]

# POST /account
@app.route("/account", methods=["POST"])
def create_account():
    if "name" not in request.get_json():
        return abort(400)

    acct_name = str(request.get_json()["name"]).lower()
    if not acct_name.isalnum():
        return jsonify({"message":"Invalid account name. Must be alphanumeric characters."}), 400

    for account in accounts:
        if account["name"] == acct_name:
            return jsonify({"error": "Bad Request. Account already exists"}), 400
    accounts.append({"name": acct_name, "balance": 0.00})
    return jsonify({"message": "Account created"}), 201

# GET /account/:name
@app.route("/account/<string:name>", methods=["GET"])
def get_account(name):
    for account in accounts:
        if account["name"] == name.lower():
            return jsonify(account), 200
    return abort(404)

# POST /account/:name/deposit
@app.route("/account/<string:name>/deposit", methods=["POST"])
def deposit(name):
    if "amount" not in request.get_json():
        return abort(400)
    try:
        amount = round(float(request.get_json()["amount"]), 2)
    except ValueError:
        return abort(400)

    account_name = str(name.lower().strip())
    for account in accounts:
        if account["name"] == account_name:
            account["balance"] += amount
            print(f'{account["name"]} updated with new balance of {account["balance"]}')
            return jsonify({"message": "balance updated"}, 200)
    return abort(404)

# POST /account/:name/withdraw
@app.route("/account/<string:name>/withdraw", methods=["POST"])
def withdraw(name):
    if "amount" not in request.get_json():
        return abort(400)
    try:
        amount = round(float(request.get_json()["amount"]), 2)
    except ValueError:
        return abort(400)

    account_name = str(name.lower().strip())
    for account in accounts:
        if account["name"] == account_name:
            if ALLOW_OVERDRAFT and account["balance"] - amount < 0:
                account["balance"] -= amount
            elif not ALLOW_OVERDRAFT and account["balance"] - amount < 0:
                print('Insufficient balance')
                return abort(400)
            else:
                account["balance"] -= amount
            print(f'account {account["name"]} updated balance of {account["balance"]}')
            return {"message": "balance updated"}, 200
    return abort(404)

if __name__ == "__main__":
    app.run(debug=True)
