from django.shortcuts import render
from django.shortcuts import render
import base64
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
import pixellib
from pixellib.tune_bg import alter_bg
import cv2
import io
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
import random
import numpy as np

# Create your views here.

class TestView(APIView):

	def post(self,request):
		encoded=request.data["Image"]
		imgdata = base64.b64decode(encoded)
		number=""
		for i in range(4):
			number+=str(random.randint(1,9))
		filename = str(number)+'.jpg'
		with open(filename, 'wb') as f:
			f.write(imgdata)
		change_bg = alter_bg()
		change_bg.load_pascalvoc_model("deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")
		output = change_bg.color_bg(filename, colors = (255, 255, 255))
		cv2.imwrite(str(number)+"_0"+".jpg", output)
		with open(str(number)+"_0"+".jpg", "rb") as img_file:
			my_string = base64.b64encode(img_file.read())

		# contours,hierachy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

		# with open('readme.txt', 'w') as f:
		# 	f.write(str(my_string))
		return Response({'success':True,'bgr_image':my_string})












