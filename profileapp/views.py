from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = "target_profile"
    form_class = ProfileCreationForm
    # success_url에서는 동적인 추가데이터를 보내줄 수 없다.
    # 그러므로 내부 메서드를 수정한다.
    success_url = reverse_lazy("accountapp:hello_world")
    template_name = "profileapp/create.html"

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        # 여기서 self는 Profile임
        return reverse("accountapp:detail", kwargs={"pk": self.object.user.pk})


@method_decorator(profile_ownership_required, "get")
@method_decorator(profile_ownership_required, "post")
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = "target_profile"
    form_class = ProfileCreationForm
    success_url = reverse_lazy("accountapp:hello_world")
    template_name = "profileapp/update.html"

    def get_success_url(self):
        # 여기서 self는 Profile임
        return reverse("accountapp:detail", kwargs={"pk": self.object.user.pk})
