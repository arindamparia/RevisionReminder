# RevisionReminder

It is an Application developed using html,css,javaScript, Node.js, Express.js, MongoDB and Python, which is going to help in revising concepts. Whenever you are reading somthing online and you want to revise that after some time you can 
add the url, article name and the date(when you want to revise) in the extension and it will send mail to you consisting  topic name and url on the 
mentioned date so that you can revise.


**Basically this application has two parts:**

1)After filling the form the data will submit in mongodb database.


2)There is a Python Script which will check the database in every 24 hour and when the date is matched it will send mail and also delete that data from database.

