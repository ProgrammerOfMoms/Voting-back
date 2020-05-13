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
            voter = Voter.objects.get(request.data["voter_id"])
            candidate = Candidate.objects.get(request.data["candidate_id"])
            candidate.vote = candidate.vote + 1
            candidate.save()
            voter.is_vote = True
            voter.vote = candidate
            voter.save()
            return Response(data = {"status": "ok"})
        except:
            return Response(data={"status": "bad"})

            

        

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
        