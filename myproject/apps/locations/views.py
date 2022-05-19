from django.views.generic import ListView, DetailView
from .models import Location


class LocationList(ListView):
    model = Location
    paginate_by = 8

class LocationDetail(DetailView):
    model = Location
    context_object_name = "location"