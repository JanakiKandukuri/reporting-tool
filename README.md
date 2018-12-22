REPORTING TOOL :   #### Heading 4 ####

This application is a command line interface used to analyse the log data of articles in news papers. The tool answers questions like best articles, best authors and days with more error while accessing the articles web page.

-----------------------------------------------------------------
INSTALLATIONS:
We are using VM to run an SQL database server. 
Your can install [vagrant](https://www.vagrantup.com/) and [virtualbox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1), here.

******************* STEPS TO RUN THE APPLICATION *********************
1. navigate to project folder and create database using "psql -d news -f newsdata.sql"
2. install flask-wtf using "pip install flask-wtf"
NOTE: if you see error "Could not install packages due to an EnvironmentError: [Errno 13] Permission denied:"
Consider using the `--user` option i.e., "pip install --user flask-wtf".
3. run application using python reportingtool.py and it runs on port: 8000
4. Open http://localhost:8000/
5. select a question or view all to view reporting tool answers.






