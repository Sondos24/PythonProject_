from django.shortcuts import render, redirect
from .models import Advertisement
from .forms import AdvertisementForm

def add_advertisement(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_ads')
    else:
        form = AdvertisementForm()
    return render(request, 'ads/add_advertisement.html', {'form': form})

def list_ads(request):
    ads = Advertisement.objects.all()
    return render(request, 'ads/list_ads.html', {'ads': ads})
