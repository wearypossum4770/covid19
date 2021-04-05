from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from appointments.models import LocationState
# from classroom.models import Student, Subject, User

class PatientSignUpForm(UserCreationForm):
    
    interests = forms.ModelMultipleChoiceField(
        queryset=LocationState.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.interests.add(*self.cleaned_data.get('interests'))
        return user