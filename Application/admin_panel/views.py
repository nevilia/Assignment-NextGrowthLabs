from django.shortcuts import render, redirect, get_object_or_404
from .models import AndroidApp
from .forms import AndroidAppForm

from app.models import AndroidApp  # Import the AndroidApp model from the main app


def admin_panel(request):
    if request.method == 'POST':
        # Handle form submission for adding a new Android app
        form = AndroidAppForm(request.POST)
        if form.is_valid():
            # Associate the Android app with the current user
            android_app = form.save(commit=False)
            android_app.user = request.user
            android_app.save()
            return redirect('admin_panel')
    else:
        form = AndroidAppForm()

    # List Android apps associated with the current user
    apps = AndroidApp.objects.filter(user=request.user)

    return render(request, 'admin_panel.html', {'apps': apps, 'form': form})

def edit_app(request, app_id):
    # Edit an existing Android app
    app = get_object_or_404(AndroidApp, pk=app_id)

    if request.method == 'POST':
        form = AndroidAppForm(request.POST, instance=app)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')

    else:
        form = AndroidAppForm(instance=app)

    return render(request, 'edit_app.html', {'form': form})

def delete_app(request, app_id):
    # Delete an Android app
    app = get_object_or_404(AndroidApp, pk=app_id)
    app.delete()
    return redirect('admin_panel')
