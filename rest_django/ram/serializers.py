from dataclasses import fields
from rest_framework import serializers
from .models import *

class StaBook(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'