from django.urls import path
from .views import ArticleListView, ArticleUpdateView, ArticleDetailView, ArticleDeleteView, ArticleCreateView
from . import views

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('<int:pk>/comment/', views.add_comment, name="new-comment"),
]