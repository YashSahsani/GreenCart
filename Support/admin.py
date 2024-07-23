from django.contrib import admin
from .models import Query, TicketStatus, faqCategory, FAQ

admin.site.register(Query)
admin.site.register(TicketStatus)
admin.site.register(faqCategory)
admin.site.register(FAQ)