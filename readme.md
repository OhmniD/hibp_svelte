# HIBP Svelte App

### Synopsis

This app was created to try and learn a bit more about the Javascript framework Svelte. It allows you to add a list of e-mail addresses that will be dynamically updated on page load to show if that e-mail address has been included in any publically available data breaches, using data from the haveibeenpwned.com API.

It was built using Svelte for the front end, and Flask with PostgreSQL for the back end. It also makes use of the excellent Svelte Modal from https://github.com/flekschas/svelte-simple-modal

### Usage

 #### Server
* Obtain an API key from https://www.haveibeenpwned.com
* Install Python 3, PostgreSQL and pip
* Install flask - `pip3 install flask`
* Install Requests - `pip3 install requests`
* Download/clone the project and in `./server/services` rename `hibp_headers.template.py` to `hibp_headers.py`
* In that file, insert your API key and give your the app a unique name so the HIBP API can identify it
* From your terminal, type `createdb hibp_email` to create the required database
* Navigate to `./server/db` and type `psql -d hibp_email -f db/hibp_email.sql` to create the required table in the `hibp` database
* Navigate to `./server` and execute `flask run` to start the server
* Verify it is accesible in a browser by going to `http://localhost:8000/emails`

 #### Client
* Install Node.js and NPM
* In your terminal, navigate to `./client` and run `npm install`
* Run `npm run dev` to start the client
* Verify it is accesible in a browser by going to `http://localhost:5000`

