from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'common/index.html')

def introduce(request):
    return render(request, 'common/introduce.html')