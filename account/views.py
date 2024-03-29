from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . serializers import UserRegisterSerializer
from rest_framework.authtoken.models import Token
from django.contrib import messages
from django.contrib.auth.models import User
# email activate user accounts
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.urls import NoReverseMatch, reverse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, DjangoUnicodeDecodeError
# getting token from utils.py
from .utils import TokenGenerator, generate_token
# email 
from django.conf import settings
from django.core.mail import EmailMessage
# resetpassword generators
from django.contrib.auth.tokens import PasswordResetTokenGenerator
# threading
import threading

class EmailThread(threading.Thread):
    
    def __init__(self, email_message):
        self.email_message = email_message
        threading.Thread.__init__(self)
        
    def run(self):
        self.email_message.send()
        

@api_view(["POST",])
def user_register_view(request):
    if request.method == "POST":
        serializer = UserRegisterSerializer(data=request.data)
        
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            
            data['response'] = 'Account has been created'
            data['username'] = account.username
            data['email'] = account.email
            
            # Generate API token
            token = Token.objects.get(user=account).key
            data['token'] = token
            
            # Generate email token
            email_token = generate_token.make_token(account)
            
            current_site = get_current_site(request)
            
            # Create email message
            email_subject = "Activate Your Account"
            message = render_to_string('account/activate.html',{
                "user": account,
                "domain": current_site.domain,
                # 'domain':'127.0.0.1:8000',
                "uid": urlsafe_base64_encode(force_bytes(account.pk)),
                "email_token": email_token,  
            })
            email_message = EmailMessage(email_subject, message, settings.EMAIL_HOST_USER, [account.email])
            
            # Start a new thread to send the email
            EmailThread(email_message).start()
            
            # Display a success message to the user
            data['message'] = "Activate your account by clicking the link sent to your email."
            return Response(data, status=status.HTTP_201_CREATED)
        
        else:
            data = serializer.errors
            
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
 
        
@api_view(["GET"])
def activate_account(request, uidb64, email_token):
    try:
        uid = str(urlsafe_base64_decode(uidb64), 'utf-8')
        user = User.objects.get(pk=uid)
        
    except User.DoesNotExist:
        return Response({"Error": "Invalid activation link."}, status=status.HTTP_400_BAD_REQUEST)
    
    if generate_token.check_token(user, email_token):
        user.is_active = True
        user.save()
        return Response({"Message": "Account activated successfully."}, status=status.HTTP_200_OK)
        # return redirect('api/login/')
    else:
        return Response({"Error": "Invalid activation link."}, status=status.HTTP_400_BAD_REQUEST)
        # return render(request,'account/activatefail.html')
    
        
@api_view(["POST",])
def logout_user(request):
    if request.method == "POST":
        request.user.auth_token.delete()
        return Response({'Message':'You are logged out'}, status=status.HTTP_200_OK)
    
    
@api_view(["POST",])
def request_reset_email(request):
    if request.method == "POST":
        email = request.data.get("email")
        user = User.objects.filter(email=email).first()
        
        if user:
            current_site = get_current_site(request)
            email_subject = "Reset Your Password"
            message = render_to_string("account/request-reset-email.html",{
                "user": user,
                "domain": current_site.domain,
                # "domain": "127.0.0.1:8000",
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "rest_password_token": PasswordResetTokenGenerator().make_token(user),
            })
            
            email_message = EmailMessage(email_subject, message, settings.EMAIL_HOST_USER, [email])
            EmailThread(email_message).start()
            return Response({"message": "We have sent you an email with instructions on how to reset the password."}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "User with this email does not exist."}, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST",])
def set_new_password(request, uidb64, rest_password_token):
    if request.method == "POST":
        password = request.data.get("password")
        confirm_password = request.data.get("confirm_password")
        
        if not password or not confirm_password:
            return Response({"error": "Please provide both password and confirm_password fields."}, status=status.HTTP_400_BAD_REQUEST)
        
        if password != confirm_password:
            return Response({"error": "Password and confirm password do not match."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user_id = str(urlsafe_base64_decode(uidb64), "utf-8")
            user = User.objects.get(pk=user_id)
            
            if not PasswordResetTokenGenerator().check_token(user, rest_password_token):
                return Response({"error": "Password reset link is invalid."}, status=status.HTTP_400_BAD_REQUEST)
            
            user.set_password(password)
            user.save()
            return Response({"message": "Password reset success. Please log in with your new password."}, status=status.HTTP_200_OK)
        
        except User.DoesNotExist:
            return Response({"error": "User does not exist."}, status=status.HTTP_404_NOT_FOUND)
        