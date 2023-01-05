from dataclasses import field
from django import forms
from database.models import PostModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MainForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = [
            'gambar',
            
            
        ]
        
        labels={
         'gambar':'Image :',
         
      }

        widget={
         'gambar' : forms.FileInput(attrs={'class': 'form-control'}),
      }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']























# <div class="input-group">
#                         {% for component in Main_Form.upload%}
#                             <div class="custom-file">
#                                 {{component.tag}}
#                                 <label for="component.id_for_label" class="custom-file-label">
#                                     {{component.choice_for_label}}
#                                 </label>
#                             </div>
#                         {% endfor %}
#                         <div class="input-group-append">
#                             <button class="btn btn-outline-secondary" type="submit" id="Label Submit">Upload</button>
#                         </div>
#                 </div>