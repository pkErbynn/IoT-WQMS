import smtplib

emailAddress = 'iotwqms2019@gmail.com'
emailPassword = 'iotaquaaid2019'

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    print("structuring mail...")
    smtp.login(emailAddress, emailPassword)


    subject = 'wqms test 2'
    body = 'is the water clean'

    msg = f'Subject: {subject} \n\n {body}'
        
    print("sending mail ...")
    smtp.sendmail(emailAddress, 'john.erbynn@gmail.com', msg)
    print("email sent successfully")

