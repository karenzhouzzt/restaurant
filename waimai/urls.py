from django.urls improt path

from .improt views
app_name = 'waimai'
urlpatterns = [
    path("",views.home_page, name='home_page'),
]