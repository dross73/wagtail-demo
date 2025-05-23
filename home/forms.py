from django import forms

# This form will be shown to users on the website
# It matches the fields you defined in the MagazineOrderPage model


class MagazineOrderForm(forms.Form):
    name = forms.CharField(max_length=255)  # User's full name
    city = forms.CharField(max_length=100)  # City name
    state = forms.CharField(max_length=2)  # State abbreviation (e.g. "IA")
    zip_code = forms.CharField(max_length=10)  # Zip or postal code

    # 📰 Choices for subscription length and price
    TERM_CHOICES = [
        ("1yr_1999", "1 Year - $19.99"),
        ("2yr_2999", "2 Years - $29.99"),
        ("3yr_3999", "3 Years - $39.99"),
    ]

    # Radio button selection for subscription term
    subscription_term = forms.ChoiceField(
        choices=TERM_CHOICES, widget=forms.RadioSelect
    )
