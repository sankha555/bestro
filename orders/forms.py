from django import forms

class OfferForm(forms.Form):
    offer_text = forms.CharField(widget=forms.Textarea, max_length=2000, required=True)