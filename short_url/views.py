from django.shortcuts import redirect
from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View
from django.conf import settings

import random

class UrlShortenerView(View):
  def post(self, request):
    long_url = request.POST.get("long_url")
    short_url = str(random.randint(1, 100))

    data = {
        "long_url": long_url,
        "short_url": short_url
      }

    settings.MONGODB.urls.insert_one(data)

    return JsonResponse({
        "long_url": long_url,
        "short_url": short_url
      }
    )

class RedirectorView(View):
  def get(self, request):
    path = request.path.split('/')[-1]
    redirect_to = settings.MONGODB.urls.find_one({"short_url": path})

    if redirect_to is None:
      return HttpResponseBadRequest('Err')
    else:
      return redirect(redirect_to['long_url'])