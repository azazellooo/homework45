from django.db import models

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class Task(models.Model):
    description = models.CharField(max_length=160, null=False, blank=False)
    text = models.TextField(max_length=1500, null=True, blank=True)
    status = models.CharField(max_length=100, choices=status_choices, default='new')
    date = models.DateField(null=True, blank=True)


    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'{self.id}. {self.description}: {self.date}'
# Create your models here.
