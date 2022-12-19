from django.shortcuts import render,HttpResponseRedirect
from . forms import user_reg,user_log,update_post
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from . models import Post
from django.contrib.auth.models import Group,User
from django.core.cache import cache

def home(request):
    fm=Post.objects.all()
    return render(request,"home.html",{"post":fm})

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def dashboard(request):
    if request.user.is_authenticated:
        fm=Post.objects.all()
        fr=request.user
        group=fr.groups.all()
        ct=cache.get("count",version=fr.pk)
        ir=request.session.get("ip",0)
        return render(request,"dashboard.html",{"post":fm,"name":fr,"group":group,"ip":ir,"count":ct})
    else:
        return HttpResponseRedirect("/login/")

def user_signup(request):
    if request.method=="POST":
        fm=user_reg(request.POST)
        if fm.is_valid():
            use=fm.save()
            group=Group.objects.get(name="author")
            use.groups.add(group)
            messages.success(request,"you have been successfully registerd")  
            fm=user_reg()
    else:
        fm=user_reg()
    return render(request,"user_signup.html",{"fm":fm})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=user_log(request=request,data=request.POST)
            if fm.is_valid():
                unam=fm.cleaned_data.get("username")
                upas=fm.cleaned_data.get("password")
                user=authenticate(username=unam,password=upas)
                if user is not None:
                    login(request,user)
                    messages.success(request,"Congratulations!!!!! now you beacome an author")
                    return HttpResponseRedirect("/dashboard/")
        else:
            fm=user_log()
        return render(request,"user_login.html",{"fm":fm})
    else:
        return HttpResponseRedirect("/dashboard/")

def user_logout(request):
    if request.user.is_authenticated:
        request.session.flush()
        logout(request)
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/login/")

def update(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=Post.objects.get(pk=id)
            fm=update_post(request.POST,instance=pi,)
            if fm.is_valid():
                fm.save()
                messages.success(request,"your updated blog is now live")
                return HttpResponseRedirect("/dashboard/")
        else:
            pi=Post.objects.get(pk=id)
            fm=update_post(instance=pi)
        return render(request,"update.html",{"form":fm})
    else:
        return HttpResponseRedirect("/login/")
    
def del_post(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect("/dashboard/")
    else:
        return HttpResponseRedirect("/login/")
    
def add_blog(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=update_post(request.POST)
            if fm.is_valid():
                tit=fm.cleaned_data.get("titel")
                des=fm.cleaned_data.get("desc")
                uts=Post(titel=tit,desc=des)
                uts.save()
                messages.success(request,"your new blog is now ready")
                return HttpResponseRedirect("/dashboard/")
        else:
            fm=update_post()
        return render(request,"add.html",{"form":fm})
    else:
        return HttpResponseRedirect("/login/")