from django import forms


class SearchForm(forms.Form):
    shelf_name = forms.CharField(
        max_length=128,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Bookshelf Name", 
                "class": "form-control"
            }
        )
    )
