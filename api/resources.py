# api/resources.py

from tastypie.resources import ModelResource
from api.models import URL

class URLResource(ModelResource):
    class Meta:
        queryset = URL.objects.all()
        resource_name = 'longAddress'
