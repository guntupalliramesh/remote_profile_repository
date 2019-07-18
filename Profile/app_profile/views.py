from django.shortcuts import render
from .models import ProfileReg
from django.core.mail import EmailMessage
from Profile import settings as se



def index_profile(request):
    return render(request,'index.html')



def profile_Save(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        cno = request.POST.get("pnum")
        email = request.POST.get("email")
        sub = request.POST.get("subject")
        mes = request.POST.get("message")

        mess_age = smsACASMSotp(fname,cno)
        import json
        d1 = json.loads(mess_age)
        if d1['return']:
            to = email
            emails = list(to.split(','))
            em = EmailMessage(fname,mes,se.EMAIL_HOST_USER,emails)
            em.send(False)
            ProfileReg(first_name=fname,last_name=lname,contact_no=cno,email=email,subject=sub,message=mes).save()
            return render(request,'index.html',{"MES":"Your Response is Successfully Submitted"})
        else:
            return render(request,'index.html',{"MES": "Inavild Contact_No"})

def smsACASMSotp(fname,cno):
    import requests
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS&message=Hello,Mr./Ms. "+ str(fname)+ ", Thankyou for your attention" +"&language=english&route=p&numbers=" + cno
    headers = {
        'authorization': "vMDYfrjnLJs2XC41tPhqkAamHz6oZuNRWc93gpIx8SEKUQ0BFGNnbIdrv9OoS8uk4TCAYighwlsV0tW2",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    return response.text