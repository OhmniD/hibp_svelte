from flask import Blueprint, Flask, request, json, jsonify
import sys

from models.email import Email
import repositories.email_repository as email_repository

emails_blueprint = Blueprint("emails", __name__)

@emails_blueprint.route("/emails", methods=["GET"])
def all_emails():
    emails = email_repository.select_all()
    return jsonify(emails)
    
@emails_blueprint.route("/emails/<id>", methods=["POST"])
def update_email(id):
    request_data = request.get_json(silent=True)

    email = request_data['email']
    num_of_breaches = request_data['num_of_breaches']
    email_record = Email(email, num_of_breaches, id)

    email_repository.update(email_record)

    return "Success"