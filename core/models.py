from django.db import models

# Create your models here.
class MealType(models.Model):
  name = models.TextField()
  time = models.TimeField()

  def __unicode__(self):
    return "%s (%s)" % (self.name, self.time)

class Meal(models.Model):
  type = models.ForeignKey(MealType)
  date = models.DateField()
  notes = models.TextField()

  def __unicode__(self):
    return "%s on %s" % (self.type, self.date)

  def weekday(self):
    return self.date.strftime('%A')

  def rating(self):
    ratings = self.mealrating_set.all()
    rating_sum = sum([rating.rating for rating in ratings])

    if len(ratings) == 0:
      return None
    else:
      return rating_sum / len(ratings)

class MealItem(models.Model):
  meal = models.ForeignKey(Meal)
  name = models.TextField()
  vegetarian = models.BooleanField()
  order = models.IntegerField(default=0)

  def __unicode__(self):
    return "%s for %s" % (self.name, self.meal)

class MealRating(models.Model):
  meal = models.ForeignKey(Meal)
  rating = models.IntegerField(default=0)
  ident = models.TextField()

  def __unicode__(self):
    return "%s %s - %d" % (self.meal.date, self.meal.type.name, self.rating)
