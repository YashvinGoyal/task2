#task1 12345
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from  home.models import profile,bloggg
import os
from django.core.files.storage import FileSystemStorage
# Create your views here.
def loginn(request):
    if request.method=='POST':
        namee=request.POST['namey']
        pass1=request.POST['passwordd']
        userr=authenticate(username=namee,password=pass1)
        if userr is not None:
            myprof=profile.objects.filter(uname=namee).first()
            cont={'myprof':myprof}
            login(request,userr)
            return render(request,f"{myprof.work}.html",cont)
        else:
            return HttpResponse("WRONG CRENDITALS")
            #return render(request,'login.html') 
            # return redirect('fakd_login')            
    
    return render(request,'login.html')    

def signup(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        emaill=request.POST['email']
        namee=request.POST['name']
        uploaded_file = request.FILES['document']
        # print(uploaded_file)
        # savefile= FileSystemStorage() 
        # name = savefile.save( namee,uploaded_file)# this is the name of file
        # #know where to save the file
        # print(name)
        # d = os.getcwd() #current directory of the project
        # file_directory = d+'\files\\'+name
        
        pass1=request.POST['password']
        pass2=request.POST['cnfpassword']
        add=request.POST['add']
        d=request.POST.get('doc','off')
        p=request.POST.get('pat','off')
        if pass1!=pass2:
           return HttpResponse("PASSWORD AND CONFRIM PASSWORD DONOT MATCH")
        myuser=User.objects.create_user(namee,emaill,pass1)
        myuser.save()
        print(d,p)
        if d=="on":
            work="doctor"
            myprof=profile(fname=fname,lname=lname,email=emaill,uname=namee,password=pass1,img=uploaded_file,address=add,work=work)
        else:
            work1="patient"
            myprof=profile(fname=fname,lname=lname,email=emaill,uname=namee,password=pass1,img=uploaded_file,address=add,work=work1)   
        myprof.save()       
        return render(request,'login.html') 
        
    return render(request,'signup.html')

def logoutt(request):
    logout(request)
    return render(request,'login.html') 
   
def dash(request):
    namee=request.user.username
    myprof=profile.objects.filter(uname=namee).first()
    cont={'myprof':myprof}
    return render(request,f"{myprof.work}.html",cont)
    
def blog(request):
    user=request.user
    if request.method=='POST':
        title=request.POST['title']
        uploaded_file = request.FILES['docum']
        d=request.POST.get('draftt','off')
        d1=request.POST.get('m1','off')
        d2=request.POST.get('m2','off')
        d3=request.POST.get('m3','off')
        d4=request.POST.get('m4','off')
        summ=request.POST.get('text1','off')
        cont=request.POST.get('text2','off')   
        if d1=="on":
            blogg=bloggg(user=user,title=title,img=uploaded_file,cat="Mental Health",summ=summ,con=cont)
        elif d2=="on":
            blogg=bloggg(user=user,title=title,img=uploaded_file,cat="Heart Disease",summ=summ,con=cont)
        
        elif d3=="on":
            blogg=bloggg(user=user,title=title,img=uploaded_file,cat="Covid-19",summ=summ,con=cont)  
        else:
            blogg=bloggg(user=user,title=title,img=uploaded_file,cat="Immunization",summ=summ,con=cont)  
        print(d1,d2,d3,d4,d)
        if d=="on":
            blogg.draft=True
        else:
            blogg.draft=False 
        blogg.save()
        return redirect('dash')
    return render(request,'blog.html')

def viewd(request):
    userr=request.user
    allPosts=bloggg.objects.filter(user=userr)
    dictt={'allPosts':allPosts}
    return render(request,'blogd.html',dictt)
  
def viewp(request):
    a1=bloggg.objects.filter(draft=False,cat="Mental Health")
    a2=bloggg.objects.filter(draft=False,cat="Heart Disease")
    a3=bloggg.objects.filter(draft=False,cat="Covid-19")
    a4=bloggg.objects.filter(draft=False,cat="Immunization")
    
    dictt={'a1':a1,'a2':a2,'a3':a3,'a4':a4}
    return render(request,'blogp.html',dictt)

def blogpost(request,sno):
    blg=bloggg.objects.filter(sno=sno).first()
    liss={'blg':blg}
    return render(request,'blogpost.html',liss)