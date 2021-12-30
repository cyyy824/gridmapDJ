from django.db import models
import django.forms
from django.forms import ModelForm
from .models import GridNode, GridArea, GridSupport, GridMember

class GridSupportForm(ModelForm):
    class Meta:
        model = GridSupport
        fields = ['police','hospital','firestation','subdistrict','facilitie']

        labels = {
            'police':'派出所',
            'hospital':'医院',
            'firestation':'消防队',
            'subdistrict':'街道',
            'facilitie':'设备数'
        }

class GridMemberForm(ModelForm):
    class Meta:
        model = GridMember
        fields = "__all__"

        labels = {
            'name':'姓名',
            'mobile':'手机号'
        }

        widgets = {
            'gridnode': django.forms.HiddenInput(),
        }