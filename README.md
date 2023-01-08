# YoutubeFetch

## _The Most elegant Youtube data fetching tool, Ever_

## Initial Setup
### Celery
To run it firstly there are a few things to note, the celery module is amazing in its functionality however the -A flag that we require sadly does not seem to work in the celery5.0 and above. Hence in this the required version is celery==4.4.7.

### Redis
For the celery message queue to operate and for celery beat to be able to communicate with the celery worker we require redis server up and running. Refer the below links for how to installs. 
https://developer.redis.com/create/windows/
https://redis.io/docs/getting-started/installation/install-redis-on-mac-os/

### Flask
Lets discuss about flask for a bit, we're using it to handle all the incoming data (from the youtube API) splitting it up and also sending it to the database. It also handles the conversion to and from json data of the api response as well as the queried data. 

### Google API key
Depending on the method you wish to use to fetch the youtube data (using the inbuilt module) or the requests library you'd need two different types of credentials or api-keys. For more details refer to the vidFetcher file.

## Running the app!
### Setting up the Environment
- Verify that redis is up and running by entering redis-server should give the 'Ready to accept connections' message
- create a virtual environment in the current directory using python -m venv venv (here the environments name is the second venv)
- Activate the virtual environment using source /venv/bin/activate in linux and mac and /venv/bin/activate.bat in windows
- Now that's done you should see a (venv) instead of the usual base. 

Install the required modules using 
```sh
pip install -r /path/to/requirements.txt
```
Give it a while to install and once done its ready to be run!

### Operating the app
To run the different parts of the application use the below steps

To observe the different celery operated tasks and the critical functionalities such as writing to the files at regular intervals refer to the commands.txt file for more the commands. Copy and paste these below commands in four seperate terminal tabs.
```sh
redis-server
```
```sh
celery beat -A app.celery --schedule /tmp/celerybeat-schedule --loglevel=INFO --pidfile=/tmp/celerybeat.pid
```
```sh
celery worker -A app.celery --loglevel=INFO
```
```sh
flask --app app/__init__.py run
```
Almost instantly commands 2 and 3 will start sending and receiving the tasks. 

The individual functionalities can be seen in vidfetcher.py and \_\_init__.py in the app folder.

Finally to test the functionality of the flask server and that it is running error free and will return the api responses go to the local host link from terminal 4 at the querydb endpoint (http://127.0.0.1:5000/querydb). You should see a result like 

```json
{
"pagination": {
"count": 1
},
"results": [
{
"Video Link": "https://youtu.be/-9P4Swmt7TI",
"title": "NUEVA Actualización de Whatsapp en 2023 💥 ¡Por fin llega esto!"
}
]
}
```

#### Adding more tasks
- To configure these tasks refer to app>tasks>tasklist.py
- To add more commands first follow the sample tasks in the above file and to add them to the celery beat refer to to celeryconfig.py and rerun command 2 and 3.


