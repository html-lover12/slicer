# libraries to be imported
    import smtplib
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the sender's email address
    msg['From'] = 'me@gmail.com'

    # storing the receiver's email address
    msg['To'] = 'you@gmail.com'

    # storing the subject
    msg['Subject'] = 'Email using Python'

    # Store the body of the mail
    message = 'Scaler Topics'

    # attach the body with the msg instance
    msg.attach(MIMEText(message))

    # creates SMTP session
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)

    # identify ourselves to smtp gmail client
    mailserver.ehlo()

    # secure our email with tls encryption
    mailserver.starttls()

    # re-identify ourselves as an encrypted connection
    mailserver.ehlo()

    # Authentication
    mailserver.login('me@gmail.com', 'mypassword')

    mailserver.sendmail('me@gmail.com', 'you@gmail.com', msg.as_string())

    mailserver.quit()
