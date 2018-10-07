from django.db import models


class Claz(models.Model):
    name = models.CharField(max_length=32)
    year_admission = models.DecimalField(max_digits=4, decimal_places=0)
    graduated = models.BooleanField(default=False)

    day_total = models.FloatField(default=0.0)
    day_full = models.FloatField(default=0.0)
    week_total = models.FloatField(default=0.0)
    week_full = models.FloatField(default=0.0)
    semester_total = models.FloatField(default=0.0)
    semester_full = models.FloatField(default=0.0)


class Subject(models.Model):
    name = models.TextField()
    full_marks = models.IntegerField(default=10)
    in_use = models.BooleanField(default=True)


class Inspector(models.Model):
    name = models.CharField(max_length=32)
    auth_code = models.CharField(max_length=8)

    clazes = models.ManyToManyField(Claz)
    subjects = models.ManyToManyField(Subject)

    in_use = models.BooleanField(default=True)
    modify_other_dates = models.BooleanField(default=False)


class Score(models.Model):
    date = models.DateField()
    score = models.FloatField(default=0.0)
    full_score = models.FloatField(default=0.0)
    reason = models.TextField(null=True, blank=True)
    
    claz = models.ForeignKey(Claz, on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    inspector = models.ForeignKey(Inspector, on_delete=models.PROTECT)
