from django.db import models


class Candidate(models.Model):
    full_name = models.CharField(max_length=120, verbose_name='Полное имя')
    position = models.CharField(max_length=120, verbose_name='Должность')
    short_info = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Кандидат'
        verbose_name_plural = 'Кандидаты'


class Contact(models.Model):
    type = models.CharField(max_length=50, verbose_name='Способ связи')
    connect = models.CharField(max_length=50, verbose_name='Связь')
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='candidate_contact')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Experience(models.Model):
    from_date = models.DateField(max_length=50, verbose_name='Начало работы')
    to_date = models.DateField(max_length=50, verbose_name='Окончание', null=True, blank=True)
    company = models.CharField(max_length=120, verbose_name='Организация')
    position = models.CharField(max_length=120, verbose_name='Должность')
    duties = models.TextField()
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='candidate_exp')

    def __str__(self):
        return f'{self.company} {self.position}'

    class Meta:
        verbose_name = 'Опыт'
        verbose_name_plural = 'Опыт'
        ordering = ['-from_date']


class Education(models.Model):
    year_finish = models.IntegerField(verbose_name='Год окончания')
    title = models.CharField(max_length=120, verbose_name='Учебное заведение')
    specialty = models.CharField(max_length=120, verbose_name='Специальность')
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='candidate_edu')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Образование'
        ordering = ['-year_finish']


class Certificate(models.Model):
    year_finish = models.IntegerField(verbose_name='Год окончания')
    title = models.CharField(max_length=120, verbose_name='Наименование курса')
    url = models.URLField(max_length=120, verbose_name='Ссылка', blank=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='candidate_cert')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'
        ordering = ['-year_finish']


class HardSkill(models.Model):
    title = models.CharField(max_length=120, verbose_name='Навык')
    level = models.IntegerField(verbose_name='Уровень')
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='candidate_hs')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Профессиональные навыки'
        ordering = ['-level']


class SoftSkill(models.Model):
    title = models.TextField(max_length=120, verbose_name='Навык')
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='candidate_ss')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Личные качества и умения'
