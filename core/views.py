from django.shortcuts import render, redirect
from .models import Appointment, Contact
from django.core.mail import send_mail
from ourdoctors.models import Doctor
from ourblogs.models import Blog
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


def our_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'team.html', {'doctors': doctors})

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})



def index(request):
    doctors = Doctor.objects.all()
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'doctors': doctors, 'blogs': blogs})

def appointment(request):
    if request.method == "POST":
        Appointment.objects.create(
            department=request.POST.get("department"),
            doctor=request.POST.get("doctor"),
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            date=request.POST.get("date"),
            time=request.POST.get("time"),
        )
        return redirect("index")
    return render(request, "appointment.html")

def contact(request):
    if request.method == 'POST':
        # HTML form se data lena (same as tumhare input names)
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save contact to database
        allData = Contact(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        allData.save()

        # ---------- Email to User (Confirmation) ----------
        html_content_user = render_to_string('email_template.html', {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        })

        text_content_user = (
            f"Dear {name},\n\n"
            "Thank you for contacting Sangam University.\n"
            "We have received your message and will get back to you soon.\n\n"
            "Best regards,\nSangam University Support Team"
        )

        try:
            user_email = EmailMultiAlternatives(
                subject=f"Thank You for Contacting Us - {subject}",
                body=text_content_user,
                from_email="lalitpandit7474@gmail.com",  # same as EMAIL_HOST_USER
                to=[email],
            )
            user_email.attach_alternative(html_content_user, "text/html")
            user_email.send(fail_silently=False)

            # ---------- Email to Admin ----------
            admin_subject = f"New Contact Form Submission from {name}"
            admin_message = (
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Subject: {subject}\n"
                f"Message:\n{message}\n"
            )

            admin_email = EmailMultiAlternatives(
                subject=admin_subject,
                body=admin_message,
                from_email="lalitpandit7474@gmail.com",
                to=["lalitpandit7474@gmail.com"],  
            )
            admin_email.send(fail_silently=False)

            messages.success(request, "Your message has been sent successfully!")

        except Exception as e:
            print("❌ Email error:", e)
            messages.error(request, "Sorry, we couldn't send your message. Please try again.")

        return redirect('/contact/')
    
    return render(request, 'contact.html')

def service(request):
    return render(request,'service.html')
def detail(request):
    return render(request,'detail.html')
def about(request):
    return render(request,'about.html')
def price(request):
    return render(request,'price.html')
def search(request):
    return render(request,'search.html')
def testimonial(request):
    return render(request,'testimonial.html')