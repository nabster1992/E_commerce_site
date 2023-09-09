from django.conf import settings
from .models import Product 


class Cart(object):
    def __init__(self, request):
        self.session = request.session