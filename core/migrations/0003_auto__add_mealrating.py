# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'MealRating'
        db.create_table('core_mealrating', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('meal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Meal'])),
            ('rating', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ident', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('core', ['MealRating'])


    def backwards(self, orm):
        
        # Deleting model 'MealRating'
        db.delete_table('core_mealrating')


    models = {
        'core.meal': {
            'Meta': {'object_name': 'Meal'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.MealType']"})
        },
        'core.mealitem': {
            'Meta': {'object_name': 'MealItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Meal']"}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'vegetarian': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'core.mealrating': {
            'Meta': {'object_name': 'MealRating'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ident': ('django.db.models.fields.TextField', [], {}),
            'meal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Meal']"}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'core.mealtype': {
            'Meta': {'object_name': 'MealType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'time': ('django.db.models.fields.TimeField', [], {})
        }
    }

    complete_apps = ['core']
