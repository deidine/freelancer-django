from django import forms
from .models import PostProject,  PostJobs
 

class PostProjectForm(forms.ModelForm):
    class Meta:
        model = PostProject
        fields = '__all__'
        exclude = ['user', 'viewers_project', 'updated_project', 'created_project', 'likes', 'cacher']
   
    def __init__(self, *args, **kwargs):
        super(PostProjectForm, self).__init__(*args, **kwargs)
        self.fields['nom_projet'].widget.attrs['placeholder'] = 'titre du projet'
        self.fields['epic_coder'].widget.attrs['placeholder'] = 'Categorie: programming, Designer...'
        self.fields['location'].widget.attrs['placeholder'] = 'payes'
        self.fields['prix_premiere'].widget.attrs['placeholder'] = 'prix minimaum'
        self.fields['prix_derniere'].widget.attrs['placeholder'] = 'prix maximale'
        self.fields['description_projet'].widget.attrs['placeholder'] = 'Description'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].required = True


class PostJobForm(forms.ModelForm):
    class Meta:
        model = PostJobs
        fields = '__all__'
        exclude = ['user',  'viewers_job', 'updated_job', 'created_job', 'likes', 'cacher']
 
    def __init__(self, *args, **kwargs):
        super(PostJobForm, self).__init__(*args, **kwargs)
        self.fields['name_jobs'].widget.attrs['placeholder'] = 'titre Traveil'
        self.fields['epic_coder'].widget.attrs['placeholder'] = 'Categorie : programming, Designer...'
        self.fields['location'].widget.attrs['placeholder'] = 'Payes'
        self.fields['prix'].widget.attrs['placeholder'] = 'prix'
        self.fields['description_job'].widget.attrs['placeholder'] = 'Description'

        self.fields['prix'].widget.attrs['prix'] = 'javascript: return event.keyCode === 8 ||event.keyCode === 46 ? true : !isNaN(Number(event.key))'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].required = True
 