from django.urls import path
from django.views.generic import TemplateView

from commentapp.views import CommentCreateView, CommentDeleteView
from subscribeapp.views import SubscriptionView, SubscriptionListView

app_name = "subscribeapp"

urlpatterns = [
    path("subscribe/", SubscriptionView.as_view(), name="subscribe"),
    path("list/", SubscriptionListView.as_view(), name="list"),
]
