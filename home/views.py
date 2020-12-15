import random
from django.shortcuts import render
from django.http import HttpResponse
from home import views
from home import models

n1 = models.blogers()
n1.title = 'Title 1'
n1.description = 'Blog 1'
n1.Blogid = 'Author 1'
n1.category = 'other'
n2 = models.blogers()
n2.title = 'Title 2'
n2.description = 'Blog 2'
n2.Blogid = 'Author 2'
n2.category = 'fashion'
n3 = models.blogers()
n3.title = 'Title 3'
n3.description = 'Blog 3'
n3.Blogid = 'Author 3'
n3.category = 'fashion'
n4 = models.blogers()
n4.title = 'Title 4'
n4.description = 'Blog 4'
n4.Blogid = 'Author 4'
n4.category = 'sports'
dests = [n1,n2,n3,n4]

def fillBlog(request):
    title = request.POST['title']
    blogDat = request.POST['blogData']
    category = request.POST['category']
    name = request.POST['Name']
    if(title == '' or blogDat == '' or name == ''):
        return home(request)
    
    l =[]
    while True:
        n = random.randint(1,1000000000000000000000)
        if n not in l:
            l.append(n)
            n = models.blogers()
            n.title = title
            n.description = blogDat
            n.Blogid = name
            n.category = category
            dests.append(n)
            break
    return render(request,'succes.html')
            

def category(request):
    cat = request.GET['cat']
    y = []
    for i in dests:
        if i.category == cat:
            y.append(i)
    return render(request,'filtered.html',{'dest1':y})



# Create your views here.
def home(request):
   
   return render(request,'index.html',{'dest1':dests})
def MyPost(request):
    x=[]
    for i in dests:
        if i.Blogid == 'Abhinav':
            x.append(i)

    return render(request,'myPost.html',{'dest1':x})
def Contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def search(request):
    return render(request,'search.html')
def addBlog(request):
    return render(request,'AddBlog.html')
