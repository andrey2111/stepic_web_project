from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core.paginator import Paginator
from models import Question


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def main(request):
    questions = Question.objects.order_by('-id')
    page = request.GET.get('page', 1)
    limit = request.GET.get('limit', 10)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'main.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })
