from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(verbose_name='URL', unique=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', verbose_name='Под категория',
                               on_delete=models.CASCADE)

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Brand(models.Model):
    name = models.CharField(max_length=500, verbose_name='Название')

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"


class Product(models.Model):
    SIZE_CLASS = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('EL', 'Extra Large'),

    )
    name = models.CharField(max_length=255, verbose_name='Название')
    uuid = models.UUIDField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand', verbose_name='Бренд')
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    sale = models.IntegerField('Скидка в процентах', blank=True, default=0)
    min_description = models.TextField(max_length=500, verbose_name="Мини описание")
    description = models.TextField('Описание')
    stock = models.IntegerField(default=1, verbose_name="Количество на складе")
    size = models.CharField(max_length=2, choices=SIZE_CLASS, default='Small', verbose_name="Размер")
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    creation_up = models.DateTimeField(auto_now=True, verbose_name="Дата редоктирования")

    def get_sale(self):
        '''Расчитать стоимость со скидкой'''
        price = int(self.price * (100 - self.sale) / 100)
        return price

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
