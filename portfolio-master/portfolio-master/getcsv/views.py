from django.shortcuts import render
import pandas as pd
import numpy as np
import os

# Create your views here.
def task(request):
	return render(request,'getcsv/getcsv.html')

