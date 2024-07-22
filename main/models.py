from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from .utils import generate_random_filename, generate_random_photo
from django.utils import timezone
import bcrypt
from django.contrib.auth import get_user_model

class CustomUser(models.Model):
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=128)
	username = models.CharField(max_length=150, unique=True)
  
	
	def set_psw(self, raw_psw):
		self.password = bcrypt.hashpw(raw_psw.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

	def check_psw(self, raw_psw):
		return bcrypt.checkpw(raw_psw.encode('utf-8'), self.password.encode('utf-8'))



class Video(models.Model):
  
	preview = models.ImageField('preview', upload_to=generate_random_photo)
	video = models.FileField('video',upload_to=generate_random_filename)
	uploader = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)  
	views = models.PositiveIntegerField(default=0) 
	title = models.CharField('title', max_length=40, validators=[MinLengthValidator(3), MaxLengthValidator(40)])
  

	def __str__(self):
		return self.title
	
	class Meta: 
		verbose_name = 'Video'
		verbose_name_plural = 'Video'


