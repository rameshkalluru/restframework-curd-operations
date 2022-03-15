from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
# Create your views here.
@api_view(['GET'])
def home(request):
    goto=god.objects.all()
    serializer=Angel(goto,many=True)
    return Response({'payload':serializer.data})
