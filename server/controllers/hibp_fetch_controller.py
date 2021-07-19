from flask import Blueprint, Flask, Response
import sys
import http.client
import requests
from services.hibp_headers import headers


hibp_fetch_blueprint = Blueprint("hibp_fetch", __name__)

@hibp_fetch_blueprint.route("/hibp_fetch/<email>", methods=["GET"])
def hibp_info(email):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}?truncateResponse=false"
    response = requests.get(url, headers=headers)
    return Response(response.content, response.status_code, headers)

@hibp_fetch_blueprint.route("/hibp_fetch/no_detail/<email>", methods=["GET"])
def hibp_info_no_detail(email):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    response = requests.get(url, headers=headers)
    return Response(response.content, response.status_code, headers)