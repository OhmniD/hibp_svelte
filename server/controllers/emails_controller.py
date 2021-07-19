from flask import Blueprint, Flask, request, json, jsonify, redirect
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

@emails_blueprint.route("/emails", methods=["POST"])
def create_email():
    form_data = request.form

    email = form_data['email']
    email_record = Email(email)

    email_repository.save(email_record)

    return redirect('http://localhost:5000')