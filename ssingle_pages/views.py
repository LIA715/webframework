from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def landing(request): #랜딩까지 호출이 된다면 클라이언트에게 ssingle>landing.html을 읽어서 보여줘라
    return render(
        request,
        'ssingle_pages/landing.html', #최종적으로 여기 파일을 보여줘. 근데 항상 templates>ssigle>안에 랜딩
    )

def about_me(request):
    return render(
        request,
        'ssingle_pages/about_me.html',
    )
