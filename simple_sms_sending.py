# OTP based login system using Fast2Sms and Python

import random
import requests

Name=str(input("Enter your name  "))
Mobile_Num=(input("Enter your number "))

OTP = random.randint(1111,9999)
otp=OTP

url = "https://www.fast2sms.com/dev/bulk"
payload = f"sender_id=FSTSMS&message=Your OTP for login: &language=english&route=p&numbers={Mobile_Num}"
headers = {'authorization': "Your auth id from fast2sms website",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
user_otp = int(input("Enter OTP "))
try:
    if(otp == user_otp):
        print("OTP matched \nNumber successfully registered")
        #Data.extend([Name,Mobile_Num])
        #Data[Name]=Mobile_Num
    else:
        print("OTP not matched")
except:
    print("error sending message")

    
