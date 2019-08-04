from django import forms
from .models import Project, Comments, Profile



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('poster', 'comment_content',)


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'pic']



class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description','link','projimage',)
        # exclude = ['profile', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }


