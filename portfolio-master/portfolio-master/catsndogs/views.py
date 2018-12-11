from django.shortcuts import render

import numpy as np
import pickle
from keras.preprocessing import image
from .models import CatsDogs
from keras import backend as K
# Create your views here.


def task(request):
	if request.method == 'POST':
		if not request.POST['name']:
			return render(request,'catsndogs/catsndogs.html',{'error':'All fields required'})
		else:
			product = CatsDogs()
			product.name = request.POST['name']
			product.img = request.FILES['image']
			print(product.img.name)
			if product.img.name.endswith('jpg'):
				product.save()
				test_image = image.load_img(request.FILES['image'],target_size = (64,64))
				#return render(request,'catsndogs/catsndogs.html',{'error':'SUCCESS'})
				test_image = image.img_to_array(test_image)
				test_image = np.expand_dims(test_image,axis=0)
				model = pickle.load(open('C:\\Users\\dibehera\\Desktop\\boringjobs\\portfolio-master\\portfolio-master\\catsndogs\\catsndogs2.pkl',"rb"))
				result = model.predict(test_image)
				K.clear_session()
				product.delete()
				#training_set.class_indices
				print(result[0][0])
				if result[0][0] == 1:
					return render(request,'catsndogs/catsndogs.html',{'error':'dog'})
				else:
					return render(request,'catsndogs/catsndogs.html',{'error':'cat'})
			else:
				return render(request,'catsndogs/catsndogs.html',{'error':'Must upload a JPG'})
	else:
		return render(request,'catsndogs/catsndogs.html')