
def sendmail(listederlinks):
    import smtplib
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("send-email@provider.com", "passwort")

    if listederlinks[0]:
        links2 = ['\nhttps://willhaben.at' + link for link in listederlinks]
        msg = '\n'.join(links2)

    server.sendmail("send-email@provider.com", "receive-email@provider.com", msg)
    server.close()

