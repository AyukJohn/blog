from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Article
# from .models import Products

# Create your views here.


def index(request):
    # return HttpResponse('hy')
    
    contents = Article.objects.all()

    paginator = Paginator(contents, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render(request, 'index.html',{'page_obj': page_obj})