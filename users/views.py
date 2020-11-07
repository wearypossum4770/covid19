import json
from django.shortcuts import render
from django.core.cache import caches
from django.contrib.auth import views as auth_views


def home(self):
    return render(request, "home.html")


# def home(request):
#     # Get Session Key
#     if not request.session.session_key:
#         request.session.save()
#     session_id = request.session.session_key

#     redis_cache = caches["default"]
#     redis_client = redis_cache.client.get_client()
#     redis_client.expire(session_id, "3600")

#     # String
#     redis_client.hset(session_id, "request", "response")
#     output_val = redis_client.hget(session_id, "request")  # output is response

#     # Dictionary
#     redis_client.hset(session_id, "earth", json.dumps({"water": "ocean"}))
#     output_val = json.loads(
#         redis_client.hget(session_id, "earth")
#     )  # output is {'water': 'ocean'}
