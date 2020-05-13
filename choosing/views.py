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
        ip = get_client_ip(request)
        try:
            voter = Voter.objects.get(voter_ip = ip)
            candidates = Candidate.objects.all()
            serializer = CandidateSerializer(candidates, many=True)
            data = serializer.data
            res = {"status": "already_voted"}
            res.update({"candidates": data})
            print(res)
            return Response(data=data)
        except:         
            candidate_id = request.data['id']
            try:
                candidate = Candidate.objects.get(id=candidate_id)
                candidate.votes = candidate.votes + 1
                candidate.save()
                Voter.objects.create(voter_ip=ip, isVote=True)
                candidates = Candidate.objects.all()
                serializer = CandidateSerializer(candidates, many=True)
                data = serializer.data
                res = {"status": "voted"}
                res.update({"candidates": data})
                print(res)
                return Response(data=res)
            except:
                candidates = Candidate.objects.all()
                serializer = CandidateSerializer(candidates, many=True)
                data = serializer.data
                res = {"status": "bad id"}
                res.update({"candidates": data})
                print(res)
                return Response(data=data)

        

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
        