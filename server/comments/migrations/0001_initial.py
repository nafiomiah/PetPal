# Generated by Django 4.2.7 on 2023-12-14 02:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_text', models.CharField(max_length=1000)),
                ('comment_creation_time', models.DateTimeField(auto_now_add=True)),
                ('object_id', models.PositiveIntegerField()),
                ('rating', models.PositiveIntegerField(blank=True, null=True)),
                ('is_application', models.BooleanField(default=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('is_reply', models.BooleanField(default=False)),
                ('comment_made_by_the_id_pet_seeker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.petseeker')),
                ('comment_made_by_the_id_pet_shelter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.petshelter')),
                ('comment_made_by_the_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('parent_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='comments.comment')),
            ],
        ),
    ]
