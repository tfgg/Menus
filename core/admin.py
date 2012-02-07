from django.contrib import admin

import models

class MealItemAdmin(admin.TabularInline):
  model = models.MealItem

class MealAdmin(admin.ModelAdmin):
  model = models.Meal
  inlines = [MealItemAdmin,]

admin.site.register(models.Meal, MealAdmin)
admin.site.register(models.MealType)
admin.site.register(models.MealItem)
admin.site.register(models.MealRating)

