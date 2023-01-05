from tkinter import Widget
from django import forms

from .models import PostModel

#class PostForm(forms.Form):
   #nama = forms.CharField(max_length=255)
   #keterangan = forms.CharField()
   #gambar = forms.ImageField()
   
class PostForm(forms.ModelForm):
   class Meta:
      model = PostModel
      fields = [
         'gambar',
         'category',
      ]

      labels={
         'gambar':'Image :',
         'category':'Category :',
      }

      # widget={
      #    'id_gambar' : forms.FileInput(
      #       attrs={
      #          'class':'form-control'}
      #    ),

      #    'id_category' : forms.Select(
      #       attrs={
      #          'class':'form-select'}
      #    ),
      # }
         
      