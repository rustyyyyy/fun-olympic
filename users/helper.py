import os
from pathlib import Path
import environ
import requests

from users.models import EmailVerification

from .models import CustomUser

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env_file = os.path.join(BASE_DIR, ".env")
environ.Env.read_env(env_file)

api_key = env("api_key")
import json
import random


def captcha_validation(recaptcha_response=None, secret=None):
    data = {"secret": secret, "response": recaptcha_response}

    r = requests.post("https://www.google.com/recaptcha/api/siteverify", data=data)
    result = r.json()

    if result["success"]:
        return True

    return False


def email_verification(email=None):

    otp_code = random.randint(111111, 999999)

    user = CustomUser.objects.get(email=email)
    new_user = EmailVerification(user=user, verification_code=otp_code, verified=False)
    new_user.save()

    url = "https://api.sendinblue.com/v3/smtp/email"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "api-key": api_key,
    }

    data = {
        "body": "Email Verification",
        "sender": {"name": "admin@funOlympic", "email": "maharjanajul18@gmail.com"},
        "subject": "Email Verification",
        "to": [{"email": f"{email}", "name": "Email verification"}],
        "textContent": f"Your verification code is {otp_code}",
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    # print(response)

    if response.status_code == 201:
        user = CustomUser.objects.get(email=email)
        user_id = EmailVerification.objects.get(user=user).id

        return user_id
    return False


def reset_email(email=None, user=None):

    password = generate_random_hash()

    url = "https://api.sendinblue.com/v3/smtp/email"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "api-key": api_key,
    }
    data = {
        "body": "Reset Password",
        "sender": {"name": "admin@funOlympic", "email": "maharjanajul18@gmail.com"},
        "subject": "Email Verification",
        "to": [{"email": f"{email}", "name": "Reset Password"}],
        "textContent": f"Your reseted password is {password}",
    }
    
    # print(password)
    # print(user)
    if email != None:
        # print("sent")
        response = requests.post(url, headers=headers, data=json.dumps(data))
        user.set_password(password)
        user.save()

        if response.status_code == 201:
            print("sent")


def generate_random_hash():
    import random, string
    hash1 = ''.join(random.sample(string.ascii_letters + string.digits, 32))
    return hash1
