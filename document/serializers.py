from rest_framework import serializers
from .models import *


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'
