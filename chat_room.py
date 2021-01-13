class Person:
    def __init__(self,name):
        self.name = name
        self.chat_log = []
        self.room = None
    
    def receive(self, sender, message):
        s = f'{sender}: {message}'
        print(f'[{self.name}\'s chat session] {s}')
        self.chat_log.append(s)

class ChatRoom:
    def __init__(self):
        self.people = []
    
    def join(self,person):
        join_msg = f'{person.name} joins the chat'
        self.broadcast('room', join_msg)
        person.room = self
        self.people.append(person)
    
    def broadcast(self, source, message):
        for p in self.people:
            if p.name != source:
                p.receive(source, message)