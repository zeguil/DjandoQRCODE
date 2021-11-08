from django.shortcuts import render

def leitor(request):
    return render(request, 'leitor.html')
