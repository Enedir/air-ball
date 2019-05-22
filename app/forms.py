# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )

from app import models


# class FormUser(forms.Form):
#     name = forms.CharField(label='Nome', widget=forms.TextInput(attrs={'class' : 'form-control collectes-ville text-center'}))
#     email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class' : 'form-control collectes-ville text-center'}))
#     birth_date = forms.DateField(label='Data de nascimento', widget=forms.DateInput(attrs={'class' : 'form-control collectes-ville text-center'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control collectes-ville text-center'}), label='Senha' )

# class FormLogin(forms.Form):
#      email = forms.EmailField(label='E-mail', widget=forms.EmailInput())
#      password = forms.CharField(label='Senha', widget=forms.PasswordInput())

#      def clean(self):
#             cleaned_data = super(FormLogin, self).clean()
#             aemail = cleaned_data.get("email")
#             apassword = cleaned_data.get("password")

#             if len(aemail) == 0:
#                 raise forms.ValidationError("O email deve ser informado")
            
#             if len(apassword) == 0:
#                 raise forms.ValidationError("A senha deve ser informada")

User = get_user_model()

class FormLogin(forms.Form):
    username = forms.CharField(label='☭ Nome usuario')
    password = forms.CharField(label='☭ Palavra-chave', widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
       
        # user_qs = User.objects.filter(username=username)
        # if user_qs.count() == 1:
        #     user = user_qs.first()
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect passsword")
            if not user.is_active:
                raise forms.ValidationError("This user is not longer active.")
        return super(FormLogin, self).clean(*args, **kwargs)


class FormUser(forms.ModelForm):
    email = forms.EmailField(label='Email ')
    email2 = forms.EmailField(label='Confirmar Email')
    password = forms.CharField(label='Palavra-chave', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]

    # def clean(self, *args, **kwargs):
    #     email = self.cleaned_data.get('email')
    #     email2 = self.cleaned_data.get('email2')
    #     if email != email2:
    #         raise forms.ValidationError("Emails must match")
    #     email_qs = User.objects.filter(email=email)
    #     if email_qs.exists():
    #         raise forms.ValidationError("This email has already been registered")

    #     return super(UserRegisterForm,self).clean(*args, **kwargs)

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered")
        return email
         

class FormPlayer(forms.ModelForm):
    name = forms.CharField(label='Nome', widget=forms.TextInput(attrs={'class' : 'form-control collectes-ville text-center'}))
    description = forms.CharField(label='Descrição', widget=forms.Textarea(attrs={'class' : 'form-control collectes-ville text-center'}))
    
    def clean(self):
        cleaned_data = super(FormPlayer, self).clean()
        aname = cleaned_data.get("name")
        adescription = cleaned_data.get("description")

        if len(aname) == 0:
            raise forms.ValidationError("O nome deve ser informado")
            
        if len(adescription) == 0:
            raise forms.ValidationError("A descrição deve ser informada")

    class Meta:
        model = models.Player
        fields = ['name','description']

class FormTeam(forms.ModelForm):
    name = forms.CharField(label='Nome', widget=forms.TextInput(attrs={'class' : 'form-control collectes-ville text-center'}))
    description = forms.CharField(label='Descrição', widget=forms.Textarea(attrs={'class' : 'form-control collectes-ville text-center'}))
    general_manager = forms.CharField(label='GM', widget=forms.TextInput(attrs={'class' : 'form-control collectes-ville text-center'}))
    coach = forms.CharField(label='Técnico', widget=forms.TextInput(attrs={'class' : 'form-control collectes-ville text-center'}))
    arena = forms.CharField(label='Arena', widget=forms.TextInput(attrs={'class' : 'form-control collectes-ville text-center'}))

    def clean(self):
        cleaned_data = super(FormTeam, self).clean()
        aname = cleaned_data.get("name")
        adescription = cleaned_data.get("description")
        ageneral_manager = cleaned_data.get("general_manager")
        acoach = cleaned_data.get("coach")
        aarena = cleaned_data.get("arena")

        if len(aname) == 0:
            raise forms.ValidationError("O nome deve ser informado")
            
        if len(adescription) == 0:
            raise forms.ValidationError("A descrição deve ser informada")

        if len(ageneral_manager) == 0:
            raise forms.ValidationError("O gerente geral deve ser informado")

        if len(acoach) == 0:
            raise forms.ValidationError("O técnico deve ser informado")

        if len(aarena) == 0:
            raise forms.ValidationError("A arena deve ser informada")

    class Meta:
        model = models.Team
        fields = ['name','description','general_manager','coach','arena']

class FormQuestion(forms.ModelForm):
    CHOICES = ((1, 'Resposta 1'),(2, 'Resposta 2'),(3, 'Resposta 3'),(4, 'Resposta 4'),(5, 'Resposta 5'),)
    
    question = forms.CharField(label='Pergunta', widget=forms.Textarea(attrs={'class' : 'form-control collectes-ville text-center'}))
    answer_1 = forms.CharField(label='Resposta 1', widget=forms.TextInput(attrs={'class' : 'form-control collectes-ville text-center'}))
    answer_2 = forms.CharField(label='Resposta 2', widget=forms.TextInput(attrs={'class' : 'form-control collectes-ville text-center'}))
    answer_3 = forms.CharField(label='Resposta 3', widget=forms.TextInput(attrs={'class' : 'form-control collectes-ville text-center'}))
    answer_4 = forms.CharField(label='Resposta 4', widget=forms.TextInput(attrs={'class' : 'form-control collectes-ville text-center'}))
    answer_5 = forms.CharField(label='Resposta 5', widget=forms.TextInput(attrs={'class' : 'form-control collectes-ville text-center'}))
    correct_answer = forms.ChoiceField(choices=CHOICES, label='Resposta correta', widget=forms.Select(attrs={'class' : 'form-control collectes-ville text-center'}))

    def clean(self):
        cleaned_data = super(FormQuestion, self).clean()
        aquestion = cleaned_data.get("question")
        aanswer_1 = cleaned_data.get("answer_1")
        aanswer_2 = cleaned_data.get("answer_2")
        aanswer_3 = cleaned_data.get("answer_3")
        aanswer_4 = cleaned_data.get("answer_4")
        aanswer_5 = cleaned_data.get("answer_5")
        acorrect_answer = cleaned_data.get("correct_answer")
        
        if len(aquestion) == 0:
            raise forms.ValidationError("A pergunta deve ser informada")
        
        if len(aanswer_1) == 0:
            raise forms.ValidationError("A resposta 1 deve ser informada")

        if len(aanswer_2) == 0:
            raise forms.ValidationError("A resposta 2 deve ser informada")
            
        if len(aanswer_3) == 0:
            raise forms.ValidationError("A resposta 3 deve ser informada")
            
        if len(aanswer_4) == 0:
            raise forms.ValidationError("A resposta 4 deve ser informada")
            
        if len(aanswer_5) == 0:
            raise forms.ValidationError("A resposta 5 deve ser informada")
            
        if len(acorrect_answer) == 0:
            raise forms.ValidationError("A resposta correta deve ser informada")

    class Meta:
        model = models.Question
        fields = ['question','answer_1','answer_2','answer_3','answer_4', 'answer_5', 'correct_answer']