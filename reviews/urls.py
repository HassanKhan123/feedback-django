from django.urls import path

from . import views

urlpatterns = [
    path("", views.ReviewView.as_view(), name="review"),
    path("thank-you/", views.ThankYouView.as_view(), name="thankyou"),
    path("review-list/", views.ReviewListView.as_view(), name="review_list"),
]
