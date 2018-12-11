from django.shortcuts import render

# Create your views here.
from .models import Master
def task(request):
	id_list = []	
	obj = Master.objects
	for i in obj.all():
		id_list.append(i.cid)
	print(id_list)
	admin_list = ['consolify','sriram']	
	if request.method == "POST":
		if request.POST['username'] and request.POST['id'] and request.FILES['excel']:
			product = Master()
			product.name = request.POST['username']
			product.cid = request.POST['id']
			product.csv = request.FILES['excel']
			print(type(product.csv.url))
			print(product.csv.name)
			product.csv.name = 'template_'+product.cid+'.csv'
			if product.csv.url.endswith('csv'):
				if product.cid not in id_list:
					if product.name in admin_list:
						product.save()
						return render(request,'master/master.html',{'error':'SUCCESS'})
					else:
						return render(request,'master/master.html',{'error':'Not Authorized'})
				else:
					return render(request,'master/master.html',{'error':'Template ID in use'})
			else:
				return render(request,'master/master.html',{'error':'must submit a CSV file'})
		else:
			return render(request,'master/master.html',{'error':'All fields Required'})
	else:
		return render(request,'master/master.html')