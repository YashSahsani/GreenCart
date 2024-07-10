from django.db import models

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
]

class Payment(models.Model):
    Name = models.CharField(max_length=255, default="John")
    Description = models.CharField(max_length=255)
    address = models.CharField(max_length=264, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=264, choices=COUNTRY_CHOICES, blank=True, default='CAN')
    city = models.CharField(max_length=264, choices=CITY_CHOICES, blank=True, default='TOR')
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    Email = models.EmailField()
    stripe_payment_intent_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.Email} - {self.Amount}"
