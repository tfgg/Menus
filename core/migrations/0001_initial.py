# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'MealType'
        db.create_table('core_mealtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('time', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal('core', ['MealType'])

        # Adding model 'Meal'
        db.create_table('core_meal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.MealType'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('notes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('core', ['Meal'])

        # Adding model 'MealItem'
        db.create_table('core_mealitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('meal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Meal'])),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('vegetarian', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
        ))
        db.send_create_signal('core', ['MealItem'])


    def backwards(self, orm):
        
        # Deleting model 'MealType'
        db.delete_table('core_mealtype')

        # Deleting model 'Meal'
        db.delete_table('core_meal')

        # Deleting model 'MealItem'
        db.delete_table('core_mealitem')


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
