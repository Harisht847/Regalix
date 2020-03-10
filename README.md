# Regalix
Regalix projext

REST APIs with Flask and Python

code folder is divided into models and resouces folder

migrate.py file is migration file for this app.
 
 python migrate.py db init
 python migarate.py db migrate
 
  

End points:
1.http://localhost:5000/item/<string:name>
verbs: Get, Post, Delete, Put

2.http://localhost:5000/items  <--- to view all the books
 verb: Get
 
3. http://localhost:5000/userregister  <-- register the user
Verb : Post

4. http://localhost:5000/auth <--- creates token for authentication
   verb : Get
  
