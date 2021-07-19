from flask import Blueprint, Flask
import sys
import http.client
from services.hibp_headers import headers

hibp_fetch_blueprint = Blueprint("hibp_fetch", __name__)

@hibp_fetch_blueprint.route("/hibp_fetch/<email>", methods=["GET"])
def hibp_info(email):
    conn = http.client.HTTPSConnection("haveibeenpwned.com")
    payload = ''
    conn.request("GET", f"/api/v3/breachedaccount/{email}/?truncateResponse=false", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data

@hibp_fetch_blueprint.route("/hibp_fetch/no_detail/<email>", methods=["GET"])
def hibp_info_no_detail(email):
    conn = http.client.HTTPSConnection("haveibeenpwned.com")
    payload = ''
    conn.request("GET", f"/api/v3/breachedaccount/{email}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data