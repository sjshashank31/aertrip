from django.shortcuts import render, HttpResponse, redirect
from . import queryparser
import json
# Create your views here.


def home(request):

    if request.POST:
        query = request.POST['query']
        print(query)
        result = queryparser.query_parser(query)
        request.session['response'] = json.dumps(result, default=str)
        return redirect('booking')
    return render(request, 'index.html')


def booking(request):
    resp = request.session.get('response')
    resp = json.loads(resp)
    request.session.flush()
    return render(request, 'booking.html', {"travel_details": resp[0], "return_details": resp[1]})

