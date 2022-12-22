import random
import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

server.login('meaniketnim@gmail.com','password')
otp = random.randrange(100000, 100000000)
message = 'OTP for login is ' + str(otp)
server.sendmail('meaniketnim@gmail.com','aniketnim1708@gmail.com',message)
server.quit()
user = int(input('Enter the OTP: '))
if (user == otp):
    print('Access granted!')
else:
    print('Access Denied!')
