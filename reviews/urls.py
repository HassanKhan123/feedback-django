from django.urls import path

from . import views

urlpatterns = [
    path("", views.ReviewView.as_view(), name="review"),
    path("thank-you/", views.ThankYouView.as_view(), name="thankyou"),
    path("reviews/", views.ReviewListView.as_view(), name="review_list"),
    path("reviews/<int:pk>/", views.SingleReviewView.as_view(), name="single_review"),
]
