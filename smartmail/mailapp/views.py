from django.shortcuts import render,redirect
from smartmail.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
import imaplib
import email

def get_info(request):
	global username
	global password
	username = request.POST.get('em')
	password = request.POST.get('pw')
	return render(request,'getinfo.html')

def get_inbox(stat):
	host = 'imap.gmail.com'
	mail = imaplib.IMAP4_SSL(host)
	mail.login(username, password)
	mail.select("inbox")
	_, search_data = mail.search(None, stat)
	my_message = []
	for num in search_data[0].split():
		email_data = {}
		_, data = mail.fetch(num, '(RFC822)')
		_, b = data[0]
		email_message = email.message_from_bytes(b)
		for header in ['subject', 'to', 'from', 'date']:
			email_data[header] = email_message[header]
		for part in email_message.walk():
			if part.get_content_type() == "text/plain":
				body = part.get_payload(decode=True)
				email_data['body'] = body.decode()
			elif part.get_content_type() == "text/html":
				html_body = part.get_payload(decode=True)
				email_data['html_body'] = html_body.decode()
			my_message.append(email_data)
	return my_message

def home(request):
	result = " "
	if request.method == 'POST':
		try:
			result = "Mail sent successfully..."
			subject = request.POST.get('sub')
			message = request.POST.get('msg')
			frm = EMAIL_HOST_USER
			to = []
			to.append(request.POST.get('email'))
			send_mail(subject,message,frm,to,fail_silently = False)
		except:
			result = "Failed to send mail..."
	return render(request,'index.html',{'result':result})

def getmail(request):
	lst = get_inbox('UNSEEN')
	data = []
	for x in lst:
		y = list(x.values())
		data.append(y)
	return render(request,'get.html',{'data':data})

def getseen(request):
	lst = get_inbox('SEEN')
	data = []
	for x in lst:
		y = list(x.values())
		data.append(y)
	return render(request,'getseen.html',{'data':data})