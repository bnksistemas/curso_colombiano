from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'
    login_url='/admin'


"""
 esta linea estaba anteriormente y nos permía direccionar el archivo padre ubicado en la carpeta
 template del proyecto (la plantilla hija esta ubicada en la carpeta template de la aplicacion)

    template_name='base/base.html' #busca en archivo raiz la carpeta template y luego otra base
"""
