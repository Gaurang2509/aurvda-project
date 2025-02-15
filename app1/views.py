from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def service(request):
    return render(request,"service.html")

def blog(request):
    return render(request,"blog.html")

def contact(request):
    return render(request,"contact.html")

#admin views

def index1(request):
    return render(request,"admin/index1.html")

def client_profile(request):
    return render(request,"admin/client-profile.html")

def page_login(request):
    return render(request,"admin/pages-login.html")

def send_suggestions(request):
    return render(request,"admin/send-suggestions.html")

def users_profile(request):
    return render(request,"admin/users-profile.html")

def view_documents(request):
    return render(request,"admin/view-documents.html")

def view_receive_payment(request):
    return render(request,"admin/view-receive-payment.html")

def view_suggestions(request):
    return render(request,"admin/view-suggestions.html")

# client urls

def client_index(request):
    return render(request,"client/index2.html")

def payment_info(request):
    return render(request,"client/payment-info.html")

def profile(request):
    return render(request,"client/profile.html")

def send_document(request):
    return render(request,"client/send-document.html")

def send_query(request):
    return render(request,"client/send-query.html")

