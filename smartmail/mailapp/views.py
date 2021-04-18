from django.shortcuts import render
from smartmail.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
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
			result = "Mail sended successfully"
		except:
			result = "Failed to send mail..."
	return render(request,'index.html',{'result':result})
