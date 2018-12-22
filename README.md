# REPORTING TOOL

This application is a command line interface used to analyse the log data of articles in news papers. The tool answers questions like best articles, best authors and days with more error while accessing the articles web page.

-----------------------------------------------------------------
## INSTALLATIONS:
* We are using VM to run an SQL database server. You can install [vagrant](https://www.vagrantup.com/) and [virtualbox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1), here.
* Install git bash from https://git-scm.com/downloads based on your OS. (For windows git provides git bash to do unix shell).
-------------------------------------------------------------------
### STEPS TO CONFIGURE VM
1. Clone this project.
2. Navigate to downloaded project folder in your system using terminal/ git bash for windows.
3. In project you will find a vagrant file which is used to configure VM. 
#### NOTE: (vagrant file is important to configure/interact with VM).
4. Follow below steps to setup and use VM.
   * Start up virtual machine using vagrant up.
   * Once up to log into newlys installed VM use vagrant ssh.

#### RUN APPLICATION
1. There is newsdata.sql file which consists of news database. Once logged in create database using "psql -d news -f newsdata.sql"
2. Use "psql news"  command to connect to news database.
3. Open new terminal window navigate to project folder and perform step 4 from above to connect VM.
4. run "python reportingtool.py" command to see this reporting tool up and running.






