from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'

class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voter
        fields = ['idVK', 'firstName', 'lastName', 'is_voted'] 
