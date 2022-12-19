from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.cache import cache
@receiver(user_logged_in,sender=User)
def user_login(sender,request,user,**kwargs):
    ip=request.META.get("REMOTE_ADDR")
    request.session["ip"]=ip
    ct=cache.get("count",0,version=user.pk)
    new=ct + 1
    cache.set("count",new,60*24*24,version=user.pk)
    
    