# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from models import Create, CreateUser
from forms import CreateForm, MyRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.views.generic import CreateView
from pymongo import MongoClient
client = MongoClient()
db = client['my_database']


class CreateUserView(CreateView):
	model=CreateUser
	template_name = 'createuser_form.html'

def home(request):
	html = 'welcome to django'
	return HttpResponse(html)

def Contact_Create(request):
	if request.POST:
		form = CreateForm(request.POST)
		if form.is_valid():
			a = form.save()

			messages.add_message(request, messages.SUCCESS, "You Data was added")
			return HttpResponseRedirect('/users/all')

	else:
		form = CreateForm()

	args = {}
	args.update(csrf(request))
	args['form'] = form

	return render_to_response('create_list.html', args)

def users(request):
	args = {}
	args.update(csrf(request))

	args['users'] = db.auth_user.find()

	return render_to_response('users.html', args) 

def loginuser(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')

@login_required
def loggedin(request):
	args = {}
	args.update(csrf(request))
	username = request.user.username
	args['users'] = db.auth_user.find({'username':{'$ne':username}},{"username":1,"first_name":1,"last_name":1,"email":1})
	args['full_name'] = request.user.username
	return render_to_response('loggedin.html', args)

def invalid_login(request):
	return render_to_response('invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')

def register_user(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/register_success')
	else:
		form = MyRegistrationForm()
	args = {}
	args.update(csrf(request))    
	args['form'] = form
	
	return render_to_response('register.html', args)

def register_success(request):
	return render_to_response('register_success.html')

def particularuser(request,user_id=1):
	username =user_id
	user = request.user.username
	if user != username:
		args = {}
		args['users'] = db.auth_user.find({'username':username},{"username":1,"email":1})
		args['person'] = user
		return render_to_response('details.html', args)
	else:
		return HttpResponse('You can see your details in your profile')

@login_required
def edituser(request,user_name=1):
	username = user_name
	user = db.auth_user.find({'username':user_name},{"first_name":1,"last_name":1, "_id":0,"username":1,"email":1})
	if request.POST:
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			a = db.auth_user.update({'username':username},{'$set':{'username':form.data['username'],'first_name':form.data['first_name'],'last_name':form.data['last_name'],'email':form.data['email']}})
			return HttpResponseRedirect('/accounts/loggedin')
		else:
			a = db.auth_user.update({'username':username},{'$set':{'username':form.data['username'],'first_name':form.data['first_name'],'last_name':form.data['last_name'],'email':form.data['email']}})
			return HttpResponseRedirect('/accounts/loggedin')
		
	else:
		form = MyRegistrationForm()

	args = {}
	args.update(csrf(request))
	data = user	
	for info in data:
		form.fields["first_name"].initial = info['first_name']
		form.fields["last_name"].initial = info['last_name']
		form.fields["username"].initial = info['username']
		form.fields["email"].initial = info['email']
	args['form'] = form
	args['user'] = user_name
	return render_to_response('edit.html', args)

def deleteuser(request,user_name=1):
	query = db.auth_user.remove({'username':user_name})
	return HttpResponseRedirect('/accounts/loggedin')

def getdistrict(request):
	args={}
	return render_to_response('loggedin.html',args)