# Generated by Django 4.2.13 on 2024-06-24 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_kelas_kategori_kelas'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='bio',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
