from flask import Flask, render_template
from flask_cors import CORS

from controllers.hibp_fetch_controller import hibp_fetch_blueprint
from controllers.emails_controller import emails_blueprint

app = Flask(__name__)
CORS(app)

app.register_blueprint(hibp_fetch_blueprint)
app.register_blueprint(emails_blueprint)


@app.route('/')
def main():

    return render_template('index.html')

if __name__ == '__main__':
    app.run()