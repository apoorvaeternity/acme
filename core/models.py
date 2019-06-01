import random
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    active = models.BooleanField(default=True, null=True)

    def save(self, *args, **kwargs):
        if self.active not in [True, False]:
            self.active = random.choice([True, False])
        if self.pk is None:
            old = Product.objects.filter(sku__iexact=self.sku)
            if old.exists():
                new = old.first()
                new.name = self.name
                new.sku = self.sku
                new.description = self.description
                new.active = self.active
                new.save()
            else:
                super(Product, self).save(*args, **kwargs)
        else:
            super(Product, self).save(*args, **kwargs)
