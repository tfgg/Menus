from django.core.management import setup_environ 
import settings 
setup_environ(settings)

import datetime
import sys
import lxml.html as html
import re
import quopri

from core.models import MealType, Meal, MealItem 

brunch_type = MealType.objects.get(name='Brunch')
breakfast_type = MealType.objects.get(name='Breakfast')
lunch_type = MealType.objects.get(name='Lunch')
dinner_type = MealType.objects.get(name='Dinner')

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def refine_coltext(col):
  items = []
  day = None
  notes = []
  for p in col.xpath('./p | ./h1'):
    text = re.sub('\s+', ' ', p.text_content()).strip()
    
    if text != "":
      if p.tag == 'h1' or any([weekday in p.text_content() for weekday in weekdays]):
        day = text
      elif 'sign up' in text.lower() or 'chapter day' in text.lower() or 'dinner' in text.lower() or '6.30pm' in text.lower():
        notes.append(text)
      else:
        items.append(text)

  return (day, notes, items)

def parse_html(data, start_date, dry_run=False):
  tree = html.document_fromstring(data)

  table = tree.xpath('//table')

  rows = table[0].xpath('//tr')

  week = None
  days = []

  for i, row in enumerate(rows):
    num_cols = len(row.xpath('./td'))

    cols = row.xpath('./td')

    brunch_day = False

    if num_cols == 4:
      day_name, notes, vegetarian = refine_coltext(cols[0])
      _, _, breakfast = refine_coltext(cols[1])
      _, _, lunch = refine_coltext(cols[2])
      _, _, dinner = refine_coltext(cols[3])
    elif num_cols == 3:
      brunch_day = True
      day_name, notes, vegetarian = refine_coltext(cols[0])
      _, _, brunch = refine_coltext(cols[1])
      _, _, dinner = refine_coltext(cols[2])    

    day = weekdays[i-1]

    date = start_date + datetime.timedelta(i-1)

    if i == 0:
      week = day_name
      continue

    Meal.objects.filter(date=date).delete()
    
    if brunch_day:
      print day, day_name
      print "Brunch"
      print " ", "\n  ".join(brunch)
      print "Dinner"
      print " ", "\n  ".join(dinner)
      print "  Vegetarian:", vegetarian
      
      if not dry_run:
        brunch_obj = Meal.objects.create(type=brunch_type,
                                         date=date,
                                         notes="")

        dinner_obj = Meal.objects.create(type=dinner_type,
                                         date=date,
                                         notes=" ".join(notes))

        for i, item in enumerate(dinner):
          MealItem.objects.create(meal=dinner_obj,
                                  name=item,
                                  order=i,
                                  vegetarian=False)

        for item in vegetarian:
          i += 1
          MealItem.objects.create(meal=dinner_obj,
                                  name=item,
                                  order=i,
                                  vegetarian=True)
    
    else:
      print day, day_name
      print "Breakfast"
      print " ", "\n  ".join(breakfast)
      print "Lunch"
      print " ", "\n  ".join(lunch)
      print "Dinner"
      print " ", "\n  ".join(dinner)
      print "  Vegetarian:", vegetarian

      if not dry_run:
        breakfast_obj = Meal.objects.create(type=breakfast_type,
                                            date=date,
                                            notes="")
        
        lunch_obj = Meal.objects.create(type=lunch_type,
                                        date=date,
                                        notes="")

        dinner_obj = Meal.objects.create(type=dinner_type,
                                         date=date,
                                         notes=" ".join(notes))

        for i, item in enumerate(breakfast):
          MealItem.objects.create(meal=breakfast_obj,
                                  name=item,
                                  order=i,
                                  vegetarian=False)
        for i, item in enumerate(lunch):
          MealItem.objects.create(meal=lunch_obj,
                                  name=item,
                                  order=i,
                                  vegetarian=False)
        
        for i, item in enumerate(dinner):
          MealItem.objects.create(meal=dinner_obj,
                                  name=item,
                                  order=i,
                                  vegetarian=False)

        for item in vegetarian:
          i += 1
          MealItem.objects.create(meal=dinner_obj,
                                  name=item,
                                  order=i,
                                  vegetarian=True)

  #print week
  #print days
if __name__ == "__main__":
  data = open(sys.argv[1]).read()
  data = quopri.decodestring(data)

  start_date = datetime.date(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
  parse_html(data, start_date, False)
