from django.db import models
from .models import *
from users.models import BasicUser
import datetime
from django.forms import ModelForm

class Post(models.Model):
    idUser1 = models.ForeignKey(BasicUser, null=False, related_name='writer', default=None)
    idUser2 = models.ForeignKey(BasicUser, null=False, related_name='receiver', default=None)
    comment = models.CharField(max_length=1000, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.id)

    @classmethod
    def delete_post(self, idPost, idUser):
        post = Post.objects.get(id=idPost)
        receiver = BasicUser.objects.get(id=str(post.idUser2))
        seguidos = Follower.objects.filter(idUser1=receiver.id)
        teSiguen = Follower.objects.filter(idUser2=receiver.id)
        user = BasicUser.objects.get(id=str(idUser))

        if str(post.idUser1) == str(idUser) or str(post.idUser2) == str(idUser):
            post.delete()
        else:
            print("Estás eliminando un mensaje que no ha sido escrito por ti.")

        posts = Post.objects.filter(idUser2=receiver.id).order_by('-date')

        return {'user': user, 'seguidos': seguidos, 'numSeguidos': (len(seguidos)), 'teSiguen': teSiguen,
            'numTeSiguen': (len(teSiguen)), 'posts': posts, 'numPosts': (len(posts)), 'user': receiver}


class Follower(models.Model):
    idUser1 = models.ForeignKey(BasicUser, null=False, related_name='follower')
    idUser2 = models.ForeignKey(BasicUser, null=False, related_name='followed')
    def __str__(self):
        return str(self.id)

    @classmethod
    def get_profile(self, idUser):
        seguidos = Follower.objects.filter(idUser1=idUser)
        teSiguen = Follower.objects.filter(idUser2=idUser)
        posts = Post.objects.filter(idUser2=idUser).order_by('-date')
        user = BasicUser.objects.get(id=str(idUser))
        return {'user': user, 'seguidos': seguidos, 'numSeguidos': (len(seguidos)), 'teSiguen': teSiguen,
            'numTeSiguen': (len(teSiguen)), 'posts': posts, 'numPosts': (len(posts))}

    @classmethod
    def get_friends(self, idUser):
        sigues = Follower.objects.filter(idUser1=idUser)
        friends = []

        for s in sigues:
            friends.append(BasicUser.objects.get(id=str(s.idUser2)))

        return {'user': idUser, 'friends': friends}

    @classmethod
    def delete_followers(self, follower, followed):
        r = Follower.objects.filter(idUser1=follower, idUser2=followed)
        r.delete()

    @classmethod
    def add_followers(self, follower, followed):
        f1 = BasicUser.objects.get(id=str(follower))
        f2 = BasicUser.objects.get(id=str(followed))
        if f1 != f2 and not Follower.objects.filter(idUser1=f1, idUser2=f2).exists():
            ad = Follower(idUser1=f1, idUser2=f2)
            ad.save()
        #else:
            #Mensaje de error

    @classmethod
    def add_post_function(self, post, idReceiver, u):

        receiver = BasicUser.objects.get(id=str(idReceiver))
        user = BasicUser.objects.get(id=u.id)

        if Follower.objects.filter(idUser1=u, idUser2=receiver).exists() or idReceiver == u.id:
            ad = Post(idUser1=user, idUser2=receiver, comment=post)
            ad.save()
        else:
            print("Tienes que seguir a este usuario para poder escribirle un comentario.")

        seguidos = Follower.objects.filter(idUser1=receiver.id)
        teSiguen = Follower.objects.filter(idUser2=receiver.id)
        posts = Post.objects.filter(idUser2=receiver.id).order_by('-date')

        return {'user': receiver,'seguidos': seguidos,'posts':posts,
            'numSeguidos': (len(seguidos)), 'teSiguen': teSiguen, 'numTeSiguen': (len(teSiguen)),'numPosts': (len(posts))}

class Upload(models.Model):
    pic = models.ImageField("Image", upload_to="images/")
    upload_date=models.DateTimeField(auto_now_add =True)

# FileUpload form class.
class UploadForm(ModelForm):
    class Meta:
        model = Upload
        fields = '__all__'