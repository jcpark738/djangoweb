from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    #templates폴더 안에있는 폴더 및 html파일의 경로를 설정
    return render(request,'main/index.html')

def program(request):
    programlist = Program.objects.all()
    return render(request,'main/program.html', {'programList':programlist})
