from django.shortcuts import render
from rest_framework import viewsets
from .models import awsimage,Diseases,Fertilizers
from .serliazer import awsiImageserliazer,UserSignupsrilaizer,diseasesserializer,ferilizersserializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http.response import JsonResponse 
from rest_framework import status,filters
import os
import joblib



data = ""
class awsImageview(viewsets.ModelViewSet):
    queryset=awsimage.objects.all()
    serializer_class=awsiImageserliazer
    data=serializer_class.data
    


     



@api_view(['GET','POST'])
def ret(request):

    if request.method == 'POST':
        model=joblib.load(os.path.join('apiapp\save.pkl'))
        prediction=model.predict(data)[0]
        if prediction == 0:
            output="awl mrd"
        elif prediction == 1:
            output="tany mrd"
        elif prediction == 2:
            output="talat mrd"
        elif prediction == 3:
            output="healthy"
        return JsonResponse({"prediction" : output})
        
            


@api_view(['GET','POST'])
def FBV_LIST(request):


    if request.method == 'GET':
        diseas = Diseases.objects.all()
        serializer=diseasesserializer(diseas,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer=diseasesserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data , status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','POST'])
def fer_list(request):
    
    if request.method == 'GET':
        diseas = Fertilizers.objects.all()
        serializer=ferilizersserializer(diseas,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer=ferilizersserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data , status=status.HTTP_400_BAD_REQUEST)



# class UserLoginViewset(viewsets.ModelViewSet):
#     permission_classes=(IsAuthenticated,)
#     serializer_class=UserLoginserliazer
#     queryset=get_user_model().objects.all()


class userSignupViewset(generics.CreateAPIView):
    queryset=User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class=UserSignupsrilaizer



# 
from .serliazer import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer