from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountUpdateForm


def hello_world(request):
    if request.method == "GET":
        print("dddd")
        return render(request, "accountapp/hello_world.html")
    else:
        return render(request, "accountapp/hello_world.html", context={"text": "text"})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("accountapp:hello_world")
    template_name = "accountapp/create.html"


class AccountDetailView(DetailView):
    model = User
    context_object_name = "target_user"  # 템플릿에서 사용하는 user 객체명을 지정해줄 수 있음
    template_name = "accountapp/detail.html"


class AccountUpdateView(UpdateView):
    model = User
    # form_class = UserCreationForm
    context_object_name = "target_user"
    form_class = AccountUpdateForm
    success_url = reverse_lazy("accountapp:hello_world")
    template_name = "accountapp/update.html"


class AccountDeleteView(DeleteView):
    model = User
    context_object_name = "target_user"
    success_url = reverse_lazy("accountapp:login")
    template_name = "accountapp/delete.html"
