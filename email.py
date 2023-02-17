import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('devananth511@gmail.com','Deva@5112002')
server.sendmail('mjeevanantham04@gmail.com','mjeevanantham04@gmail.com','Message Alert!!!!')
print("email sent")