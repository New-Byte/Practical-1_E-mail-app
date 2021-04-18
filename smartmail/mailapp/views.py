from django.shortcuts import render
from smartmail.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
import imaplib
from email.parser import HeaderParser
def home(request):
	subject = request.POST.get('sub')
	message = request.POST.get('msg')
	frm = EMAIL_HOST_USER
	to = []
	to.append(request.POST.get('email'))
	# print(subject)
	# print(message)
	# print(frm)
	# print(to)
	send_mail(subject,message,frm,to,fail_silently = False)
	return render(request,'index.html')


"""
Deleting a mail:

m = imaplib.IMAP4_SSL("your_imap_server")
m.login("your_username","your_password")
# get list of mailboxes
list = m.list()
# select which mail box to process
m.select("Inbox") 
resp, data = m.uid('search',None, "ALL") # search and return Uids
uids = data[0].split()    
mailparser = HeaderParser()
for uid in uids:
    resp,data = m.uid('fetch',uid,"(BODY[HEADER])")        
    msg = mailparser.parsestr(data[0][1])       
    print (msg['From'],msg['Date'],msg['Subject'])        
    print m.uid('STORE',uid, '+FLAGS', '(\\Deleted)')
print m.expunge()
m.close() # close the mailbox
m.logout() # logout 
"""
