"""
Testing module for proper response codes
Alter base url if configuration differs in your environment
"""
import pytest
import requests
from requests.exceptions import HTTPError, ConnectionError

BASE_URL = 'http://127.0.0.1:5000'

# GET
def test_get_account_valid():
    try:
        response = requests.get(f"{BASE_URL}/account/checking")
        print(response.status_code)
        assert response.status_code == 200
    except HTTPError as http_err:
        print(http_err)
    except ConnectionError as conn_err:
        print(conn_err)

def test_get_account_invalid():
    try:
        response = requests.get(f"{BASE_URL}/account/checkinggg")
        print(response.status_code)
        assert response.status_code == 404
    except HTTPError as http_err:
        print(http_err)
    except ConnectionError as conn_err:
        print(conn_err)

# POST - Create Account
def test_post_account_valid():
    try:
        response = requests.post(f"{BASE_URL}/account", json={"name":"401k"})
        print(response.status_code)
        assert response.status_code == 201
    except HTTPError as http_err:
        print(http_err)
    except ConnectionError as conn_err:
        print(conn_err)

def test_post_account_lowercase():
    try:
        name = "InVESTmeNT"
        requests.post(f"{BASE_URL}/account", json={"name":name})
        response = requests.get(f"{BASE_URL}/account/{name.lower()}")
        assert response.status_code == 200
    except HTTPError as http_err:
        print(http_err)
    except ConnectionError as conn_err:
        print(conn_err)

def test_post_account_already_exists():
    try:
        response = requests.post(f"{BASE_URL}/account", json={"name":"checking"})
        print(response.status_code)
        assert response.status_code == 400
    except HTTPError as http_err:
        print(http_err)
    except ConnectionError as conn_err:
        print(conn_err)

def test_post_account_invalid_name():
    try:
        response = requests.post(f"{BASE_URL}/account", json={"name":"checking!@#$%^&"})
        print(response.status_code)
        assert response.status_code == 400
    except HTTPError as http_err:
        print(http_err)
    except ConnectionError as conn_err:
        print(conn_err)

def test_post_account_invalid_params():
    try:
        response = requests.post(f"{BASE_URL}/account", json={"balance":500})
        print(response.status_code)
        assert response.status_code == 400
    except HTTPError as http_err:
        print(http_err)
    except ConnectionError as conn_err:
        print(conn_err)

# POST - Deposit
def test_post_deposit_valid():
    try:
        params = {"name":"checking", "amount":50}
        response = requests.post(f"{BASE_URL}/account/checking/deposit", json=params)
        print(response.status_code)
        assert response.status_code == 200
    except HTTPError as http_err:
        print(http_err)
    except ConnectionError as conn_err:
        print(conn_err)

def test_post_deposit_no_account():
    try:
        params = {"name":"checking", "amount":50}
        response = requests.post(f"{BASE_URL}/account/chekkking/deposit", json=params)
        print(response.status_code)
        assert response.status_code == 404
    except HTTPError as http_err:
        print(http_err)
    except ConnectionError as conn_err:
        print(conn_err)

def test_post_account_deposit_invalid_params():
    try:
        params = {"acct":"checking", "amt":50}
        response = requests.post(f"{BASE_URL}/account/checking/deposit", json=params)
        print(response.status_code)
        assert response.status_code == 400
    except HTTPError as http_err:
        print(http_err)
    except ConnectionError as conn_err:
        print(conn_err)

def test_post_account_deposit_not_numeric():
    try:
        params = {"account":"checking", "amount":"thirty"}
        response = requests.post(f"{BASE_URL}/account/checking/deposit", json=params)
        print(response.status_code)
        assert response.status_code == 400
    except HTTPError as http_err:
        print(http_err)
    except ConnectionError as conn_err:
        print(conn_err)

# POST - Withdraw
def test_post_withdraw_valid():
    try:
        params = {"name":"checking", "amount":10}
        response = requests.post(f"{BASE_URL}/account/checking/withdraw", json=params)
        print(response.status_code)
        assert response.status_code == 200
    except HTTPError as http_err:
        print(http_err)
    except ConnectionError as conn_err:
        print(conn_err)

def test_post_withdraw_no_account():
    try:
        params = {"name":"checking", "amount":50}
        response = requests.post(f"{BASE_URL}/account/chekkking/withdraw", json=params)
        print(response.status_code)
        assert response.status_code == 404
    except HTTPError as http_err:
        print(http_err)
    except ConnectionError as conn_err:
        print(conn_err)

def test_post_account_withdraw_invalid_params():
    try:
        params = {"acct":"checking", "amt":50}
        response = requests.post(f"{BASE_URL}/account/checking/withdraw", json=params)
        print(response.status_code)
        assert response.status_code == 400
    except HTTPError as http_err:
        print(http_err)
    except ConnectionError as conn_err:
        print(conn_err)

def test_post_account_withdraw_not_numeric():
    try:
        params = {"account":"checking", "amount":"thirty"}
        response = requests.post(f"{BASE_URL}/account/checking/withdraw", json=params)
        print(response.status_code)
        assert response.status_code == 400
    except HTTPError as http_err:
        print(http_err)
    except ConnectionError as conn_err:
        print(conn_err)

# If ALLOW_OVERDRAFT remains set to False, leave this test as is.
# If changed, comment out this test and uncomment test below.
def test_post_account_withdraw_overdraft_not_allowed():
    try:
        params = {"account":"checking", "amount":1000.00}
        response = requests.post(f"{BASE_URL}/account/checking/withdraw", json=params)
        print(response.status_code)
        assert response.status_code == 400
    except HTTPError as http_err:
        print(http_err)
    except ConnectionError as conn_err:
        print(conn_err)

# If ALLOW_OVERDRAFT set to True, use this test
# def test_post_account_withdraw_overdraft_allowed():
#     try:
#         params = {"account":"checking", "amount":1000.00}
#         response = requests.post(f"{BASE_URL}/account/checking/withdraw", json=params)
#         print(response.status_code)
#         assert response.status_code == 200
#     except HTTPError as http_err:
#         print(http_err)
#     except ConnectionError as conn_err:
#         print(conn_err)
