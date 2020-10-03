# Generated by Django 3.0.8 on 2020-07-22 04:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paratususer',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='paratususer',
            name='last_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.CreateModel(
            name='ParatusPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paratus_message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('paratus_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ParatusComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('paratus_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ParatusPost')),
                ('paratus_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]