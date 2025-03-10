import django_tables2 as tables
from .models import Product

class ProductTable(tables.Table):
    price = tables.Column(attrs={"td": {"class": "price-column"}})
    class Meta:
        model = Product
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "id", "stock", "price")

    def render_price(self, value):
        return f'{value} zł'

