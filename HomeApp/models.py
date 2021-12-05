from django.db import models

# Create your models here.


class Experience (models.Model):  # MODEL OF EXPERIENCE SECTION
    title = models.CharField(verbose_name='Title',
                             blank=False, null=False, max_length=100)

    company = models.CharField(verbose_name='Company',
                               blank=False, null=False, max_length=100)

    description = models.TextField(
        verbose_name='Description', blank=False, null=False)

    dateStart = models.DateField(
        verbose_name='Start Date', blank=True, null=True)

    dateEnd = models.DateField(
        verbose_name='End Date', blank=True, null=True)

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'

    def __str__(self):
        return self.title


class Education (models.Model):  # MODEL OF EDUCATION SECTION
    title = models.CharField(verbose_name='Title',
                             blank=False, null=False, max_length=100)

    school = models.CharField(verbose_name='School',
                              blank=False, null=False, max_length=100)

    description = models.TextField(
        verbose_name='Description', blank=False, null=False)

    dateStart = models.DateField(
        verbose_name='Start Date', blank=False, null=False)

    dateEnd = models.DateField(
        verbose_name='End Date', blank=False, null=False)

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'

    def __str__(self):
        return self.title


class Award (models.Model):  # MODEL OF AWARDS SECTION
    title = models.CharField(verbose_name='Title',
                             blank=False, null=False, max_length=100)

    description = models.TextField(
        verbose_name='Description', blank=False, null=False)

    class Meta:
        verbose_name = 'Award'
        verbose_name_plural = 'Awards'

    def __str__(self):
        return self.title
