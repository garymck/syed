from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm, SignUpForm
from .models import SignUp

# Create your views here.
def home(request):
	title = 'Sign Up Now'
	form = SignUpForm(request.POST or None)
	context = {
		"title": title,
		"form": form
	}
	if form.is_valid():
		
		instance = form.save(commit=False)

		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		
		instance.save()
		context = {
			"title": "Thank you"
		}

	if request.user.is_authenticated() and request.user.is_staff:
		

		queryset = SignUp.objects.all().order_by('-timestamp') 
		context = {
			"queryset": queryset
		}

	return render(request, "home.html", context)



def contact(request):
	title = 'Contact Us'
	title_align_center = True
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# for key, value in form.cleaned_data.iteritems():
		# 	print key, value
		# 	#print form.cleaned_data.get(key)
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		# print email, message, full_name
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, '']
		contact_message = "%s: %s via %s"%( 
				form_full_name, 
				form_message, 
				form_email)
		some_html_message = """
		<h1>hello</h1>
		"""
		send_mail(subject, 
				contact_message, 
				from_email, 
				to_email, 
				html_message=some_html_message,
				fail_silently=True)

	context = {
		"form": form,
		"title": title,
		"title_align_center": title_align_center,
	}
	return render(request, "forms.html", context)


def mobiles(request):
	return render(request,'mobiles.html',{})


def laptops(request):
	return render(request,'laptops.html',{})

def gaming(request):
	return render(request,'gaming.html',{})



def apple(request):
	return render(request,'apple.html',{})


def tomclansy(request):
	return render(request,'tomclansy1.html',{})

def witcher(request):
	return render(request,'witcher.html',{})

def sniper(request):
	return render(request,'sniper.html',{})


def forhonor(request):
	return render(request,'forhonor.html',{})


def zero(request):
	return render(request,'zero.html',{})

def mirror(request):
	return render(request,'mirror.html',{})

def dead(request):
	return render(request,'dead.html',{})

def king(request):
	return render(request,'king.html',{})

def mafia(request):
	return render(request,'mafia.html',{})