# Generated by Django 3.2.12 on 2022-03-23 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Creation Date and Time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modification Date and Time')),
                ('meta_keywords', models.CharField(blank=True, help_text='Separate keywords with commas.', max_length=255, verbose_name='Keywords')),
                ('meta_description', models.CharField(blank=True, max_length=255, verbose_name='Description')),
                ('meta_author', models.CharField(blank=True, max_length=255, verbose_name='Author')),
                ('meta_copyright', models.CharField(blank=True, max_length=255, verbose_name='Copyright')),
                ('title_bg', models.CharField(blank=True, db_tablespace='', max_length=200, verbose_name='Title (Bulgarian)')),
                ('title_hr', models.CharField(blank=True, db_tablespace='', max_length=200, verbose_name='Title (Croatian)')),
                ('title_cs', models.CharField(blank=True, db_tablespace='', max_length=200, verbose_name='Title (Czech)')),
                ('title_da', models.CharField(blank=True, db_tablespace='', max_length=200, verbose_name='Title (Danish)')),
                ('title_nl', models.CharField(blank=True, db_tablespace='', max_length=200, verbose_name='Title (Dutch)')),
                ('title_en', models.CharField(blank=True, db_tablespace='', max_length=200, verbose_name='Title (English)')),
                ('title_et', models.CharField(blank=True, db_tablespace='', max_length=200, verbose_name='Title (Estonian)')),
                ('title_fi', models.CharField(blank=True, db_tablespace='', max_length=200, verbose_name='Title (Finnish)')),
                ('title_fr', models.CharField(blank=True, db_tablespace='', max_length=200, verbose_name='Title (French)')),
                ('title_de', models.CharField(blank=True, db_tablespace='', max_length=200, verbose_name='Title (German)')),
                ('title_el', models.CharField(blank=True, db_tablespace='', max_length=200, verbose_name='Title (Greek)')),
                ('title_hu', models.CharField(blank=True, db_tablespace='', max_length=200, verbose_name='Title (Hungarian)')),
                ('title_ga', models.CharField(blank=True, db_tablespace='', max_length=200, verbose_name='Title (Irish)')),
                ('title_it', models.CharField(blank=True, db_tablespace='', max_length=200, verbose_name='Title (Italian)')),
                ('title_lv', models.CharField(blank=True, db_tablespace='', max_length=200, verbose_name='Title (Latvian)')),
                ('title_lt', models.CharField(blank=True, db_tablespace='', max_length=200, verbose_name='Title (Lithuanian)')),
                ('title_mt', models.CharField(blank=True, db_tablespace='', max_length=200, verbose_name='Title (Maltese)')),
                ('title_pl', models.CharField(blank=True, db_tablespace='', max_length=200, verbose_name='Title (Polish)')),
                ('title_pt', models.CharField(blank=True, db_tablespace='', max_length=200, verbose_name='Title (Portuguese)')),
                ('title_ro', models.CharField(blank=True, db_tablespace='', max_length=200, verbose_name='Title (Romanian)')),
                ('title_sk', models.CharField(blank=True, db_tablespace='', max_length=200, verbose_name='Title (Slovak)')),
                ('title_sl', models.CharField(blank=True, db_tablespace='', max_length=200, verbose_name='Title (Slovene)')),
                ('title_es', models.CharField(blank=True, db_tablespace='', max_length=200, verbose_name='Title (Spanish)')),
                ('title_sv', models.CharField(blank=True, db_tablespace='', max_length=200, verbose_name='Title (Swedish)')),
                ('content_bg', models.TextField(blank=True, db_tablespace='', verbose_name='Content (Bulgarian)')),
                ('content_hr', models.TextField(blank=True, db_tablespace='', verbose_name='Content (Croatian)')),
                ('content_cs', models.TextField(blank=True, db_tablespace='', verbose_name='Content (Czech)')),
                ('content_da', models.TextField(blank=True, db_tablespace='', verbose_name='Content (Danish)')),
                ('content_nl', models.TextField(blank=True, db_tablespace='', verbose_name='Content (Dutch)')),
                ('content_en', models.TextField(blank=True, db_tablespace='', verbose_name='Content (English)')),
                ('content_et', models.TextField(blank=True, db_tablespace='', verbose_name='Content (Estonian)')),
                ('content_fi', models.TextField(blank=True, db_tablespace='', verbose_name='Content (Finnish)')),
                ('content_fr', models.TextField(blank=True, db_tablespace='', verbose_name='Content (French)')),
                ('content_de', models.TextField(blank=True, db_tablespace='', verbose_name='Content (German)')),
                ('content_el', models.TextField(blank=True, db_tablespace='', verbose_name='Content (Greek)')),
                ('content_hu', models.TextField(blank=True, db_tablespace='', verbose_name='Content (Hungarian)')),
                ('content_ga', models.TextField(blank=True, db_tablespace='', verbose_name='Content (Irish)')),
                ('content_it', models.TextField(blank=True, db_tablespace='', verbose_name='Content (Italian)')),
                ('content_lv', models.TextField(blank=True, db_tablespace='', verbose_name='Content (Latvian)')),
                ('content_lt', models.TextField(blank=True, db_tablespace='', verbose_name='Content (Lithuanian)')),
                ('content_mt', models.TextField(blank=True, db_tablespace='', verbose_name='Content (Maltese)')),
                ('content_pl', models.TextField(blank=True, db_tablespace='', verbose_name='Content (Polish)')),
                ('content_pt', models.TextField(blank=True, db_tablespace='', verbose_name='Content (Portuguese)')),
                ('content_ro', models.TextField(blank=True, db_tablespace='', verbose_name='Content (Romanian)')),
                ('content_sk', models.TextField(blank=True, db_tablespace='', verbose_name='Content (Slovak)')),
                ('content_sl', models.TextField(blank=True, db_tablespace='', verbose_name='Content (Slovene)')),
                ('content_es', models.TextField(blank=True, db_tablespace='', verbose_name='Content (Spanish)')),
                ('content_sv', models.TextField(blank=True, db_tablespace='', verbose_name='Content (Swedish)')),
            ],
            options={
                'verbose_name': 'Idea',
                'verbose_name_plural': 'Ideas',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.CharField(default='', help_text='Please enter the ID of the related object.', max_length=255, verbose_name='Related object')),
                ('owner_object_id', models.CharField(default='', help_text='Please enter the ID of the related object.', max_length=255, verbose_name='Owner')),
                ('content_type', models.ForeignKey(help_text='Please select the type (model) for the relation, you want to build.', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype', verbose_name="Related object's type (model)")),
                ('owner_content_type', models.ForeignKey(help_text='Please select the type (model) for the relation, you want to build.', limit_choices_to={'model__in': ('user', 'group')}, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='contenttypes.contenttype', verbose_name="Owner's type (model)")),
            ],
            options={
                'verbose_name': 'Like',
                'verbose_name_plural': 'Likes',
            },
        ),
    ]
