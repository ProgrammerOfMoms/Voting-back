from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from back import settings

from django.http import HttpResponseRedirect

import requests
import vk_api

from choosing.models import Voter
from choosing.serializers import VoterSerializer
from choosing.models import Voter

import random
import string

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

# from .models import Candidate, Account
# from .serializers import CandidateSerializer

def auth(token):
    vk = vk_api.VkApi(token=token)
    vk._auth_token()
    return vk

import datetime

def set_cookie(response, key, value, days_expire = 10):
  if days_expire is None:
    max_age = 365 * 24 * 60 * 60  #one year
  else:
    max_age = days_expire * 24 * 60 * 60 
  expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
  response.set_cookie(key, value, max_age=max_age, expires=expires, domain=settings.SESSION_COOKIE_DOMAIN, secure=settings.SESSION_COOKIE_SECURE or None)


class Login(APIView):
    def get(self, request):
        try:
            root_url = "https://oauth.vk.com/access_token?"
            if "code" in request.GET:
                code = request.GET["code"]
            res = requests.get(root_url+"client_id="+settings.SOCIAL_AUTH_VK_OAUTH2_KEY+"&client_secret="+settings.SOCIAL_AUTH_VK_OAUTH2_SECRET+"&redirect_uri="+settings.REDIRECT_URI+"&code="+code)
            content = res.json()
            if "error" in content:
                error = content
                return Response(data={"error": error})
            vk = auth(content["access_token"])
            id = content["user_id"]
            user = vk.method("users.get", {"user_ids": [id]})[0]
            group_members = vk.method("groups.getMembers", {"group_id": settings.GROUP_ID})["items"]
            if id in group_members:
                #create new user
                data = {
                    "idVK": str(user["id"]),
                    "firstName": user["first_name"],
                    "lastName": user["last_name"],
                    "is_voted": False,
                    "voted": None
                }
                serializer = VoterSerializer(data = data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                response =  HttpResponseRedirect(redirect_to='https://voting-school47.herokuapp.com/voting?id={}'.format(str(user['id'])))
                set_cookie(response, id, str(user['id']))
                return response
            else:
                return HttpResponseRedirect(redirect_to='https://voting-school47.herokuapp.com/voting')
        except:
            raise


# class GetUser(APIView):
#     def post(self, request):
