import requests
from bs4 import BeautifulSoup

from django.shortcuts import render


def home(request):
    
    followers = "29700000"
    
    return render(request, "movies/home.html" , {'num_followers': followers})
