from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_view
from django.contrib.auth import logout
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	try:
		username = request.session['user']
	except:
		return render(request, 'signin.html')
	
	context = {'text' : username}
	return render(request, 'index.html', context)

def signup(request):
	return render(request, 'signup.html')


def register(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		password = request.POST.get('password')
		password_again = request.POST.get('password_again')

		if password == password_again:
			try:
				user = User.objects.create_user(name, email, password)
				user.save()
				return redirect('/')
			except:
				context = {'text': 'Username already existed. Please try again'}
				return render(request, 'signup.html', context)
		else:
			context = {'text': 'Password not matched'}
			return render(request, 'signup.html', context)

		return render(request, 'signup.html')

def login(request):
	if request.method == 'POST':
		username = request.POST.get('name')
		password = request.POST.get('password')
		print(username, password)
		user = authenticate(username = username, password = password)

	if user is not None:
		request.session['user'] = username
		request.session['id'] = request.user.id
		return redirect('/')

	else:
		context = {'error': 'Please check your credentials'}
		return render(request, 'signin.html', context)

def logout(request):
	request.session['user'] = None
	request.session.flush()
	return redirect('/')