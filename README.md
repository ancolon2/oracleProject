# oracleProject
# Application Title: Andrew's MX Domain App
# Author: Andrew Colon
# Create Date: Oct 1st 2019

# =============================================================================
# Installation Instructions
# =============================================================================

If Running from Python IDE (i.e I use Pycharm)

1) Unzip the contents of the application to a local directory location (i.e /Users/<YourMacUserName>/Python/OracleProject)
2) Open the project from your IDE
3) Make sure the below Project Interpreter/Packages are installed on the project

Flask
dns-batch-resolver==0.0.2
dnspython==1.16.0

4) Run the src/app.py file. You should see the below output

Serving Flask app "app" (lazy loading)
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off

5) Open a web browser and go to URL http://127.0.0.1:5000/ . This is the homepage of the application

If Running from docker

1) First make sure Docker Desktop is up and running. Instructions are here https://docs.docker.com/v17.09/docker-for-mac/install/
2) In a terminal command line pull the project from my docker hub repository

docker pull ancolon/python-domain-mx-project

3) Start and run a container from the image

docker container run -d --name provide-name -p 5000:5000 ancolon/python-domain-mx-project

4) Open a web browser and go to URL http://127.0.0.1:5000/ . This is the homepage of the application

If Running from Shell

1) Unzip the contents of the application to a local directory location (i.e /Users/<YourMacUserName>/Python/OracleProject)
2) Open a new terminal and navigate to /src directory of project
3) Execute the below commands in order

pip install -r requirements.txt
python app.py

4) You should see the below output, after which open a web browser and go to URL http://127.0.0.1:5000/ . This is the homepage of the application

MacBook-Pro-9:src mymac$ python app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


# =============================================================================
# Developer Notes
# =============================================================================

Given that I had more time to work on this project I would have done the below improvements/Enhancements

1) Added features to the UI for customizing search results (i.e Filters and checkboxes that support more format outputs such as string, list, table, etc)
2) Added database support enhancement for tracking previously searched domains using mongodb to store JSON MX record entries.
3) Would have gone a step future out of pulling MX records and will have extended the app to perform advanced search capabilities for pulling other domain specific and/or details from websites and API's
4) Setup Connexion and swagger.yml in order to create the swagger.json api for Bonus points
5) Would have completed the unit and functional testing under testing/TestApi.py
