from django.contrib import admin
from tweetapp.models import Tweet
# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Message Group',{"fields":["message"]}),
        ('Nickname Group',{"fields":["nickname"]})
    ] #eğer verilerimizi metriklere ayıracaksak(finansal veriler, kullanıcı verileri vb.) böyle yapabiliriz.

    #fields = ['nickname'] #admine kısıt koyabiliriiz

admin.site.register(Tweet, TweetAdmin)
