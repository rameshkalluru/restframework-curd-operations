from django.shortcuts import render
from ram.models import *
from ram.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


#read
@api_view(['GET'])
def BookList(request):
    res=Book.objects.all()#query set
    serializer=StaBook(res,many=True)
    return Response(serializer.data)

#create
@api_view(['POST'])
def Bookpost(request):
    res=Book.objects.all()#query set
    serializer=StaBook(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


#update
@api_view(['POST'])
def Bookupdate(request,pk):
    res=Book.objects.get(pk=pk)#query set
    serializer=StaBook(instance=res, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#delete
@api_view(['DELETE'])
def Bookdelete(request,pk):
    res=Book.objects.get(pk=pk)#query set
    res.delete()
    return Response('book is a deleted')
