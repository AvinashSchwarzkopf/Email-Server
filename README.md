# Email-Server
 A simple program for sending and recieving emails in a server!

 First, a server needs to be created, along with users. Users can only send emails to other users in their server.
>>> a = Server('Server')
>>> user1 = User('Bobby', a)
>>> user2 = User('Annie', a)
>>> user3 = User('Happy', a)

Users can send emails to each other. Every email sent is stored indefinitely in a server dictionary.
>>> user1.send(['Annie', 'Happy'], 'Greetings', 'Hello world!')
"Greetings" saved as #0 in Server storage
>>> user2.send(['Bobby', 'Happy'], 'Hey!', 'Nice to meet you!')
"Hey!" saved as #1 in Server storage

Users can view those emails in their inbox. The inbox shows the index and subject line of the email, either of which can be used to access the email itself.
>>> user3.see_inbox()
|0| UNREAD | Hey!
|1| UNREAD | Greetings

When a user opens an email, they access the original email, which is stored on the server.
>>> user3.open(0)
Sender: Annie
Recipients: ['Bobby', 'Happy']
Subject: Hey!
Nice to meet you!

>>> user3.open('Hey!')
Sender: Annie
Recipients: ['Bobby', 'Happy']
Subject: Hey!
Nice to meet you!

After an email has been opened, it's no longer marked as unread in the user's inbox.
>>> user3.see_inbox()
|0| Hey!
|1| UNREAD | Greetings

After reading an email, users can delete an email from their inbox. 
>>> user3.delete(0)
>>> user3.see_inbox()
|0| UNREAD | Greetings

Deleting an email moves up the index of every email that comes after it, so that the index of the most recent email is always 0 and ascends consistently. Reading and deleting emails does not, of course, affect any other users' inbox. 
>>> user1.see_inbox()
|0| UNREAD | Hey!

In the future I could add a reply feature, so that users could create threads with one another. CC and BCC are other features that could be supported. 