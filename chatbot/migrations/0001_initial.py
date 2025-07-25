# Generated by Django 5.2.4 on 2025-07-15 17:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatbotCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Categoría de Chatbot',
                'verbose_name_plural': 'Categorías de Chatbot',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ChatbotKnowledgeBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question', models.CharField(max_length=255, unique=True)),
                ('answer', models.TextField()),
                ('keywords', models.TextField(blank=True, help_text='Palabras clave separadas por comas para mejorar la búsqueda.')),
                ('is_active', models.BooleanField(db_index=True, default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='knowledge_entries', to='chatbot.chatbotcategory')),
            ],
            options={
                'verbose_name': 'Entrada de Conocimiento',
                'verbose_name_plural': 'Base de Conocimiento del Chatbot',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='ChatConversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('session_id', models.CharField(db_index=True, help_text='ID de sesión para agrupar interacciones de usuarios anónimos o logueados.', max_length=100)),
                ('question_text', models.TextField()),
                ('answer_text', models.TextField()),
                ('matched_knowledge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='matched_conversations', to='chatbot.chatbotknowledgebase')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chat_conversations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Conversación de Chatbot',
                'verbose_name_plural': 'Historial de Conversaciones',
                'ordering': ['-created_at'],
            },
        ),
    ]
