from dataclasses import fields
from distutils.util import execute
from rest_framework import serializers
from .models import *


class Angel(serializers.ModelSerializer):
    class Meta:
        model=god
        fields='__all__'