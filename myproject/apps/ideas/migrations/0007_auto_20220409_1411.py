# Generated by Django 3.2.12 on 2022-04-09 14:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_auto_20220323_1706'),
        ('ideas', '0006_auto_20220324_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='like',
            name='owner_content_type',
        ),
        migrations.RemoveConstraint(
            model_name='idea',
            name='unique_titles_for_each_author',
        ),
        migrations.RemoveConstraint(
            model_name='idea',
            name='title_has_no_leading_and_trailing_whitespaces',
        ),
        migrations.RemoveField(
            model_name='idea',
            name='id',
        ),
        migrations.RemoveField(
            model_name='idea',
            name='meta_author',
        ),
        migrations.RemoveField(
            model_name='idea',
            name='meta_copyright',
        ),
        migrations.RemoveField(
            model_name='idea',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='idea',
            name='meta_keywords',
        ),
        migrations.AddField(
            model_name='idea',
            name='rating',
            field=models.PositiveIntegerField(blank=True, choices=[(1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')], null=True, verbose_name='Rating'),
        ),
        migrations.AddField(
            model_name='idea',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.RemoveField(
            model_name='idea',
            name='categories',
        ),
        migrations.AddField(
            model_name='idea',
            name='categories',
            field=models.ManyToManyField(related_name='category_ideas', to='categories.Category', verbose_name='Categories'),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]