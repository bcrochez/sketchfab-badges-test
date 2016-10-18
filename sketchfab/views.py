from django.shortcuts import render, get_object_or_404

from .models import Model3D, SketchfabUser

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
    return render(request, 'sketchfab/model.html', {
        'model': model
    })


def user_view(request, user_id):
    user = get_object_or_404(SketchfabUser, pk=user_id)
    return render(request, 'sketchfab/user.html', {
        'user': user
    })
