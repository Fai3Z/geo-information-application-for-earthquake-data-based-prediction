"""geoQuakes1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import url
import django.contrib.auth.views

import geoQuakes1app
from geoQuakes1app.views import quake_dataset, quake_dataset_predict, quake_dataset_pred_risk # this is the view we developed (can be view, class (or class within class), function (or function within function))
# added the ML based endpoint from urls.py

urlpatterns = [
    url(r'^$', geoQuakes1app.views.home, name='home'), # '^$' means that localhost:8000 link is default link (this page is default view), no need to write /admin etc
    # name argument beacuse frontend requires a name of page to direct request to.
    url(r'^quake_dataset/', quake_dataset, name='quakedataset'), # this url will return this view
    # this url will make request in index.html to display markers from DB (variable storing this result is dataUrl)  
    # recall that name is for javascript fronntend to reference
    # IMPORTANT: quake_dataset is the endpoint (http://127.0.0.1:8000/quake_dataset/) that calls the view (quake_dataset) from views.py to return the dataset as json.wewill use this data to build maps and visualize maps 
    
    
    # Add the ML based API endpoints url here:
    url(r'^quake_dataset_predict/', quake_dataset_predict, name="quakedatasetpred"), # name to call this backend endpoint in frontend javascript and html code 
    # now if we add quake_dataset_predict at end of our localhost hyperlink, we should see the prediction data returned in json format
    
    url(r'^quake_dataset_predict_risk/', quake_dataset_pred_risk, name="quakedatasetpredrisk"), 
    path('admin/', admin.site.urls),
]

# we have to design url pattern that points to our 'Quake' dataset endpoint (view in this case definedin views.py as quake_dataset)
# will allow us to display the data on frontend using the REST API

