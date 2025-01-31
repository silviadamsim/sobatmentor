# Generated by Django 4.2.13 on 2024-06-24 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_pengguna_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=255)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='foto_skill/')),
            ],
        ),
        migrations.AddField(
            model_name='mentor',
            name='video_profile',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pengalamankerja',
            name='deskripsi',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pengalamankerja',
            name='keahlian',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pengalamankerja',
            name='tempat',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pengalamankerja',
            name='waktu',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pengalamanmengajar',
            name='deskripsi',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pengalamanmengajar',
            name='keahlian',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pengalamanmengajar',
            name='tempat',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pengalamanmengajar',
            name='waktu',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pengalamanorganisasi',
            name='tempat',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pengalamanorganisasi',
            name='waktu',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='kelas',
            name='deskripsi',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pengalamanorganisasi',
            name='bukti',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='skill_mentor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.mentor')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.skills')),
            ],
        ),
    ]
