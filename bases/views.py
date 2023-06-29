from django.shortcuts import render
from django.views import generic

# Create your views here.
class Home(generic.TemplateView):
    template_name = 'bases/home.html'





   # template_name='bases/home.html' #busca en archivo raiz la carpeta template y luego otra base
"""
 esta linea estaba anteriormente y nos permía direccionar el archivo padre ubicado en la carpeta
 template del proyecto (la plantilla hija esta ubicada en la carpeta template de la aplicacion)

    template_name='base/base.html' #busca en archivo raiz la carpeta template y luego otra base
"""
