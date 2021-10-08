# flask_mongo_todo_list

### <a href="https://lit-brook-98133.herokuapp.com">Try running this app here.</a>

TODO list CRUD app using Flask and Mongo DB Atlas (Cloud DBaaS for MongoDB).

## Challenges I faced
* This was my first time using NoSQL DB and initially, I was a bit confused, but I got quickly used to it and I have to say that document databases are my favorite now!
* I was receiving H12 - Request timeout error on Heroku. Fortunatelly, the solution wasn't so hard to find: If you are running Mongo's Atlas DB (Cloud DBaaS for MongoDB), but also want to deploy your app with a database on Heroku, it's necessary to allow all IP addresses to access this DB.

## Usage

* First, clone the repo:
```
git clone https://github.com/mclbdn/flask_mongo_todo_list
```
* Then, install python packages from requirements.txt:
```
pip install -r requirements.txt
```
* Set your own environment variables.
* Set your own MongoDB Atlas database and collection.
* Run `python3 main.py`.

## Screenshot
<img src="https://raw.githubusercontent.com/mclbdn/flask_mongo_todo_list/main/screenshot.png" width="400" height="600">
