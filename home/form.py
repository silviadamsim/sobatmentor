from django import forms
from .models import *

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Pengguna
        fields = ['nama', 'username', 'email', 'no_telp']

class MentorForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = [
            'pengguna', 'tempat_tanggal_lahir', 'jenis_kelamin', 'alamat', 'domisili',
            'universitas', 'program_studi', 'semester', 'nim', 'bio', 'metode_pembayaran',
            'video_profile'
        ]
        widgets = {
            'jenis_kelamin': forms.RadioSelect(choices=[('L', 'Laki-laki'), ('P', 'Perempuan')]),
            'tempat_tanggal_lahir': forms.TextInput(attrs={'placeholder': 'Tempat, Tanggal Lahir'}),
        }