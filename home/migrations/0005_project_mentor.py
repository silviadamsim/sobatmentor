# Generated by Django 4.2.13 on 2024-06-24 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_skills_mentor_video_profile_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='project_mentor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=255)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='foto_project/')),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.mentor')),
            ],
        ),
    ]