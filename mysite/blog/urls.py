from django.urls import path
from . import views

# we define an application namespace with the app_name variable
#  This allows us to organize URLs by application
# and use the name when referring to them.
app_name = 'blog'

urlpatterns = [
    # path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail')
]
