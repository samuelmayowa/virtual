from .models import Blog, categorybag, tagbag
from django import forms
from django.utils.translation import ugettext_lazy as _
from django_comments_xtd.forms import XtdCommentForm
from django_comments_xtd.models import TmpXtdComment


class MyCommentForm(XtdCommentForm):
    title = forms.CharField(
        max_length=256,
        widget=forms.TextInput(attrs={'placeholder': _('title')})
    )

    def get_comment_create_data(self):
        data = super(MyCommentForm, self).get_comment_create_data()
        data.update({'title': self.cleaned_data['title']})
        return data


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ("title", "category", "tag", "content", "image",)

        widget = {
            'title': forms.TextInput(),
            'category': forms.ChoiceField(choices=(categorybag)),
            'content': forms.Textarea(),
            'image': forms.ImageField(max_length=300, allow_empty_file=False),
            'tag': forms.ChoiceField(choices=(tagbag))
        }
