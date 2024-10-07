from django.contrib import admin
from aplic.models import Gato
from aplic.models import Cachorro
from aplic.models import Tutor
from aplic.models import Raca


admin.site.register(Cachorro)
admin.site.register(Gato)
admin.site.register(Tutor)
admin.site.register(Raca)

# Register your models here.
