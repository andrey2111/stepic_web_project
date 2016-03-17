from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from models import Question, Answer
from forms import AskForm, AnswerForm, SignUpForm
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return paginator, page


def main(request):
    questions = Question.objects.order_by('-id')
    paginator, page = paginate(request, questions)
    paginator.baseurl = '/?page='
    return render(request, 'main.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


def popular(request):
    questions = Question.objects.order_by('-rating')
    paginator, page = paginate(request, questions)
    paginator.baseurl = '/popular/?page='
    return render(request, 'main.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


def question(request, id):
    try:
        question = Question.objects.get(pk=id)
        form = AnswerForm()
    except Question.DoesNotExist:
        raise Http404
    try:
        answers = Answer.objects.filter(question=question).order_by('-added_at')
    except Answer.DoesNotExists:
        answers = None
    return render(request, 'question.html', {
        'question': question,
        'answers': answers,
        'form': form,
    })


def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        form._user = request.user
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask.html', {'form': form})


@require_POST
def answer(request):
    form = AnswerForm(request.POST)
    form._user = request.user
    if form.is_valid():
        answer = form.save()
        url = answer.get_question_url()
        return HttpResponseRedirect(url)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        if form.is_valid():
            form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/signup/')
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if form.is_valid and user.is_active:
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form': form})
