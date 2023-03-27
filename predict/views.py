from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
import random
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
# Create your views here.
TAMANO_IMG = 100

class prediccion(APIView):
    def createJson(self,message,data,status):
        custom={"messages":message,"pay_load":data,"status":status}
        auxiliar=json.dumps(custom)
        responseOk=json.loads(auxiliar)
        return responseOk

    def get(self, request, format=None):
        responseOk=self.createJson("succes","202","funciona")
        print('hola')
        return Response(responseOk)
    
    def post(self, request, format=None):
        #modelo_exportado = load_model('modelov5.h5')
        modelo_exportado = load_model('modelo3.h5')
        prueba = []
        responseOk=self.createJson("succes","202","funciona")
        serializer = request.data
        img = request.FILES.get('image')
        image_bytes = img.read()
        imagen = np.array(Image.open(BytesIO(image_bytes)))
        print(imagen)
        imagen = cv2.resize(imagen,(TAMANO_IMG,TAMANO_IMG))
        imagen = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
        imagen = imagen.reshape(TAMANO_IMG,TAMANO_IMG,1)
        prueba.append(imagen)
        tensor = tf.convert_to_tensor(prueba)
        print(tensor.shape)
        resultado = modelo_exportado.predict([tensor])
        print(resultado)
        result = str(resultado)
        #return Response('Katakana')
        if result == "[[0.]]":
            return Response('Hiragana')
        else:
            return Response('Katakana')
        
        #return Response(responseOk)

    












    # def post(self, request, format=None):
    #     modelo_exportado = load_model('modelov5.h5')
    #     prueba = []
    #     responseOk=self.createJson("succes","202","funciona")
    #     serializer = request.data
    #     img = request.FILES.get('image')
    #     print(type(img))
    #     image_bytes = img.read()
    #     test = np.frombuffer(image_bytes,np.uint8)
    #     print(type(test))
    #     test = cv2.resize(test,(TAMANO_IMG,TAMANO_IMG))
    #     #test = cv2.cvtColor(test,cv2.COLOR_BGR2GRAY)
    #     test = test.reshape(TAMANO_IMG,TAMANO_IMG,1)
    #     prueba.append(test)
    #     print(type(prueba))
    #     tensor = tf.convert_to_tensor(prueba)
    #     print(tensor.shape)
    #     resultado = modelo_exportado.predict([tensor])
    #     print(resultado)

    #     return Response(responseOk)