from django.contrib import admin

# Register your models here.

from .models import Data6
from .models import User6
from .models import Medicine
from .models import test


admin.site.register(Data6)
admin.site.register(User6)
admin.site.register(Medicine)
admin.site.register(test)

