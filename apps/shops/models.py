from django.db import models
from django.urls import reverse
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    Top_choices = (
        (False, 'Нет'),
        (True, 'Да'),
    )
    Status = (
        ('True', 'True'),
        ('False', 'False'),
    )

    bool_choices = (
        (True, 'Yes'),
        (False, 'No'),
    )
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Родительская категория')
    title = models.CharField(max_length=50, unique=True, verbose_name='Название')
    slug = models.SlugField()
    top = models.BooleanField(verbose_name='Главное', null=True, blank=True, default=False, choices=Top_choices)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=Status, null=True, blank=True)
    is_active = models.BooleanField(choices=bool_choices, null=True, blank=True)
    meta_keywords = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    image = models.ImageField(blank=True, upload_to='images/', null=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        db_table = 'categories'

        unique_together = [['parent', 'slug']]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        if self.top is False:
            self.isActive = False
        elif self.top is True:
            self.isActive = True
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
# class Category(models.Model):
#     name = models.CharField(max_length=150, verbose_name='Название')
#     slug = models.SlugField(verbose_name='URL', unique=True)
#     parent = models.ForeignKey('self', blank=True, null=True, related_name='children', verbose_name='Под категория',
#                                on_delete=models.CASCADE)
#
#     def __str__(self):
#         full_path = [self.name]
#         k = self.parent
#         while k is not None:
#             full_path.append(k.name)
#             k = k.parent
#         return ' -> '.join(full_path[::-1])
#
#     class Meta:
#         unique_together = ('slug', 'parent',)
#         verbose_name = "Категория"
#         verbose_name_plural = "Категории"


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
