from django.shortcuts import render
from django.template import Context, loader 
from django.http import HttpResponse 
from models import UserLink  

def alluser(request):
  lis = UserLink.objects.all()
  t = loader.get_template('my_social_network/templates/alluser.html')
  c = Context({'lis':lis,})
  return HttpResponse(t.render(c))

def allfollowers (request , username):
  f_lis = UserLink.objects.filter(to_user__username = username)
  #lis = []
  #for i in link: 
    #if i.to_user.username == username; 
    #lis.append(i.from_user)
  t = loader.get_template('my_social_network/templates/msn/followers.html')      
  c = Context({'f_lis':f_lis})
  return HttpResponse(t.render(c))

def allfollowing (request, username): 
  fo_lis = UserLink.objects.filter(from_user__username = username)
  #lis = []
  #for i in link:
    #if i.to_user.username == username;
    #lis.append(i.from_user)
  t = loader.get_template('my_social_network/templates/msn/following.html')
  c = Context({'fo_lis':fo_lis})
  return HttpResponse(t.render(c))
  