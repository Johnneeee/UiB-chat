### Authors:

Pavel Blindheim, Johnny Nguyen, Pål Vindenes 

### Design considerations from Part A:

We decided base our project on the given “login server project” from Anja and work on from there. The problem with this given project is that the structure is bad. The two biggest problem we see with this structure is that the files are not sorted into folders and that the app.py itself can be divided into smaller files. 
A bad structure like this can become a big mess in the long run when the projects gets bigger. It will become harder and harder to keep track of where a specific code is located within the project. 

##### Structure after refactoring:

    |  app/
    |   |--__init__.py
    |   |--login_form.py
    |   |--login_management.py
    |   |--viewsButtons.py
    |   |--viewsResources.py
    |   |--viewsSites.py
    |   |
    |   |--templates/
    |   |      |--index.html
    |   |      |--login.html
    |   |      |--register.html
    |   |
    |   |--resources/
    |   |      |--favicon.ico
    |   |      |--favicon.png
    |
    |--tiny.db
    |--run.py // kjører denne
    

Everything that has to do with the app is within the app folder, except the database and the file you run to start the whole app (run.py). 
In the app folder you can see all the python files. We decided to divide views into three smaller files to make it even easier to know where to look to find the view you want. In this app folder, we decided to make two more folders, one for all resources, and one for all html files.

### Demo:

To start the application, use the "flask run" command in a terminal, if this does not work, you might have to use "export FLASK_APP=run.py" first. Then, use a browser and search for "localhost:5000". This will take you to a login site, and there is a button beneath the login page that will take you to the registration site. When registering, you should pick a username and choose a password that is atleast 12 characters long and atleast 3 digits, all users already in the database have password1234 as passwords.

You will then have to log in and you will be taken to the main page of the website. Here you can press the "see all users" button to do that, and you can send messages to these users. if you want to send the same message to multiple people for example alice and bob, write "alice, bob" in the "To" field.  

On the website you can also block/unblock users from sending you messages. You can reply to specific messages by typing the message id of the message you want to reply to in the reply field and pressing reply. You are also able to see all messages from and to you on the website. When done, you can press logout to log out of your account and get redirected to the login page.


### Features:

-   Create and login to a user.
-   Send and receive messages to and from other users in the application. 
-   Check who else is active at the moment.
-   Block other users, as well as having the option to unblock them.
-   Reply to messages that have been sent to you by inputting the id of the message you want to reply to.
-   You can search for:
    -   Keywords in older messages that you have sent or received.
    -   Users that you have sent or received messages from.
    -   A message given its id.



## Questions

### Threat model:

##### Who might attack the application?

Attackers could be someone or a group of people that want to obtain private messages between groups of people. Some attacker might want to impersonate a user (Masquerade attack) of the application in order to manipulate someone that trusts the user into doing something the attacker wants to. Information about users such as passwords and maybe even activity on the website could be points of interest for an attacker. Attackers that want to see private messages and make specific people do something might be lonely hackers while attackers interested in the general personal information stored on the website might be larger groups of organized hackers.

##### What can an attacker do?

There are countless of attacks an attacker could try, but these are probably the most relevant/probable for our application: Masquerade attacks could be done with through a compromised account for example because of a password leak or through the attacker making an account that appears similar to the real one. Attackers could try to leak the databases by sql injection attacks or use cross site scripting to upload their own code to the website that could basically do whatever the attacker wants to. Attackers could also try the man in the middle attacker where the attacker would be able to see and alter all information a user sends to the application.

##### What damage could be done (in terms of confidentiality, integrity, availability)?

The biggest damage that could be done in terms of confidentiality is all the information in the databases leaking and somehow decrypted. It could also be damaged by an attacker being able to eavesdrop on what users do on the application. Integrity could be damaged if attackers are able to alter or delete databases or any information given by the user. Availability would be damaged if some of the services of the application were available for the user. This could happen through for example a denial of service attack where the application would go down and users would not be able to access it. It could also happen through database deletion if there is no backup, making the information unavailable for the users.

##### Are there limits to what an attacker can do?

The biggest limitation to what an attacker could do with our application would probably be breaking the encrypted passwords stored in the database. The passwords are atleast 12 characters long with atleast 3 digits and they are also salted and then hashed with sha512. The only way a password could be cracked is if the attacker picks a specific hash and manages to brute-force it which wouldnt be cost efficient for the attacker, unless the password is weak and the attacker uses a dictionary attack where the dictionary contains the password.

##### Are there limits to what we can sensibly protect against?

Attacks like distributed denial of service attack are basically impossible to fully stop. Even for the largest actors in cyber-space, DDoS attacks are hard to handle and you can only prepare for it not stop it from happening and effecting your application. Also, it is very hard to stop phising attacks happening on the application. There is no good way of preventing a user from giving up sensitive information to a phising attack happening on the website. The only thing we could really do is to warn the user to not give sensitive information to someone they dont trust

### What are the main attack vectors for the application?

The main attack vectors for our application would first of all be, as mentioned, SQL injections. Being able to inject SQL queries into our application would be a major problem as any information stored in the database would be exposed to a potential attacker. Another attack that poses a great threat to our application would be Cross Site Scripting (XSS). This would cause multiple problems to both the user and the application itself. XSS could also, for example, be used to hijack cookies from users and gain access to their accounts and data. Another attack that could be used to hijack cookies is a man-in-the-middle attack.

### What should we do (or what have you done) to protect against attacks?

We have tried to prevent a couple of different attacks to our application. First, we made sure that to create an account the user must create a password that is at least 12 characters long with minimum 3 of them being a number. This was done in an attempt to make it difficult for potential hackers to brute force their way into accounts. On top of this we made it so that after 4 failed login attempts you are timed out for 2 minutes before you can try again.

For Cross Site Scripting attacks what we did was change the way inputs got rendered in the application. The code we were given used .innerHTML() to render input which renders it as HTML, which makes injecting JavaScript not very difficult so we changed this to .innerText(). This results in the input being rendered only as text and not HTML. We also stripped inputs from all characters excluding letters and numbers to prevent SQL injections.

### What is the access control model?

The access control model we use in our app is Attribute-Based Access Control (ABAC). This is the model where “subject request to perform operations on objects are granted or denied based on assigned attributes of the subject, assigned attributes of the object, environment conditions, and a set of policies that are specified in terms of those attributes and conditions”[(Owasp/Authorization).](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
Each user in our database has a set of attributes they can perform, as in reading their own and sending messages, and blocking and unblocking other users. They can also lose their attribute to send a message to a specific user if this user has blocked them.

### How can you know that you security is good enough?

Traceability is important when you try to find out if your security is good enough or not. If your security is weak, the website or the database can be modified and get destroyed. When we have good traceability we can restore the damage and identify who, what and when the damage was caused.

We trace a couple of things in our project. First, use Git to work on this project. For every changes to the project in Git, the change is traced with the user and the time of the commit, and for every message sent in our website it gets logged with who it was sent from, who it was sent to and the timestamp of the message. 

