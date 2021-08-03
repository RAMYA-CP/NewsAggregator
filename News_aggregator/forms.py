from django import forms
from .models import Articles
class Post_article(forms.ModelForm):
	class Meta:
		model=Articles
		fields=('title','img','link')