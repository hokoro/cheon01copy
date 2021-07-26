from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationsForm(ModelForm):
    class meta:
        model = Profile #models.py 에서 생성한 모델
        fields = ['image','nickname','message']
