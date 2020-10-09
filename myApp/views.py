from django.shortcuts import render
from django.http import HttpResponse
from .models import Info
from .models import rImages,Rfonts
import random
import wikiquote

def home(request):
    all_img = ["https://cdn.wallpapersafari.com/21/3/FDXab2.jpg",
    "https://www.wallpaperflare.com/static/821/889/92/blurred-motion-blur-colorful-landscape-wallpaper.jpg",
    "https://million-wallpapers.com/wallpapers/3/59/462865831916145.jpg",
    "https://wallpaperaccess.com/full/2898150.jpg",
    "https://img3.goodfon.com/wallpaper/nbig/4/4d/dusk-silhouettes-twilight-lights-hill.jpg",
    "https://papers.co/wallpaper/papers.co-oe87-nature-mountain-blur-29-wallpaper.jpg",
    "https://hdwallpaperim.com/wp-content/uploads/2017/08/25/462045-blurred-sky-nature-748x421.jpg",
    "https://wallup.net/wp-content/uploads/2015/12/65322-landscape-nature-mountain-sunset-sunrise-sunlight-blurred-Nepal-Himalayas-climbing-rock.jpg"]


    quotes = Info()
    rimg = rImages()
    rfonts = Rfonts()

    rand_fonts = random.choice([
    "Mali",
    "Rajdhani",
    "Raleway",
    "Acme"])
    
    rand_persons = random.choice([
    "Linus Torvalds",
    "Bill Gates",
    "Walt Disney",
    "Albert Einstein",
    "Walt Disney",
    "William Shakespeare",
    "Elon Musk"
    ])


    quotes.quotes = random.choice(wikiquote.quotes(str(rand_persons)))
    quotes.name = rand_persons

    rimg.urls = random.choice(all_img)

    rfonts.name = rand_fonts
    
    return render(request,'home.html',{'quotes': quotes ,'rimg': rimg,'rfonts': rfonts})


