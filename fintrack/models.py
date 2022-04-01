from django.db import models

# Create your models here.
class Transaction(models.Model):
    cantidad = models.DecimalField(max_digits=4, decimal_places=2, blank=False)
    fecha    = models.DateField(blank=False)

    CONCEPTOS = (
        ('Agua', 'Agua'),
        ('Luz', 'Luz'),
        ('Gas', 'Gas'),
        ('Compra', 'Compra'),
        ('Ocio', 'Ocio'),
        ('Otros', 'Otros')
    )

    concepto = models.CharField(max_length=10, choices=CONCEPTOS, blank=False)

    TIPOS = (
        ('Individual', 'Individual'),
        ('Común', 'Común')
    )

    tipo = models.CharField(max_length=10, choices=TIPOS, blank=False)

    notas = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.cantidad}, {self.concepto} ({self.fecha})'
