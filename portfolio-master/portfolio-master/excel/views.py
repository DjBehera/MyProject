from django.shortcuts import render,redirect
from .models import excelmodel
from master.models import Master
# Create your views here.
def task(request):
	id_list = []
	name_list = []
	obj = Master.objects
	obj_excel = excelmodel.objects
	for i in obj.all():
		id_list.append(i.cid)
	for i in obj_excel.all():
		name_list.append(i.name)
	if request.method == "POST":
		if request.POST['username'] and request.POST['id'] and request.FILES['excel']:
			product = excelmodel()
			product.name = request.POST['username']
			product.cid = request.POST['id']
			product.csv = request.FILES['excel']
			if product.csv.url.endswith('csv'):
				if product.cid in id_list:
					if product.name in name_list:
						obj_excel.filter(name=product.name).delete()
						product.csv.name = product.name+'_'+product.cid+'.csv'
						product.save()
						return render(request,'excel/boringjobs.html',{'error':'Previous record deleted'})
					else:
						product.csv.name = product.name+'_'+product.cid+'.csv'
						product.save()
						return render(request,'excel/boringjobs.html')
				else:
					return render(request,'excel/boringjobs.html',{'error':'Incorrect Template ID'})
			else:
				return render(request,'excel/boringjobs.html',{'error':'must submit a CSV file'})
		else:
			return render(request,'excel/boringjobs.html',{'error':'All fields Required'})
	else:
		return render(request,'excel/boringjobs.html')
