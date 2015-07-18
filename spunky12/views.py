from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("dammitall")

def spunky_at_the_park(request):
	return render(request, "spunky12/spunky.html")
