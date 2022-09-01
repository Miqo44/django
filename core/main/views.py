from django.shortcuts import render
from django.views.generic import ListView

from .models import Home, About, About2, Slider, Client, ClientImg, LetsTalk

# Create your views here.
class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        home = Home.objects.all()
        about = About.objects.all()
        about2 = About.objects.all()
        slider = Slider.objects.all()
        client = Client.objects.all()
        clientimg = ClientImg.objects.all()
        letstalk = LetsTalk.objects.all()
        return render(request, self.template_name, {'home': home, 'about':about, 'about2':about2, 'slider':slider, 'client':client, 'clientimg':clientimg, 'letstalk':letstalk})