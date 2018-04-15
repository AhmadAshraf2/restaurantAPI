# RESTAURANT API


## SUMMARY

The API is built using REST standard and contains the below mentioned endpoints

--> View single restaurant.
--> View all restaurants.
--> Create a new restaurant.
--> Updtae an existing restaurant.
--> Delete a restaurant.

--> Authentication
	The view endpoints are publicly available where as the rest of the endpoints need authentication.
	A user is authenticated based upon a auth token. whenever a user is created an auth token for that user is auto genertaed using user information.
	Djangos User model is used. which by default has 3 types of users superuser, staff and normal. 

--> Authorization
	Read (view) endpoints are publicly available.
	Create endpoint is available to any registered user.
	Update endpoint is available to any registered user.
	Delete endpoint is only accessible to admin users.

	Every role (user) has a set of permissions based on which it is allowed access to an endpoint.
 

## TOOLS USED.

API is built using Django DRF, and PostgreSQL.

Docker containers are used for development environment.

Swagger has been configured with Django to access and test the endpoints.


## ASSUMPTIONS AND IMPROVEMENTS:

User module is needed for authorization and authentication. I assumed that exposing user endpoints are beyond the scope of this task. Hence the users are to be added using Django admin panel (localhost:8000/admin).

Also is is assumed that the functionality of sharing a token with the client is already in place. For simplicity I directly read the token from admin panel.

For the sake of this assignment I have used 0.0.0.0:8000 to run the server but in production these values should be passed along as environment variables.

Test cases for this assignment only check the basic functionality. Currently tests only assert on the response code. These can be improved, where we can also assert upon the response data to make these tests more rigid.


## HOW TO RUN:

Go to the RestaurantAPi folder and run the below command to start docker containers.

-->   Docker-compose up --build

Docker-compose uses 3 files (placed in /restaurantAPI/dockers folder) to setup the docker containers. DockerFile contains command to setup django_container. 
After the container is setup, we need to make migrations. Bash script entrypoint.sh contains the commands to migrate, create django superuser and start the server.

--> Superuser username = ahmad (same for postgres user)
--> Superuser password = abc123456 (same for postgres user)

A problem arises where the django_container gets ready before the postgres container and runs the migration commands before the database is ready. 
So to solve this, Wait_for_it.sh bash file ensures that the migrations are run after the database is up and ready to entertain requests.

After starting the dockers containers, move to the browser on your host machine and go to the below URL.

--> localhost:8000/docs 

Please note that I am using localhost not 0.0.0.0 as IP address. 
We are forwarding port from dokcer container to host machine, because of this swagger will start throwing a warning (cannot read from 0.0.0.0 but will work perfectly). Using localhost will get rid of this warning message.


PUT, POST, DELETE endpoints require authentication. To authenticate a user in swagger, we have to add authentication token in our request.
A <auth_token> is automatically generated for every new user. <auth_token> can be viewed via admin panel (localhost:8000/admin) or directly from the DB. 

After acquiring <auth_token>, go to the top right corner. Press "Authorize" button and add the below text (Token word included).

--> Token <auth_token> 

Now every request sent via swagger will contain the auth token unless user is logged out of swagger. 



