# NOTAS:
# full_clean(): Llama a todas las validaciones del modelo antes de guardar los datos en la base de datos.
# Método save(): Usamos super().save(commit=False) para crear una instancia del modelo sin guardarla en la base de datos de inmediato. 
# Esto permite ejecutar full_clean() primero y después guardar solo si los datos son válidos


from django import forms
from .models import Artista, Album, PerfilRedesSociales, SelloDiscografico

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['nombre', 'nacionalidad', 'genero_musical', 'perfil', 'sello']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.full_clean()  # Ejecuta las validaciones del modelo
        if commit:
            instance.save()
        return instance



class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['titulo', 'fecha_lanzamiento', 'genero', 'artistas'] 

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.full_clean()
        if commit:
            instance.save()
        return instance
    
    
    

class PerfilRedesSocialesForm(forms.ModelForm):
    class Meta:
        model = PerfilRedesSociales
        fields = ['instagram', 'facebook', 'twitter']
        
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.full_clean()
        if commit:
            instance.save()
        return instance



class SelloDiscograficoForm(forms.ModelForm):
    class Meta:
        model = SelloDiscografico
        fields = ['nombre']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.full_clean()
        if commit:
            instance.save()
        return instance