from django import forms
from. import models

class TecnicosForm(forms.ModelForm):
    class Meta:
        model = models.Tecnicos
        fields = '__all__'
        labels ={
            'rg': 'RG',
            'cpf': 'CPF',
            'cep': 'CEP',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'rg': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '10', 'placeholder': '00.000.000-00 (Somente Números)', }),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '14', 'placeholder': '000.000.000-00 (Somente Números)', }),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'cidade': forms.Select(attrs={'class': 'form-control'}),
            'bairro': forms.Select(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '00000-000 (Somente Números)'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(00)00000-0000 (Somente Números)'}),
            'formacao': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'nivel': forms.Select(attrs={'class': 'form-control'}),
            'n3': forms.HiddenInput(),
            'n2': forms.HiddenInput(),
            'n1': forms.HiddenInput(),
            'observacao': forms.Textarea(attrs={'class': 'form-control'}),

        }
