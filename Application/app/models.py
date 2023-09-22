from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AndroidApp(models.Model):
    name = models.CharField(max_length=100)
    points = models.IntegerField(default=100)
    icon = models.ImageField(upload_to='icon/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='android_apps', default=1)

    
    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points_earned = models.PositiveIntegerField(default=0)
    # app = models.ForeignKey(AndroidApp, on_delete=models.CASCADE, default=6) #this points to 6->Google which will be installed by default and gives 0 points
    app = models.ManyToManyField(AndroidApp)
    
    # Not entirely correct logic
    def get_points_earned(self, app):
        self.app.add(app)
        self.points_earned += app.points
        self.save()
    
    def __str__(self):
        return self.user.username
    
class Task(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    app = models.ForeignKey(AndroidApp, on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to='task_screenshots/')  # Assuming screenshots are uploaded to a "task_screenshots" directory


    def __str__(self):
        return f"Task for {self.app.name} by {self.user.user.username}"