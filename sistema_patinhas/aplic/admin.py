from django.contrib import admin
from aplic.models import Gato
from aplic.models import Cachorro
from aplic.models import Tutor
from aplic.models import Raca
from aplic.models import Tipo
from aplic.models import Evento


admin.site.register(Cachorro)
admin.site.register(Gato)
admin.site.register(Tutor)
admin.site.register(Raca)
admin.site.register(Tipo)

admin.site.register(Evento)




# Register your models here.
