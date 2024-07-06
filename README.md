# CatastroBuddy-Backend

Backend for CatastroBuddy, a service to upload household item records in case of catastrophe. Go to https://github.com/DevonSchwartz/CatastroBuddy-Frontend to set up the frontend of the web application

The backend REST API was built with [Flask](https://flask.palletsprojects.com/en/3.0.x/), a Python web framework. The api will interact with a [MongoDB](https://www.mongodb.com/) server.

## Setting Up MongoDB
0. If you do not have a MongoDB server installed, follow the instructions to install the community edition https://www.mongodb.com/try/download/community
1. Download either the [MongoDB GUI](https://www.mongodb.com/try/download/compass) or the [MongoDB Shell](https://www.mongodb.com/try/download/shell)
2. Start a mongodb instance with `sudo systemctl start mongod`
3. Run `sudo systemctl status mongod` to verify the server is running. The default port is 27017

## Setting Up REST API
Clone the repository and cd into CatastroBuddy-Backend
0. If you do not already have Python, install Python for your local machine https://www.python.org/downloads/
1. If you do not already have pipenv, run `pip install pipenv`
2. Run `pipenv install` to install dependencies used in the backend into your virtual environment
3. Run `pipenv shell` to run PATH commands created by the dependencies
4. Change MONGO_LOCAL_PORT to what your local port is
5. Run `flask run` in your pipenv shell to start the app.
