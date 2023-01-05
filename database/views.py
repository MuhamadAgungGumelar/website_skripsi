from random import choice
from django.shortcuts import redirect, render
from django.views import View
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required, permission_required

import os
from PIL import Image

from keras.models import load_model
from keras_preprocessing import image
import tensorflow as tf
import numpy as np

from mywebsite.forms import MainForm

from .models import PostModel
from .forms import PostForm


model_graph = tf.compat.v1.Graph()
with model_graph.as_default():
    tf_session = tf.compat.v1.Session()
    with tf_session.as_default():
        model = load_model('models/model_hybrid4.h5')

def delete(request, delete_id):
    PostModel.objects.filter(id=delete_id).delete()
    return redirect('database:index')

def update(request, update_id):
    image_update = PostModel.objects.filter(id=update_id).first()
    post_model = PostModel.objects.all()

    data={
        'category'  : image_update.category,
        'gambar'  : image_update.gambar,
    }
    post_form = PostForm(request.POST or None, request.FILES or None, initial=data, instance=image_update)

    if request.method == 'POST':
        if post_form.is_valid():
            post_form.save()

        return redirect('database:index')    

    context = {
        "Judul" : "Database of Lung Disease Detection",
        "Subjudul" : "Database Page",
        'nav': [
            ['/','home'],
            ['/database','database']
        ],
        'Post_Model':post_model,
        'Post_Form':post_form,
    }
    return render(request, 'database/index_user.html', context)

def images2(request, slugInput):
    #query
    post_model = PostModel.objects.get(slug=slugInput)
    print("cekkkkkkkkkkkkkkkkk")
    print(post_model)

    context = {
        "Judul" : "Database of Lung Disease Detection",
        "Subjudul" : "Database Page",
        'nav': [
            ['/','home'],
            ['/database','database']
        ],
        'Post_Model':post_model,
        # 'Post_Form':post_form,
    }
    return render(request, 'database/images2.html', context)

def images(request, slugInput):
    #query
    post_model = PostModel.objects.filter(slug=slugInput).first()
    print("cekkkkkkkkkkkkkkkkk")
    print(post_model)

    context = {
        "Judul" : "Database of Lung Disease Detection",
        "Subjudul" : "Database Page",
        'nav': [
            ['/','home'],
            ['/database','database']
        ],
        'Post_Model':post_model,
        # 'Post_Form':post_form,
    }
    return render(request, 'database/images.html', context)

def predictImage(request):
    if request.method == 'POST':
        main_form = MainForm(request.POST, request.FILES)
        if main_form.is_valid():
            
            simpan=request.FILES['gambar']
            fs=FileSystemStorage()
            Path_Gambar=fs.save(simpan.name,simpan)
            Path_Gambar=fs.url(Path_Gambar)


            testimage = 'database/images/' + Path_Gambar
            img = image.load_img(testimage, target_size=(224,224))
            xray_image = image.img_to_array(img)
            xray_image=xray_image/225
            xray_image=xray_image.reshape(1,224,224,3)
            with model_graph.as_default():
                with tf_session.as_default():
                    prediksi = model.predict(xray_image)

            hasil=int(np.argmax(prediksi,axis=1))
            # probability = max(prediksi.tolist()[0])
            # probability = probability*100

            p = PostModel(category="COVID19", gambar=Path_Gambar)
            q = PostModel(category='Normal', gambar=Path_Gambar)
            r = PostModel(category='Tuberculosis', gambar=Path_Gambar)
            s = PostModel(category='Pneumonia', gambar=Path_Gambar)
            
            if hasil==0:
                hasil=p.category
                p.save()
            elif hasil==1:
                hasil=q.category
                q.save()
            elif hasil==2:
                hasil=r.category
                r.save()
            elif hasil==3:
                hasil=s.category
                s.save()

    template_name=None
    if request.user.is_authenticated():
        template_name= 'index_user.html'
    else:
        template_name= 'index_anonymous.html'

    context = {
            'Top' : 'Lung Disease Website',
            'Judul': 'Lung Disease Detection ',
            'Subjudul' : 'Main Page',
            'Main_Form' : main_form,
            'Path_Gambar':Path_Gambar,
            'Hasil':hasil,
            # 'probability':probability,
            #'Main_model':main_model,
           
            'nav': [
                ['/','home'],
                ['/database','database']
            ],
            
        }
    return render(request, template_name, context)

@login_required(login_url='login')
def index(request):
    #query
    post_model = PostModel.objects.all()

    post_form = PostForm(request.POST, request.FILES)

    template_name=None
    if request.user.is_authenticated():
        template_name= 'database/index_user.html'
    else:
        template_name= 'database/index_anonymous.html'
    
    if request.method == 'POST':
        if post_form.is_valid():
            post_form.save()

        #     simpan = request.FILES['gambar']
        #     fss=FileSystemStorage()
        #     Path_Gambar=fss.save(simpan.name,simpan)
        #     Path_Gambar2=fss.url(Path_Gambar)

        # else:
        #     post_model

        return redirect('database:index')    

    context = {
        "Judul" : "Database of Lung Disease Detection",
        "Subjudul" : "Database Page",
        'nav': [
            ['/','home'],
            ['/database','database']
        ],
        'Post_Model':post_model,
        'Post_Form':post_form,

        
    }
    return render(request, template_name, context)



