from django.shortcuts import render
from django.views import View



# Create your views here.

def login(request):
    return render(request,'users/login.html')
#
# def register(request):
#     return render(request,'users/register.html')

#用到渲染模板和提交数据用类视图比较多
class RegisterView(View):
    """
    /register/
    """
    def get(self,request):
        return render(request,'users/register.html')