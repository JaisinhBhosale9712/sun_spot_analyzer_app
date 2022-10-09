1.) To Run or Use the app there are two ways -

A.) The Swaggerhub way using deployed application

-   Use the deployed application to AWS
    url - http://sunspotanalyzer-env.eba-7wpjmwpx.eu-central-1.elasticbeanstalk.com/sun-spot-analyser-api/

-   You can easily test all routes using swaggerhub -
    url - https://app.swaggerhub.com/apis/JAISINHBHOSALE/Sun_Spot_Analyzer/1.0.0
    Or you can simply copy the OAS file from project directory to your swagger account and test. 
    Please check the server selected on swaggerhub, i have disabled auto-mocking, but just to be on      safer side.
    Please note the database has first entry with id 1 already stored, could be used for testing


B.) Running docker with testing using postman
-   Start docker container with following steps
    - Run the docker daemon
    - Run command "docker build --tag python-docker ." from project directory
    - Run command "docker-compose up" from project directory
   
-   Use the Postman workspace -
    url - https://www.postman.com/orange-firefly-598387/workspace/sun-spot-analyser/overview
    All routes can be found in collection section as "GET", "POST" and "DELETE" collection.


2.) Unit testing -
    - Installing dependancies from requirements.txt
     Run views/unit_tests.py file.

