from django.urls import path

from . import views

app_name = 'IC'
urlpatterns = [
    # ex: /IC/
    path('', views.index, name='index'),
    path('<int:test_id>/', views.test, name='test'),
    path('<int:test_id>/save', views.save, name='save'),
    path('<int:answer_id>/certificate', views.certificate, name='certificate'),
    path('list', views.list, name='list'),
]
