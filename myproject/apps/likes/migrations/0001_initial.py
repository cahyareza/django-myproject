# Generated by Django 3.2.12 on 2022-05-19 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Creation Date and Time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modification Date and Time')),
                ('object_id', models.CharField(default='', help_text='Please enter the ID of the related object.', max_length=255, verbose_name='Related object')),
                ('content_type', models.ForeignKey(help_text='Please select the type (model) for the relation, you want to build.', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype', verbose_name="Related object's type (model)")),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Likes',
                'verbose_name_plural': 'Likes',
                'ordering': ('-created',),
            },
        ),
    ]
