"""

This is an Email transaction module
Created on Sun, 25th of May 2019
Authors: John Pk Erbynn, Josiah Nii Kortey, Isaac Agyen Duffour

This module handles the alert of any wrong data which is collected and send as email (gmail)
Data can be sent to multiple emails concurrently ie. addresses in lists
Uses Simple Mail Transfer Protocol (SMTP)

Usage:
    Parse the json data as an argument unto the send_mail attribute as 
    send_mail(data)

    Expected data should be in the format;

    data = {
        "temperature": 30,
        "turbidity": 7,
        "ph": 2,
        "water_level": 23
    }

    run <python mail.py> ... Done! enjoy :)

"""

import smtplib
from email.message import EmailMessage


def send_mail(sensor_data):
    print("Error found while scanning data readings.\nSending email ...")
        
    try:
        email_address = 'iotwqms2019@gmail.com'
        email_password = 'iotaquaaid2019'
        email_subject = "WQMS Alert ! :)"
        to_email = ['john.erbynn@gmail.com', 'josiahkotey13@gmail.com', 'izagyen96@gmail.com']
        # to_email = 'john.erbynn@gmail.com'

        print("Composing mail ...")

        # creating object
        msg = EmailMessage()

        # email composition
        msg['Subject'] = email_subject
        msg['From'] = email_address
        msg['To'] = to_email

        # This identifies specific data being recorded wrongly
        for key, value in data.items():
            if key == "temperature":
                if (value < 23) | (value > 34) :
                    if value < 23:
                        status = 'Water cold'
                    else:
                        status = 'Water hot'
                    check_error = f" \nTemperature out of range({status}): {value} °C "
                    print(check_error)
            if key == "turbidity":
                if (value < 0) | (value > 5) :
                    check_error = f" \nTurbidity out of range(Suspended particles present): {value} NTU "
                    print(check_error)
            if key == "ph":
                if (value < 4) | (value > 10) :
                    if value < 4:
                        status = 'acidic water'
                    else:
                        status = 'basic water'
                    check_error = f" \npH out of range({status}): {value} "
                    print(check_error)
            if key == "water_level":
                if (value < 5) | (value > 27) :
                    if value < 5:
                        status = 'water too low'
                    else:
                        status = 'water overflow'
                    check_error = f" \nWater_level out of range({status}): {value} cm "
                    print(check_error)
        
        # main content of email
        msg.set_content( f'Data collected... \n\n {sensor_data} \n\n {check_error}' )
        
        # logging in and sending email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)
            print("Email sent successfully !!")

    # runs if error occurs while trying to send email
    except Exception as err:
        print(f"Oops!!...Failed to send mail. {err}")



# send_mail(data)

