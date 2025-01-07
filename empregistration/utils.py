# empregistration/utils.py



from django.core.mail import send_mail
import random

def generateOtp():
    return str(random.randint(100000, 999999))

def sendOtp_email(email, otp):
    subject = "Your OTP Verification Code"
    message = f"Your OTP code is {otp}. Please use this to complete your registration."
    send_mail(subject, message, 'manasharma767@gmail.com', [email])
