from django.shortcuts import render
from django.views import View

# Create your views here.
class index(View):
    def get(self, request):
       return render(request, "league_profiles/index.html")

    def post(self, request):
        pass