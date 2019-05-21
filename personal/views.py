from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic import View
from . forms import UserForm,ProductForm,RecycleForm
from . models import Product,Recycle
from django.views.generic.edit import CreateView

def main(request):
    return render(request,'personal/home2.html')

def contact(request):
    return render(request,'personal/contact.html')

@login_required(login_url='/signin/')
def mainin(request):
    return render(request,'personal/homelogin.html')

@login_required(login_url='/signin/')
def contactin(request):
    return render(request,'personal/contactlogin.html')

def signin(request):
    return render(request,'personal/signin.html')


class IndexView(generic.ListView):
    template_name = 'personal/index.html'
    context_object_name = 'all_products'

    def get_queryset(self):
        return Product.objects.all()

class DetailView(generic.DetailView):
    model = Product
    template_name ='personal/detailview.html'

class SumitProduct(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'personal/product_form.html'


class RecycleProduct(CreateView):
    model = Recycle
    form_class = RecycleForm
    template_name = 'personal/Recycle_form.html'

class DetailViewRecycle(generic.DetailView):
    model = Recycle
    template_name ='personal/detailviewrecycle.html'


class UserFormView(View):
    form_class=UserForm
    template_name='personal/registration_form.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():

            user=form.save(commit=False)
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user=authenticate(username=username,password=password)


            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('signin')
        return render(request, self.template_name, {'form':form})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'personal/afterlogin.html',{'Product.objects.all()':Product.objects.all()})
            else:
                return render(request, 'personal/signin.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'personal/signin.html', {'error_message': 'Invalid login'})

    return render(request, 'personal/signin.html')

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'personal/signin.html', context)

@login_required(login_url='/signin/')
def buynow(request):
    return render(request,'personal/buynow.html')















