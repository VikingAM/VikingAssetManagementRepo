from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

def landingpage(request):
	return render(request, 'landingpage.html')

def EmailCallBack(request):
	data = {}
	subject = 'Viking asset management Call Back'
	callback_name = request.POST.get('callback-name', False)
	callback_mobile_number = request.POST.get('callback-mobile-number', False)
	callback_date = request.POST.get('callback-date', False)
	message = callback_name+' want us to call them thru his/her number '+callback_mobile_number+" on this date "+callback_date
	from_email = 'william.crumb@vikingassetmanagement.com'
	try:
		send_mail(subject, message, from_email, ['poliamcrumb@gmail.com'])
		data['status'] = "success!"
	except BadHeaderError:
		data['status'] = "error!"
	return JsonResponse(data, safe=False)
