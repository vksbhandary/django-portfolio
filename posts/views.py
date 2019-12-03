from django.shortcuts import render

# Create your views here.
def home_view(request):
    template = 'base.html'
    context = {}
    return render(request, template,context)