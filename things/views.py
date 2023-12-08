from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def things_view(request):
    return render(request, 'things_page.html')

def home_view(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Things</title>
    </head>
    <body>
        <h1>Things</h1>
    </body>
    </html>
    """
    return HttpResponse(html)