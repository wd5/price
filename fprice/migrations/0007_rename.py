# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_table('fprice_country', 'address_country')
        db.rename_table('fprice_city', 'address_city')
        db.rename_table('fprice_street', 'address_street')
        db.rename_table('fprice_address', 'address_address')

        db.rename_table('fprice_center', 'shop_center')
        db.rename_table('fprice_shop', 'shop_shop')

        db.rename_table('fprice_gsection', 'price_section')
        db.rename_table('fprice_goods', 'price_goods')
        db.rename_table('fprice_trade', 'price_trade')
        db.rename_column('price_goods', 'gsection_id', 'section_id')


    def backwards(self, orm):
        db.rename_table('address_country', 'fprice_country')
        db.rename_table('address_city', 'fprice_city')
        db.rename_table('address_street', 'fprice_street')
        db.rename_table('address_address', 'fprice_address')

        db.rename_table('shop_center', 'fprice_cebter')
        db.rename_table('shop_shop', 'fprice_shop')

        db.rename_table('price_section', 'fprice_gsection')
        db.rename_table('price_goods', 'fprice_goods')
        db.rename_table('price_trade', 'fprice_trade')
        db.rename_column('fprice_goods', 'section_id', 'gsection_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'fprice.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fprice.City']"}),
            'house': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'housing': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'office': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fprice.Street']"}),
            'x': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'fprice.center': {
            'Meta': {'ordering': "['title']", 'object_name': 'Center'},
            'addr': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fprice.Address']"}),
            'descr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'fprice.city': {
            'Meta': {'ordering': "['title']", 'object_name': 'City'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fprice.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'fprice.country': {
            'Meta': {'ordering': "['title']", 'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'fprice.goods': {
            'Meta': {'ordering': "['title']", 'object_name': 'Goods'},
            'descr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ed': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'gsection': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fprice.GSection']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'fprice.gsection': {
            'Meta': {'ordering': "['title']", 'object_name': 'GSection'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'fprice.shop': {
            'Meta': {'ordering': "['title']", 'object_name': 'Shop'},
            'addr': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fprice.Address']", 'null': 'True', 'blank': 'True'}),
            'center': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fprice.Center']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        'fprice.street': {
            'Meta': {'ordering': "['title']", 'object_name': 'Street'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'fprice.trade': {
            'Meta': {'object_name': 'Trade'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'goods': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fprice.Goods']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fprice.Shop']"}),
            'spytrade': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'time_add': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user'", 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['fprice']
