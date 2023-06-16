from django.shortcuts import render,redirect
from django.http import HttpResponse
# import openai
from .models import Question
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import CreateUserForm
# openai.api_key = "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 my open ai key"

# messages = []

# sys_msg = {"role":"system" , "content":"Ask me anything on Land in Uganda"}
# messages.append(sys_msg)

# while True:
#     user_content = input(">")
#     user_msg = {"role":"user","content":user_content}
#     messages.append(user_msg)
#     response = openai.ChatCompletion.create(model ="gpt-3.5-turbo",messages=messages)
#     reply = response["choices"][0]["message"]["content"]
#     messages.append({"role":"assistant","content":reply})

# Create your views here.
def ask (request):
    questions = Question.objects.all()
    context = {
        'questions':questions
    }
    return render(request,'ask/ask.html',context)

def home (request):
    return render(request,'ask/home.html')

def registerpage(request):
    form = CreateUserForm
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username') 
            messages.success(request,'Account created for' + user )
            return redirect('login')

    context = {'form':form}

    return render (request, 'ask/register.html',context)

def loginpage(request):
    return render (request, 'ask/login.html')