from django.db import models

# Create your models here.
class Home(models.Model):
    name = models.CharField('Indtroduceing',max_length= 40)
    about1 = models.TextField('Text')
    about2 = models.TextField('Text')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Homes'

class About(models.Model):
    name = models.CharField('Indtroduceing',max_length= 40)
    about1 = models.TextField('Text')
    about2 = models.TextField('Text')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

class About2(models.Model):
    name = models.CharField('Indtroduceing',max_length= 40)
    about1 = models.TextField('Text')
    about2 = models.TextField('Text')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'About2'
        verbose_name_plural = 'Abouts2'

class Slider(models.Model):
    name1 = models.CharField('Slider_Name1',max_length= 40)
    name2 = models.CharField('Slider_Name2',max_length= 40)
    about = models.TextField('Text')
    img = models.ImageField('Image', upload_to = 'media')
    bigimg = models.ImageField('BigImage', upload_to = 'media')

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'

class Client(models.Model):
    name = models.CharField('name',max_length= 40)
    about = models.TextField('Text')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        
class ClientImg(models.Model):
    img = models.ImageField('Image', upload_to = 'media')
    link = models.TextField('Link')

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = 'Clientimg'
        verbose_name_plural = 'Clientsimgs'  

class LetsTalk(models.Model):
    name = models.CharField('name',max_length= 40)
    about1 = models.TextField('Text')
    about2 = models.TextField('Text')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'LetsTalk'
        verbose_name_plural = 'LetsTalks'          