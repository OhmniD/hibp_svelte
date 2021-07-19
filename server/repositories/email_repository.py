from flask import jsonify
from db.run_sql import run_sql
import sys

from models.email import Email
from controllers.hibp_fetch_controller import hibp_info

def save(email):
    hibp_info = hibp_info(email)
    num_of_breaches = len(hibp_info)
    sql = "INSERT INTO emails(email, num_of_breaches) VALUES (%s, %s) RETURNING id"
    values = [email.email, email.num_of_breaches]
    result = run_sql(sql, values)

    email.id = result[0]['id']

def select_all():
    emails = []

    sql = "SELECT * FROM emails ORDER BY email ASC"
    results = run_sql(sql)

    for row in results:
        email = Email(row['email'], row['num_of_breaches'], row['id'])
        emails.append(vars(email))

    return emails

def update(email):
    sql = "UPDATE emails SET (email, num_of_breaches) = (%s, %s) WHERE id = %s"
    values = [email.email, email.num_of_breaches, email.id]
    run_sql(sql, values)