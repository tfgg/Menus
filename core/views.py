import datetime

from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse

from models import Meal, MealType, MealItem

def home(request):
  now = datetime.date.today()
  #meals = Meal.objects.filter(date__gt=now).order_by('date', 'type__time')
  meals = Meal.objects.order_by('date', 'type__time')

  groups = []
  group = []
  current_date = None
  for meal in meals:
    if current_date is None or current_date != meal.date:
      if current_date is not None:
        groups.append((current_date.strftime("%A"), current_date, group))
        group = [] 
      current_date = meal.date

    group.append(meal)

  if group != []:
    groups.append((current_date.strftime("%A"), current_date, group))

  return render_to_response('home.html', {'groups': groups,})
