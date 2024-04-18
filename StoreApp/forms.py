from django import forms


from StoreApp.models import Cliente


# Criando um formulario baseado num model
class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'  # server para pegar todos os campos do model, caso eu queira somente alguns eu apenas passo os nomes das variaveis 

        widgets ={
            'cpf' : forms.TextInput(attrs={'class':'cpf'}),
            'cep' : forms.TextInput(attrs= {'class': 'cep'}),
            'data_nascimento' : forms.TextInput(attrs={'class':'date'})
        }


class ContatoForm(forms.Form):
    nome = forms.CharField()
    email = forms.EmailField()
    telefone = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'cel_phone_with_ddd'}))

    assunto = forms.CharField()
    mensagem = forms.CharField(widget=forms.Textarea)
