from django.db import models
import uuid
# Define choices for country and city
COUNTRY_CHOICES = [
    ('USA', 'United States'),
    ('CAN', 'Canada'),
    ('UK', 'United Kingdom'),
    ('AUS', 'Australia'),
    ('GER', 'Germany'),
    ('FRA', 'France'),
    ('ITA', 'Italy'),
    ('ESP', 'Spain'),
    ('JPN', 'Japan'),
    ('CHN', 'China'),
    ('IND', 'India'),
    ('BRA', 'Brazil'),
    ('RUS', 'Russia'),
    ('MEX', 'Mexico'),
    ('RSA', 'South Africa'),
    ('NIG', 'Nigeria'),
    ('EGY', 'Egypt'),
    ('ARG', 'Argentina'),
    ('CHL', 'Chile'),
    ('COL', 'Colombia'),
    ('SWE', 'Sweden'),
    ('NOR', 'Norway'),
    ('DEN', 'Denmark'),
    ('FIN', 'Finland'),
    ('POL', 'Poland'),
    ('TUR', 'Turkey'),
    ('KOR', 'South Korea'),
    ('SGP', 'Singapore'),
    ('MYS', 'Malaysia'),
    ('THA', 'Thailand'),
    ('VNM', 'Vietnam'),
    ('PHL', 'Philippines'),
    ('IDN', 'Indonesia'),
    ('NZL', 'New Zealand'),
    ('SAU', 'Saudi Arabia'),
    ('ISR', 'Israel'),
    ('UAE', 'United Arab Emirates'),
    ('IRN', 'Iran'),
    ('PAK', 'Pakistan'),
    ('BGD', 'Bangladesh'),
    ('UKR', 'Ukraine'),
    ('BEL', 'Belgium'),
    ('NLD', 'Netherlands'),
    ('CHE', 'Switzerland'),
    ('AUT', 'Austria'),
    ('GRC', 'Greece'),
    ('HUN', 'Hungary'),
    ('CZE', 'Czech Republic'),
    ('PRT', 'Portugal'),
    ('ROU', 'Romania'),
]

CITY_CHOICES = [
    ('NYC', 'New York City'),
    ('LAX', 'Los Angeles'),
    ('CHI', 'Chicago'),
    ('HOU', 'Houston'),
    ('PHX', 'Phoenix'),
    ('TOR', 'Toronto'),
    ('VAN', 'Vancouver'),
    ('MTL', 'Montreal'),
    ('LDN', 'London'),
    ('MAN', 'Manchester'),
    ('SYD', 'Sydney'),
    ('MEL', 'Melbourne'),
    ('BER', 'Berlin'),
    ('MUC', 'Munich'),
    ('PAR', 'Paris'),
    ('LYO', 'Lyon'),
    ('ROM', 'Rome'),
    ('MIL', 'Milan'),
    ('MAD', 'Madrid'),
    ('BCN', 'Barcelona'),
    ('TOK', 'Tokyo'),
    ('OSA', 'Osaka'),
    ('BJS', 'Beijing'),
    ('SHA', 'Shanghai'),
    ('DEL', 'Delhi'),
    ('MUM', 'Mumbai'),
    ('RIO', 'Rio de Janeiro'),
    ('SAO', 'Sao Paulo'),
    ('MOW', 'Moscow'),
    ('SPB', 'Saint Petersburg'),
    ('MEX', 'Mexico City'),
    ('GDL', 'Guadalajara'),
    ('JHB', 'Johannesburg'),
    ('CPT', 'Cape Town'),
    ('LOS', 'Lagos'),
    ('CAI', 'Cairo'),
    ('BUE', 'Buenos Aires'),
    ('SCL', 'Santiago'),
    ('BOG', 'Bogota'),
    ('STO', 'Stockholm'),
    ('OSL', 'Oslo'),
    ('CPH', 'Copenhagen'),
    ('HEL', 'Helsinki'),
    ('WAW', 'Warsaw'),
    ('IST', 'Istanbul'),
    ('SEL', 'Seoul'),
    ('SIN', 'Singapore'),
    ('KUL', 'Kuala Lumpur'),
    ('BKK', 'Bangkok'),
    ('HAN', 'Hanoi'),  # Added Vietnamese cities
    ('HCM', 'Ho Chi Minh City'),  # Added Vietnamese cities
    ('WIN', 'Windsor')
]


class Payment(models.Model):
    Name = models.CharField(max_length=255, default="Jack Ryan")
    address = models.CharField(max_length=264, blank=True, default="300 Ouellette Avenue")
    zipcode = models.CharField(max_length=10, blank=True, default="N9A 7B4")
    country = models.CharField(max_length=264, choices=COUNTRY_CHOICES, blank=True, default='CAN')
    city = models.CharField(max_length=264, choices=CITY_CHOICES, blank=True, default='WIN')
    # Amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    Email = models.EmailField(default="test@greencart.ca")
    stripe_payment_intent_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.Email}"


class Order(models.Model):
    order_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_items = models.IntegerField()
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='orders', null=True, blank=True)

    def __str__(self):
        return f'Order {self.order_id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.CharField(max_length=100)  # Or use a ForeignKey to a Product model if you have one
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def total_price(self):
        return self.quantity * self.price

    def __str__(self):
        return f'{self.product} ({self.quantity})'
