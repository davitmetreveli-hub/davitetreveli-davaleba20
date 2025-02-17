class mailsender:
    def send_mail(self, email):
        print(f"ყვენი მეილი გაიგზევნა ამ მისამართზე: {email}")
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
class Friend(Contact, mailsender):
    def __init__(self, name, phone, email):
        super().__init__(name, phone)
        self.email = email
    def send_mail(self):
        super().send_mail(self.email)
class Family(Contact,mailsender):
    def __init__(self, name, phone, email, date):
        super().__init__(name, phone)
        self.email = email
        self.date = date
    def send_mail(self):
        super().send_mail(self.email)
