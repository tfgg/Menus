# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'MealItem.order'
        db.add_column('core_mealitem', 'order', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'MealItem.order'
        db.delete_column('core_mealitem', 'order')


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
            'vegetarian': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'})
        },
        'core.mealtype': {
            'Meta': {'object_name': 'MealType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'time': ('django.db.models.fields.TimeField', [], {})
        }
    }

    complete_apps = ['core']
