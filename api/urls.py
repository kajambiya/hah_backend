from django.urls import path
from . import views

urlpatterns = [
    path('api/episodes/', views.EpisodeListView.as_view(), name='episode-list'),
    path('api/testimonials/', views.TestimonialListView.as_view(), name='testimonial-list'),
    path('api/books/', views.BookListView.as_view(), name='book-list'),
    path('api/events/', views.EventListView.as_view(), name='evenr-list'),
    path('api/partners/', views.PartnerListView.as_view(), name='partner-list'),
]