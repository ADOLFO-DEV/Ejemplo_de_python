  class user:
    name = None
    email = None
    def send_email(self):
        if self.email is not None:
            print("sendingemail:"+self.email)
        else:
                print("Error")

    def __init__(self,name,email):
        self.name = nameself.email = email

class student (user):
id = Nonedef __init__(self,
    name = none,
    email = none,
    ):

        super().__init__(name,email)
        self.id = uuid.uuid4()
        
