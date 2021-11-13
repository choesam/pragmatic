from django import forms
from django.forms import ModelForm

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'editable', 'style': 'text-align: left; height: auto;'}))

    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']

    # def save(self, commit=True):
    #     instance = super(ArticleCreationForm, self).save(commit=False)
    #     instance.author = self.request.user
    #     # instance.published_date = timezone.now()
    #
    #     # 이미지파일이 있으면, 리사이즈/크롭 한다.
    #     if instance.image_file:
    #         instance.image_file = self.rescale(self.cleaned_data.get('image_file'), 600, 600, force=True)
    #     if commit:
    #         instance.save()
    #     return instance
