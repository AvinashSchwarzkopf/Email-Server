class Email:
    def __init__(self, sender, recipients, subject_line, msg):
        self.sender = sender
        self.recipients = recipients
        self.subject_line = subject_line
        self.msg = msg
        
class User_copy:
    def __init__(self, email):
        self.subject_line = email.subject_line
        self.index = 0
        self.read = False

class User:
    def __init__(self, name, server):
        self.name = name
        self.server = server
        self.user_copies = []
        self.inbox = {}
        self.server.add_user(self)

    def send(self, recipient_names, subject_line, msg):
        for name in recipient_names:
            if name not in self.server.users:
                print('Recipient ' + name + 'not found')
        else:
            email = Email(self, recipient_names, subject_line, msg)
            self.server.receive(email)

    def receive(self, email):
        for copy in self.user_copies:
            copy.index += 1
        _ = User_copy(email)
        self.inbox[_] = email
        self.user_copies.insert(0, _)

    def see_inbox(self):
        for email in self.user_copies:
            if email.read == False:
                print('|' + str(email.index) + '| UNREAD | ' + email.subject_line)
            else:
                print('|' + str(email.index) + '| ' + email.subject_line)
    
    def open(self, email_id):
        for email in self.user_copies:
            if email_id == email.subject_line or email_id == email.index:
                print('Sender: ' + self.inbox[email].sender.name)
                print('Recipients: ' + str(self.inbox[email].recipients))
                print('Subject: ' + self.inbox[email].subject_line)
                print(self.inbox[email].msg)
                email.read = True
                return
        print('Email not found in ' + str(self.name) + "'s inbox")
                
    def delete(self, email_id):
        for email in self.user_copies:
            if email_id == email.subject_line or email_id == email.index:
                del self.inbox[email]
                self.user_copies.remove(email)
                for rest in self.user_copies:
                    if rest.index > email.index:
                        rest.index -= 1
                del email
                return
        print('Email not found in ' + str(self.name) + "'s inbox")

class Server:
    def __init__(self, name):
        self.name = name
        self.users = {}
        self.storage = {}
        self.i=0

    def add_user(self, user):
        self.users[user.name] = user

    def receive(self, email):
        self.storage[self.i] = email
        print('"' + str(email.subject_line) + '"' + ' saved as #' + str(self.i) + ' in ' + str(self.name) + ' storage')
        self.i+=1
        self.server_send(email)
    
    def server_send(self, email):
        for name in email.recipients:
            self.users[name].receive(email)

def demo():
    print(">>> a = Server('Server')")
    print(">>> user1 = User('Bobby', a)")
    print(">>> user2 = User('Annie', a)")
    print(">>> user3 = User('Happy', a)")
    print(">>> user1.send(['Annie', 'Happy'], 'Greetings', 'Hello world!')")
    print('"Greetings" saved as #0 in Server storage')
    print(">>> user2.send(['Bobby', 'Happy'], 'Hey!', 'Nice to meet you!')")
    print('"Hey!" saved as #1 in Server storage')
    print(">>> user3.see_inbox()")
    print("|0| UNREAD | Hey!")
    print("|1| UNREAD | Greetings")
    print(">>> user3.open(0)")
    print("Sender: Annie")
    print("Recipients: ['Bobby', 'Happy']")
    print("Subject: Hey!")
    print("Nice to meet you!")
    print(">>> user3.open('Hey!')")
    print("Sender: Annie")
    print("Recipients: ['Bobby', 'Happy']")
    print("Subject: Hey!")
    print("Nice to meet you!")
    print(">>> user3.see_inbox()")
    print("|0| Hey!")
    print("|1| UNREAD | Greetings")
    print(">>> user3.delete(0)")
    print(">>> user3.see_inbox()")
    print("|0| UNREAD | Greetings")

print('Call "demo()" or read the README for a demonstration on how to use')