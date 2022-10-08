from django import forms
from .models import Blog, Category


class BlogForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.RadioSelect()
    )

    class Meta:
        model = Blog
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"style": "margin: 13px 6px;"})


    def clean(self, *args, **kwargs):
        except_list = ["Salam", "asd", "test"]
        title = self.cleaned_data.get("title")
        if title in except_list:
            raise forms.ValidationError(f"{title} is not valid title")

    def save(self):
        title = self.cleaned_data.get("title")
        print(title, "test title in save")
        super(BlogForm, self).save()