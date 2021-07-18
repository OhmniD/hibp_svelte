from flask import Blueprint, Flask, request, json, jsonify
import sys

from models.email import Email
import repositories.email_repository as email_repository

emails_blueprint = Blueprint("emails", __name__)

@emails_blueprint.route("/emails", methods=["GET"])
def all_emails():
    emails = email_repository.select_all()
    return jsonify(emails)
    