from flask import Blueprint, Flask, request, json, jsonify, redirect, Response
import sys
import json

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

    return request_data

@emails_blueprint.route("/emails", methods=["POST"])
def create_email():
    request_data = request.get_json(silent=True)

    email = request_data['email']
    email_record = Email(email)

    save = email_repository.save(email_record)
    return json.dumps(save.__dict__)

@emails_blueprint.route("/emails/<id>/delete", methods=["GET"])
def delete_email(id):
    email_repository.delete(id)
    return redirect('http://localhost:5000', 301)