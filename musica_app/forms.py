from django import forms
from .models import Artista, Album, PerfilRedesSociales, SelloDiscografico

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['nombre', 'nacionalidad', 'genero_musical', 'perfil', 'sello']

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['titulo', 'fecha_lanzamiento', 'genero', 'artistas']

class PerfilRedesSocialesForm(forms.ModelForm):
    class Meta:
        model = PerfilRedesSociales
        fields = ['instagram', 'facebook', 'twitter']

class SelloDiscograficoForm(forms.ModelForm):
    class Meta:
        model = SelloDiscografico
        fields = ['nombre']
