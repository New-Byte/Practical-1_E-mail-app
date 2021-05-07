from django.urls import path
from . import views

urlpatterns = [
	path('',views.home,name='home'),
	path('getmail',views.getmail,name='getmail'),
	path('getseen',views.getseen,name='getseen'),
	path('inbox',views.get_info,name='get_info')
]