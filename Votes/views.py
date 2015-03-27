from django.shortcuts import render
from django.http import HttpResponse
import simplejson
from models import Vote
# Create your views here.


def GetVotes(request):
    votes = Vote.objects.all()
    results = []
    for vote in votes:
        results.append(vote.to_json())
    return HttpResponse(simplejson.dumps(results, ensure_ascii=False, encoding='utf-8'))