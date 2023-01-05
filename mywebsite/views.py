from re import template
from django.shortcuts import render, redirect
from django.views.generic.base import RedirectView, TemplateView

from .forms import MainForm, CreateUserForm
from database.models import PostModel


from django.core.files.storage import FileSystemStorage

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# from django.core.mail import send_mail

# send_mail(
#     'Subject here', 'Here is the message.', 'from@example.com',
#     ['to@example.com'], fail_silently=False,
# )


def Login(request):
    # main_form = MainForm(request.POST, request.FILES)

    if request.method == "POST":
        username_login = request.POST['username']
        password_login = request.POST['password']

        user = authenticate(request, username=username_login, password=password_login)

        if user is not None:
            login(request, user)
        
        return redirect('database:index')
     
    if request.method == "GET":
        if request.user.is_authenticated():
            return redirect('index')

    context = {
            'Top' : 'Login',
            'Judul': 'Login',
            'Subjudul' : 'Second Page',
            # 'Main_Form' : main_form,
           
            'nav': [
                ['/','home'],
                ['/database','database']
            ],
            
        }
    return render(request, 'login.html', context)


@login_required(login_url='index')
def Logout(request):
    # main_form = MainForm(request.POST, request.FILES)

    if request.method == "POST":
        if request.POST["logout"] == "Submit":
            logout(request)
        
        return redirect('index')
        

    context = {
            'Top' : 'Logout',
            'Judul': 'Halaman Logout',
            'Subjudul' : 'Halaman Untuk Logout',
            # 'Main_Form' : main_form,
           
            'nav': [
                ['/','home'],
                ['/database','database']
            ],
            
        }
    return render(request, 'logout.html', context)

def Registration(request):
    registration_form = CreateUserForm(request.POST)
    if request.method == "POST":
        
        if registration_form.is_valid():
            registration_form.save()
            return redirect('login')


    context = {
            'Top' : 'Sign Up',
            'Judul': 'Sign Up',
            'Subjudul' : 'Sign Up Page',
            'registration_form' : registration_form,
           
            'nav': [
                ['/','home'],
                ['/database','database']
            ],
            
        }
    return render(request, 'regist.html', context)



def index(request):
    main_form = MainForm(request.POST, request.FILES)

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
           
            'nav': [
                ['/','home'],
                ['/database','database']
            ],
            
        }
    return render(request, template_name, context)












































































# model_graph = tf.compat.v1.Graph()
# with model_graph.as_default():
#     tf_session = tf.compat.v1.Session()
#     with tf_session.as_default():
#         model = load_model('models/model_densenet_1_100epoch.h5')

# def predictImage(request):
#     p = PostModel(category='COVID19')
#     q = PostModel(category='Normal')
#     r = PostModel(category='Tuberculosis')
#     s = PostModel(category='Pneumonia')

#     if request.method == 'POST':
#         main_form = MainForm(request.POST, request.FILES)
#         if main_form.is_valid():
#             main_form.save()
#             simpan=request.FILES['gambar']
#             fs=FileSystemStorage()
#             Path_Gambar=fs.save(simpan.name,simpan)
#             Path_Gambar=fs.url(Path_Gambar)

#             testimage = 'database/images/' + Path_Gambar
#             img = image.load_img(testimage, target_size=(224,224))
#             xray_image = image.img_to_array(img)
#             xray_image=xray_image/225
#             xray_image=xray_image.reshape(1,224,224,3)
#             with model_graph.as_default():
#                 with tf_session.as_default():
#                     prediksi = model.predict(xray_image)

#             hasil=int(np.argmax(prediksi,axis=1))

#             if hasil==0:
#                 hasil=p.category
#                 p.save()
#             elif hasil==1:
#                 hasil=q.category
#                 q.save()
#             elif hasil==2:
#                 hasil=r.category
#                 r.save()
#             elif hasil==3:
#                 hasil=s.category
#                 s.save()

            
            
            
#     context = {
#             'Top' : 'Deteksi Paru-paru',
#             'Judul': 'Halaman Utama',
#             'Subjudul' : 'Halaman Untuk Deteksi Paru-Paru',
#             'Main_Form' : main_form,
#             'Path_Gambar':Path_Gambar,
#             'Hasil':hasil,
#             #'Main_model':main_model,
           
#             'nav': [
#                 ['/','home'],
#                 ['/database','database']
#             ],
            
#         }
#     return render(request, 'index.html', context)


















# media = 'media'




# def prediction(path):



    # if request.method == 'POST' and request.FILES['upload']:

    #     if 'upload' not in request.FILES:
    #         notif = 'Tidak ada Image yang dipilih'
    #         return render(request, 'index.html', context)
    #     b = request.FILES['upload']
    #     if b == '':
    #         notif ='Tidak ada File yang dipilih'
    #         return render(request, 'index.html', context)
    #     upload = request.FILES['upload']
    #     fss=FileSystemStorage()
    #     file = fss.save(upload.name, upload)
    #     file_url=fss.url(file)
    #     prediksi=prediction(os.path.join(media,file))
    #     return render(request, 'index.html', context)

    # else:
        
    #     return render(request, 'index.html', context)
        











# #class ParameterView(TemplateView):

#     #def get_context_data(self, *args, **kwargs):

#         #main_form = MainForm()
#         #post_form = PostForm()

#         #context = super().get_context_data(**kwargs)
#         #context ['Top'] = 'Deteksi Paru-paru'
#         context ['Judul'] = 'Halaman Utama'
#         context ['Subjudul'] = 'Halaman Untuk Deteksi Paru-Paru'
#         context ['Main_Form'] = main_form
#         context ['/'] = ['home']
#         context ['/database'] = ['database']
        
#         return context













