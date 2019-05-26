"""

This is an Email transaction module
Created on Sun, 25th of May 2019
Authors are - John Pk Erbynn, Josiah Nii Kortey, Isaac Agyen Duffour

This module handles the alert of any wrong data which is collected and 
...sends to the user's gmail

Usage:
    Parse the json data as an argument unto the send_mail attribute as 
    send_mail(data)

    Expected data must be in the form;

    data = {
        "temperature": 30,
        "turbidity": 7,
        "ph": 2,
        "water_level": 23
    }

"""

import smtplib
from email.message import EmailMessage


def send_mail(sensor_data):
    print("Error found while scanning data readings.\nSending mail ...")
        
    try:
        email_address = 'iotwqms2019@gmail.com'
        email_password = 'iotaquaaid2019'
        email_subject = "WQMS Alert Test Wrap-up :)"
        to_email = ['john.erbynn@gmail.com', 'josiahkotey13@gmail.com']
        # to_email = 'john.erbynn@gmail.com'

        print("Composing mail ...")
        msg = EmailMessage()
        msg['Subject'] = email_subject
        msg['From'] = email_address
        msg['To'] = to_email

        # This identifies the specific data being recorded 
        check_error = ''
        if (sensor_data["temperature"] < 23) | (sensor_data["temperature"] > 34) :
            value = sensor_data["temperature"]
            check_error = f"Temperature out of range: {value} °C \n"

        if (sensor_data["turbidity"] < 0) | (sensor_data["turbidity"] > 5) :
            value = sensor_data["turbidity"]
            check_error += f"Turbidity out of range(Water is not clean): {value} NTU\n" 

        if (sensor_data["ph"] < 0) | (sensor_data["ph"] > 4) :
            value = sensor_data["ph"]
            check_error +=  f"ph out of range: {value} \n" 

        if (sensor_data["water_level"] < 5) | (sensor_data["water_level"] > 27) :
            value = sensor_data["water_level"]
            check_error += f"Water_level out of range (Water not enough): {value} cm \n"
        
        # main content of email
        msg.set_content( f'Data collected... \n\n {sensor_data} \n\n {check_error}' )

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)
            print("Email sent successfully")

    except Exception as err:
        print(f"Oops!!...Failed to send mail. {err}")


# send_mail(data)