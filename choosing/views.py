from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.gis.geoip2 import GeoIP2

from .models import Candidate, Voter
from .serializers import CandidateSerializer, VoterSerializer


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class Choosing(APIView):
    def get(self, request):
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        return Response(data = serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request):
        try:
            voter = Voter.objects.get(idVK = request.data["voter_id"])
            candidate = Candidate.objects.get(id = request.data["candidate_id"])
            candidate.votes = candidate.votes + 1
            candidate.save()
            voter.is_voted = True
            voter.vote = candidate
            voter.save()
            candidates = Candidate.objects.all()
            serializer = CandidateSerializer(candidates, many=True)
            return Response(data = serializer.data)
        except:
            return Response(data={"error": "bad"})

            

        

class Status(APIView):
    def get(self, request):
        ip = get_client_ip(request)
        try:
            voter = Voter.objects.get(voter_ip = ip)
            return Response(data={"status": True})
        except:
            return Response(data={"status": False})

class FakeVote(APIView):
    def get(self, request):
        ip = get_client_ip(request)
        voter = Voter.objects.create(voter_ip = ip, isVote=True)
        return Response(data={"status": "ok"})
        