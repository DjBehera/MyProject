from django.shortcuts import render
from master.models import Master
import os
import numpy as np
import pandas as pd
# Create your views here.

def merge_csvs(temp_id):
	dd = []
	for i in os.listdir('C:\\Users\\Dibya\\Desktop\\ProjectBoring\\excelproject\\boringtask\\media\\files'):
		if temp_id in i and 'template' not in i and not i.startswith(temp_id):
			d = pd.read_csv('C:\\Users\\Dibya\\Desktop\\ProjectBoring\\excelproject\\boringtask\\media\\files\\'+i, encoding='ISO-8859-1',error_bad_lines=False)
			dd.append(d)
	ddd = pd.concat(dd)
	ddd.to_csv('C:\\Users\\Dibya\\Desktop\\ProjectBoring\\excelproject\\boringtask\\media\\files\\%s.csv'%temp_id,index=False)
	
def task(request):
	admin_list = ['consolify','sriram']
	id_list = []	
	obj = Master.objects
	for i in obj.all():
		id_list.append(i.cid)
	if request.method == "POST":
		if request.POST['username'] and request.POST['id']:
			if request.POST['id'] not in id_list:
				return render(request,'consolify/consolify.html',{'error':'Incorrect Template ID'})
			else:
				if request.POST['username'] not in admin_list:
					return render(request,'consolify/consolify.html',{'error':'Not Authorized'})
				else:
					merge_csvs(request.POST['id'])
					return render(request,'consolify/consolified.html',{'message':request.POST['id']+'.csv'})
		else:
			return render(request,'consolify/consolify.html',{'error':'All Fields Required'})
	else:
		return render(request,'consolify/consolify.html')
