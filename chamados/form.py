from django import forms
from. import models

class ChamadosForm(forms.ModelForm):
    class Meta:
        model = models.Chamados
        fields = '__all__'
        widgets = {
            'numero_chamado': forms.HiddenInput(attrs={'class': 'form-control'}),
            'cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'bairro': forms.Select(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(00)00000-0000 (Somente Números)'}),
            'tecnicos': forms.Select(attrs={'class': 'form-control'}),
            'data_atendimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'horario_atendimento': forms.TimeInput(format='%H:%M', attrs={'class': 'form-control', 'type': 'time'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'nivel': forms.Select(attrs={'class': 'form-control'}),
            'motivo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
        }