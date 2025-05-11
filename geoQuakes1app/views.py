from django.shortcuts import render
from django.http import HttpRequest, HttpResponse  # these modules handles requests we make to app or API and handle the response
# i.e making request to a view containing index.html file
from django.template import RequestContext
from datetime import datetime
from django.core.serializers import serialize # to format the view of a response in json format
from geoQuakes1app.models import Quake, Quake_Predictions # import model conntaining ML working too
from django.template.context import Context
import pandas as pd # in case we need to use pandas to manipulate our views

# Create our django views here.
def quake_dataset(request): # this view named quake_dataset expects a request that can be in form of a click on app and the http response will be returned (the contents of that http response is what we will code in this view)
    quakes=serialize('json', Quake.objects.order_by("ID")[:1000]) # limiting showable records to 1000 to prevent slowup on PC.depends on local device hardware. the records areordered by ID and serialized as json
    return HttpResponse(quakes,content_type='json') # resturn serialized dataset from this view as json. we will test this response when we create a RESTAPI and send request to this view to see what kind of data is being returned

# next view is main view that returns index.html page
def home(request):
    return render(request, 'app/index.html',
                  {
                      'title':'Home Page'}) # 'app' to tell django to look into the 'app' for 'template folder' containg the required html page to return
    # 'Home page' is title of page returned
    # django template engine passes data from backend to fronted.
    # we will use AJAX to make requests as it is asynchronous and faster 

# we add second endpoint for our prediction dataset (creating URL endpoint for our prediction dataset) ML based endpoint
def quake_dataset_predict(request): # this endpoint takes a request
    quakes_pred=serialize('json', Quake_Predictions.objects.all()[:1000]) # query Quake_Predictions.objects.all() (important note: ask gpt what this does)
    # limit to first 1000 entries
    return HttpResponse(quakes_pred, content_type='json')

# now we need to add url endpoint for our second endpoint in urls.py file


# make endpoint for high risk quake sites i.e magnitude>6.5
# i.e we will filter on the magnitude value
def quake_dataset_pred_risk(request):
    quake_risk=serialize('json', Quake_Predictions.objects.filter(Magnitude__gt=6.5))
    # return query with http response
    return HttpResponse(quake_risk, content_type='json')


