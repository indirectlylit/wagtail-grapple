# Generated by Django 2.2.1 on 2019-10-30 11:59

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('home', '0012_auto_20191002_1154'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('decimal', wagtail.core.blocks.DecimalBlock()), ('date', wagtail.core.blocks.DateBlock()), ('datetime', wagtail.core.blocks.DateTimeBlock()), ('gallery', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(classname='full title')), ('images', wagtail.core.blocks.StreamBlock([('image', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(classname='full title')), ('image', wagtail.images.blocks.ImageChooserBlock())]))]))])), ('video', wagtail.core.blocks.StructBlock([('youtube_link', wagtail.embeds.blocks.EmbedBlock(required=False))]))]),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.AuthorPage'),
        ),
    ]
