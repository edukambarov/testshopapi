from django.db import models
from django.core.validators import RegexValidator, MinValueValidator
from django.db.models import CASCADE


# Создайте три модели Django: клиент, товар и заказ.
#
# Клиент может иметь несколько заказов. Заказ может содержать несколько товаров. Товар может входить в несколько заказов.
#
# Поля модели «Клиент»:
# — имя клиента
# — электронная почта клиента
# — номер телефона клиента
# — адрес клиента
# — дата регистрации клиента
#
# Поля модели «Товар»:
# — название товара
# — описание товара
# — цена товара
# — количество товара
# — дата добавления товара
#
# Поля модели «Заказ»:
# — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
# — связь с моделью «Товар», указывает на товары, входящие в заказ
# — общая сумма заказа
# — дата оформления заказа
class Client(models.Model):
    client_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, validators=[RegexValidator(regex=r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$')])
    address = models.CharField(max_length=100)
    reg_date = models.DateField(default="2020-01-01")

    def __str__(self):
        return f'{self.client_name}'


class Good(models.Model):
    good_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2,
                                validators=[
                                    MinValueValidator(0.0)],)
    quantity = models.PositiveIntegerField(default=1)
    add_date = models.DateField(default="2023-01-01")
    image = models.ImageField(blank=True, height_field=100, width_field=100)

    def __str__(self):
        return f'{self.good_name} (price: {self.price}, quantity: {self.quantity})'

    def get_good_total(self):
        return self.price * self.quantity


class Order(models.Model):
    order_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order_total = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    order_items = models.ManyToManyField(Good)
    order_date = models.DateField(default="2023-01-01")

    def get_order_items(self):
        return "\n".join([str(x) for x in list(self.order_items.all())])


    def __str__(self):
        return f'Order with {self.order_total} by {self.order_client}'