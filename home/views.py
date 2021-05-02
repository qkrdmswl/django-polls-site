from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from polls.models import Choice, Question
from django.contrib.auth.models import User, Permission
from django.contrib import auth

# Create your views here.


def home(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'home.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):  # 설문 폼을 다시 보여준다
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "답변을 선택하지 않았습니다.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # POST 데이터를 정상적으로 처리하였으면,
        # 항상 HttpResponseRedirect를 반환하여 리다이렉션 처리함
        return HttpResponseRedirect(reverse('polls:results', args=(question_id, )))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})


def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"], password=request.POST["password1"])
            auth.login(request, user)
            permission1 = Permission.objects.get(name='Can view question')
            permission2 = Permission.objects.get(name='Can add question')
            permission3 = Permission.objects.get(name='Can view choice')
            permission4 = Permission.objects.get(name='Can add choice')
            user.user_permissions.add(
                permission1, permission2, permission3, permission4)
            return render(request, 'home.html')
        return render(request, 'signup.html')
    return render(request, 'signup.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'home.html')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def savequestion(request):
    return render(request, 'addvote.html')
