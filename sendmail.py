
def sendmail(listederlinks):
    import smtplib
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("senderadresse@provider.com", "passwort")


    if listederlinks[0]:
        links2 = ['https://willhaben.at' + str(link) for link in listederlinks]
        msg = '\n' + '\n'.join(links2)

    server.sendmail("senderadresse@provider.com", "empfängeradresse@provider.com", msg)
    server.close()

