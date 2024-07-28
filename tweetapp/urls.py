from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'tweetapp'

urlpatterns = [
    path("",views.listtweet,name='listtweet'), #dogukanduman.com/tweetapp
    path("addtweet/",views.addtweet,name='addtweet'), # dogukanduman.com/tweetapp/addtweet
    path("addtweetbyform/",views.addtweetbyform,name="addtweetbyform"),
    path("addtweetbymodelform/",views.addtweetmodelform, name="addtweetbymodelform"),
    path("signup/",views.SignUpView.as_view(), name="signup"),
    path("deletetweet/<int:id>", views.deleteTweet, name="deleteTweet")
]