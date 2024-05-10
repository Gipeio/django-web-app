from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from listings.models import Band,Listing

def band_list(request):

    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})

def band_detail(request, band_id):
    
    band = get_object_or_404(Band, id = band_id)
    return render(request, 'listings/band_detail.html', {'band': band})

def about(request):

    return render(request, 'listings/about.html')

def listings(request):
    
    listings = Listing.objects.all()
    return render(request, 'listings/listing.html', {'listings': listings})

def listing_detail(request, listing_id):
    
    listing = get_object_or_404(Listing, id = listing_id)
    return render(request, 'listings/listing_detail.html', {'listing': listing})

def contact(request):
    
    return render(request, 'listings/contact.html')

def page_not_found(request, exception):
    return render(request,'listings/page_not_found.html',status=404)