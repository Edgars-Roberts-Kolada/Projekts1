import imaplib
import email
import datetime
from reportlab.lib.colors import crimson, black
from reportlab.lib.units import cm
from reportlab.pdfgen.canvas import Canvas
import os


# E-pata atversana
imap_url = 'imap.gmail.com'
my_mail = imaplib.IMAP4_SSL(imap_url)
my_mail.login("erk.testpasts@gmail.com", "nzvy jpdl mjcm gcjh") #Testesanas e-pasts, kuru es dzesisu, kad tiks izlikts vertejums. Savaa versijaa ir mana galvenaa e-pata adrese un parole.
my_mail.select("INBOX", readonly=True)
aaa, data = my_mail.search(None, 'ALL')


# Palaisanas laika nolasisana un saglabasana
Lastrun = datetime.datetime.strptime(open("lastrun.txt","r").read(), "%d-%m-%Y (%H:%M:%S)")

Tagadsafe = datetime.datetime.now() - datetime.timedelta(hours=1) #Nezinu vai ekstra stunda daudz ko mainis, bet jutas drosaak gadijumam ja e-pasts antnaak skripta palaisanas laikaa.

open("lastrun.txt","w+").write((Tagadsafe).strftime("%d-%m-%Y (%H:%M:%S)"))



# Jauno e-pastu sutitaja, temata un laika ievietosana listaa
list = reversed(data[0].split()) #Parveide lai e-patsus parbauditu sakot ar jaunaako
temp=[]
pasti=[]
for i in list:
    typ, data = my_mail.fetch(i, '(RFC822)')
    mail=data[0][1]
    msg = email.message_from_bytes(mail)
    Date=email.utils.parsedate_to_datetime(msg['Date']).replace(tzinfo=None)
    if Lastrun > Date:  #Parbaude vai epasts jau bija pajajusajaa palaisanaa
        break
    temp.append(email.utils.parseaddr(msg['from'])[1])
    temp.append(msg['subject'])
    temp.append(Date)
    pasti.append(temp)
    temp=[]



# Vecaa atgaadinaajuma dzesana
if os.path.exists("Atgadinajums.pdf"):
  os.remove("Atgadinajums.pdf")


# Atgadinajuma pdf veidosana, ja ir jauni e-pasti
if pasti:
    canvas = Canvas("Atgadinajums.pdf", pagesize=(40 * cm, 18 * cm))
    canvas.setFont("Times-Roman", 40)
    canvas.setFillColor(crimson)
    canvas.drawString(16 * cm, 16 * cm, "Jauni e-pasti!")
    canvas.setFont("Times-Roman", 13)
    canvas.setFillColor(black)
    n=0
    for i in pasti:
        canvas.drawString(2 * cm, (14-0.8*n )* cm, str(i[0]) + "  |  " + str(i[1]) + "  |  " + i[2].strftime("%d-%m-%Y (%H:%M:%S)"))
        n=n+1

    canvas.save()


# Atgadinajuma atversana, ja ir jauni e-pasti
if os.path.exists("Atgadinajums.pdf"):
  os.system("Atgadinajums.pdf")