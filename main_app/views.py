from django.shortcuts import render

# Create your views here.
from django.db import models
from django import forms
from . import test_model
import os
import numpy as np

class input(models.Model):
	image1 = models.ImageField(upload_to = 'images/')
	image2 = models.ImageField(upload_to = 'images/',blank = True)
	image3 = models.ImageField(upload_to = 'images/',blank = True)
	image4 = models.ImageField(upload_to = 'images/',blank = True)
	image5 = models.ImageField(upload_to = 'images/',blank = True)
	image6 = models.ImageField(upload_to = 'images/',blank = True)

	choices = (
		("1","Model1"),
		("2","Model2"),
		("3","Model3")
		)
	t_model = models.CharField(max_length = 128,choices = choices)

class input_f(forms.ModelForm):
	class Meta:
		model = input
		fields = ["image1","image2","image3","image4","image5","image6", "t_model"]
		widgets = {
		't_model' : forms.RadioSelect()
		}


def load_plot(request):
	return render(request,"main_app/plot.html")

def load_output(request):
	return render(request, "main_app/output.html")

def load_members(request):
	return render(request,"main_app/members.html")

def load_about(request):
	return render (request,"main_app/about.html")

def index(request):
	arr_p = ["" for i in range(5)]
	if request.method == "POST":
		path_ = os.path.join("/Users/hardikdudeja/Documents/PB_Project/PBproject/media/","images")
		for f_names in os.listdir(path_):
			p = os.path.join(path_,f_names)
			os.remove(p)
		# path_2 = os.path.join("/Users/hardikdudeja/Documents/PB_Project/PBproject/media/","images_resized")
		# for f_names in os.listdir(path_2):
		# 	p = os.path.join(path_2,f_names)
		# 	os.remove(p)

		form = input_f(request.POST,request.FILES)
		if form.is_valid():
			form.save();

		path = []
		output = []
		img = input.objects.all()[input.objects.count() - 1]
		print(img.t_model)

		if img.t_model == '1':
			path, output = test_model.run()
			print('using model1')

		elif img.t_model == '2':
			path, output = test_model.run_model2()
			print('using model2')

		elif img.t_model == '3':
			path, output = test_model.run_model3()
			print('using model3')

		for i in range(0, 5 - len(path)):
			path = np.append(path,"")
			output = np.append(output, 0)
		print(path)
		print(output)



		
		for i in range(len(path)):
			path[i] = path[i].split("/")[-1]

		print(path)

		if(img.image1):
			s = img.image1.url;
			s = s.split("/")[-1];
			print(s)
			index = (path==s)
			print(index)
			arr_p[0] = (output[index])
			# print(index[0][0])
				

		if(img.image2):
			s = img.image2.url;
			s = s.split("/")[-1];
			print(s)
			index = (path==s)
			print(index)
			arr_p[1] = (output[index])
			# print(index[0][0])
				

		if(img.image3):
			s = img.image3.url;
			s = s.split("/")[-1];
			print(s)
			index = (path==s)
			print(index)
			arr_p[2] = (output[index])
			# print(index[0][0])
				

		if(img.image4):
			s = img.image4.url;
			s = s.split("/")[-1];
			print(s)
			index = (path==s)
			print(index)
			arr_p[3] = (output[index])
				

		if(img.image5):
			s = img.image5.url;
			s = s.split("/")[-1];
			print(s)
			index = (path==s)
			print(index)
			arr_p[4] = (output[index])


		for ele in arr_p:
			print(type(ele))

		# print(arr_p[0][0])
		arr_result = []
		for ele in arr_p:
			arr_result.append(ele)

		for i in range(len(arr_p)):
			if(isinstance(arr_p[i], np.ndarray)):
				print('hardikdudeja')
				if arr_p[i][0] == 0:
					arr_result[i] = 'LOW RISK'
				else:
					arr_result[i] = 'HIGH RISK'
				
		print(arr_result)

		return render(request,"main_app/output.html",{
            "input1_o": arr_result[0],
            "input2_o": arr_result[1],
            "input3_o": arr_result[2],
            "input4_o": arr_result[3],
            "input5_o": arr_result[4],
            "img": img
            })
		
	form = input_f()

	return render(request,"main_app/home1.html",{
		"form" : form
		})