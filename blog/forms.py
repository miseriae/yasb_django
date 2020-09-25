from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'tag', 'body', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control' }),
            'tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'tag', 'body', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control' }),
            'tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', )

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
