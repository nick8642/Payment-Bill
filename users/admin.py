from django.contrib import admin
from .models import Branch_Master
from .models import Course_Master
from .models import Account_Master
from .models import Student_Master

admin.site.register(Branch_Master)
admin.site.register(Course_Master)
admin.site.register(Account_Master)
admin.site.register(Student_Master)


