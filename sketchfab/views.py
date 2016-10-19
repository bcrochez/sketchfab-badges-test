from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Model3D, SketchfabUser, Badge

from datetime import datetime, timedelta
# Create your views here.


def index(request):
    models = Model3D.objects.all()
    return render(request, 'sketchfab/index.html', {
        'models': models
    })


def model_view(request, model_id):
    model = get_object_or_404(Model3D, pk=model_id)
    model.views += 1
    model.save()
    if model.views >= 1000:
        """ Star badge
        """
        model.user.badge_set.add(Badge.objects.get(id=1))
        model.user.save()
    return render(request, 'sketchfab/model.html', {
        'model': model
    })


def user_view(request, user_id):
    user = get_object_or_404(SketchfabUser, pk=user_id)
    if user.user.model3d_set.count() >= 5:
        """ Collector badge
        """
        user.user.badge_set.add(Badge.objects.get(id=2))
        user.user.save()
    if datetime.now() - user.date_signin.replace(tzinfo=None) > timedelta(days=365):
        """ Pioneer badge
        """
        user.user.badge_set.add(Badge.objects.get(id=3))
        user.user.save()
    return render(request, 'sketchfab/user.html', {
        'user': user
    })


@login_required(login_url='sketchfab:login')
def upload(request):
    if request.POST:
        model_name = request.POST['name']
        model = Model3D(user=request.user, name=model_name)
        model.save()
        return redirect('/sketchfab/user/'+str(request.user.id))
    return render(request, 'sketchfab/upload.html')
