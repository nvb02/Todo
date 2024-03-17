from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo #importing todo class from models.py to interact with the data in database

# Create your views here.
def home(request): #creating function-based views, takes request argument in request parameter and returns a response, request parameter is compulsory for the function to be a view
    #return HttpResponse('Hello this is a home page!') #httpresponse takes string data from the paranthesis and displays or renders string data as an output in the web.
    todo = Todo.objects.all() # a query set - calling the 'Todo' model and using 'objects' as an Object Relation Manager and running the 'all()' method that fetches or retrieves all the data in a form of list type where every data is an object by requesting it from the database (Todo class/table) --> (objects.all) kind of SQL language or query is used indirectly through the use of 'objects' which converts the request into an SQL language. the fetched data is assigned to the variable 'todo'.
    content = {'todos':todo} #converting the todo variable into dictionary type and assigning it to the content variable in order to send the data to the index.html. a key 'todos' is defined in the dictionary so that todo data can be called later at html through the use of key 'todos'.
    return render(request, 'index.html', context=content) #render function displays templates from function or view, calling template 'index.html' to render function, render takes 2 arguments 1. request(coming from url to function, then function to pass it to render), 2. template to render ... this will give response. 3. "context=content" passes the content dictionary data to the html file.


def create(request): #receives arguments such as request body,user,data,nature as objects, request parameter is compulsory to view the webpage
    if request.method == 'POST': #all the data that is posted gets fetched in the POST attribute as a json file
        name = request.POST.get('name') #getting the value of name key from POST attribute from html file using the get method since it is a json file similar to that of dictionary..
        description = request.POST.get('description')
        status = request.POST.get('status')
        Todo.objects.create(name=name,description=description,status=status) # making a query through ORM, using or calling create method to query the method to create the data by sending value from each of the above defined variables to each of the parameters on the fields of the model.
        return redirect('home') # the redirect function is called from django.shortcuts class that requests for certain url (home in this case, which is defined as the name in the path of urls.py because for internal calling for redirection or calling url inside the project, url itself cannot be passed and the name parameter is used in the path statement of urls.py where we use the get method to fetch the value to be returned) and shows the response of the url on the webpage.
    return render(request,'create.html') #render function used to display html file as a type of httpresponse as a template. this is a GET method

def edit(request,pk): #defining edit function for an edit page and adding pk parameter to fetch a unique ID for the particular data to be edited from the home page (index.html)
    todo = Todo.objects.get(id=pk) #getting the value of ID field which is unique from Todo table or model that is equal to the value of pk parameter received from the front-end.
    if request.method == 'POST': #will change data only if post request comes leaving the get request condition, calling the method method of the request function.
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        todo.name = name
        todo.description = description
        todo.status = status #transferring the data inserted by the user to the field of the specific data provided with unique ID in the table or model.
        todo.save() #saving the changes made into the database through the save method.
        return redirect('home') #once saved, the page is redirected to home or index.html        
    content = {'todo':todo} # passing the received data from db as a dictionary to be sent to front-end.
    return render(request,'edit.html', context = content) #passing the dictionary content to the edit.html file.

def delete(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.delete() # deleting the data of the ID that matches with the PK sent from the front-end.
    return redirect('home')

def deleteall(request):
    todo = Todo.objects.all()
    todo.delete()
    return redirect('home')