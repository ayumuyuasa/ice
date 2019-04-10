from django.views import generic
from .models import Item

class IndexView(generic.ListView):
	model = Item