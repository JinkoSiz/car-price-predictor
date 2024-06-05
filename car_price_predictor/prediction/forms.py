from django import forms


class CarForm(forms.Form):
    BRAND_CHOICES = [
        ('Audi', 'Audi'),
        ('BMW', 'BMW'),
        ('Mercedes-Benz', 'Mercedes-Benz'),
        ('Toyota', 'Toyota'),
        ('Volkswagen', 'Volkswagen')
    ]
    MODEL_CHOICES = [
        ('A3', 'A3'), ('A4', 'A4'), ('A6', 'A6'), ('Q3', 'Q3'), ('Q5', 'Q5'),
        ('3 Series', '3 Series'), ('5 Series', '5 Series'), ('X3', 'X3'), ('X5', 'X5'),
        ('C-Class', 'C-Class'), ('E-Class', 'E-Class'), ('GLE', 'GLE'), ('GLC', 'GLC'),
        ('Corolla', 'Corolla'), ('Camry', 'Camry'), ('RAV4', 'RAV4'), ('Land Cruiser', 'Land Cruiser'),
        ('Golf', 'Golf'), ('Passat', 'Passat'), ('Tiguan', 'Tiguan'), ('Arteon', 'Arteon')
    ]
    GEARBOX_CHOICES = [
        ('AT', 'AT'),
        ('MT', 'MT'),
        ('AMT', 'AMT'),
        ('CVT', 'CVT')
    ]

    brand = forms.ChoiceField(choices=BRAND_CHOICES)
    model = forms.ChoiceField(choices=MODEL_CHOICES)
    year = forms.IntegerField(min_value=1900, max_value=2099)
    mileage = forms.FloatField(min_value=0)
    engine = forms.FloatField(min_value=0)
    gearbox = forms.ChoiceField(choices=GEARBOX_CHOICES)
