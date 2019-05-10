from django.shortcuts import render , HttpResponse

# Create your views here.

def home_view(request):

    if request.user.is_authenticated():
        context = {
            'isim' : 'FURKAN'
        }

    else:
        context = {
            'isim': 'MİSAFİR'
        }
    return render(request,"home.html",context)