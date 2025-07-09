from django import forms
from. import models

class ClientesForm(forms.ModelForm):
    class Meta:
        model = models.Clientes
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '14', 'placeholder': '000.000.000-00  (Somente Números)', }),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'cidade': forms.Select(attrs={'class': 'form-control'}),
            'bairro': forms.Select(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '00000-000 (Somente Números)'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(00)00000-0000 (Somente Números)'}),
            'qtd_equipamentos': forms.TextInput(attrs={'class': 'form-control'}),
            'detalhe_equipamento': forms.Textarea(attrs={'class': 'form-control'}),
            'nivel': forms.Select(attrs={'class': 'form-control'}),
            'qtd_chamados': forms.HiddenInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),


        }
        