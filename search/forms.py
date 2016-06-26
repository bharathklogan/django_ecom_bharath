from django import forms
from search.models import Products

class StoreForm(forms.Form):

    PRICE_CHIOCES = (
        ("<300","<Less"),
        ("300-600","300-600"),
        (">600",">600")
    )
    price_range = forms.ChoiceField(choices=PRICE_CHIOCES)
	
	
class BrandForm(forms.Form):

    PRICE_CHIOCES = (
        ("<300","<300"),
        ("300-600","300-600"),
        (">600",">600")
    )
    price_range = forms.ChoiceField(choices=PRICE_CHIOCES)
	
	
class TitleForm(forms.ModelForm):

    
    def __init__(self,*args,**kwargs):
        super(TitleForm,self).__init__(*args,**kwargs)
        self.fields['in_stock'] = forms.ChoiceField(choices=Products.INSTOCK_CHOICES,widget=forms.RadioSelect)
        self.fields['store'].required = False

    class Meta:
	    
        model = Products
        exclude=('title','price')