from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField()
    email = forms.CharField()
    telefone = forms.EmailField()
    assunto = forms.CharField()
    mensagem = forms.CharField(widget=forms.Textarea)
