from django.shortcuts import render
from smartmail.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
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
