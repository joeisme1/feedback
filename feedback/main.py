def feedback(project, email, password):
  import smtplib, ssl
  message = str(project) + (":") + input(" Feedback: ")
  smtp_server = "smtp.gmail.com"
  port = 587  # For starttls
  sender_email = email

# Create a secure SSL context
  context = ssl.create_default_context()

# Try to log in to server and send email
  server = smtplib.SMTP(smtp_server,port)
  server.ehlo() # Can be omitted
  server.starttls(context=context) # Secure the connection
  server.ehlo() # Can be omitted
  server.login(sender_email, password)
    # TODO: Send email here

  server.sendmail(email, email, message)
  server.quit() 


