from django import forms
from customers.models.customer import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['address1', 'address2', 'address3', 'zip_code', 'state', 'country', ]
