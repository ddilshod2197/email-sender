import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailSender:
    def __init__(self, host, port, from_addr, password):
        self.host = host
        self.port = port
        self.from_addr = from_addr
        self.password = password

    def send_email(self, to_addr, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.from_addr
        msg['To'] = to_addr
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP(self.host, self.port)
        server.starttls()
        server.login(self.from_addr, self.password)
        text = msg.as_string()
        server.sendmail(self.from_addr, to_addr, text)
        server.quit()

# Misol foydalanish:
sender = EmailSender('smtp.gmail.com', 587, 'your_email@gmail.com', 'your_password')
sender.send_email('to_email@example.com', 'Subject', 'Hello, world!')
```

Kodni ishlatish uchun quyidagilar kerak:

1. `host` - SMTP server manzili (masalan, `smtp.gmail.com`).
2. `port` - SMTP porti (masalan, 587).
3. `from_addr` - Email manzili, keyingi emailni yuborish uchun (masalan, `your_email@gmail.com`).
4. `password` - Email parol (masalan, `your_password`).
5. `to_addr` - Email manzili, keyingi emailni qabul qilish uchun (masalan, `to_email@example.com`).
6. `subject` - Email mavzusi (masalan, `Subject`).
7. `message` - Email matni (masalan, `Hello, world!`).
