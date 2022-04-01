from django import forms

CONCEPTOS = (
    ('Agua', 'Agua'),
    ('Luz', 'Luz'),
    ('Gas', 'Gas'),
    ('Compra', 'Compra'),
    ('Ocio', 'Ocio'),
    ('Otros', 'Otros')
)

TIPOS = (
    ('Individual', 'Individual'),
    ('Común', 'Común')
)

class TransactionForm(forms.Form):
    cantidad    = forms.DecimalField(max_digits=6, decimal_places=2, required=True)
    fecha       = forms.DateField(required=True)
    concepto    = forms.ChoiceField(choices=CONCEPTOS, required=True)
    tipo        = forms.ChoiceField(choices=TIPOS, required=True)
    notas = forms.CharField(max_length=50, widget=forms.Textarea(), required=False)
