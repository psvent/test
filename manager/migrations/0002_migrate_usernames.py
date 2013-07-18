# -*- coding: utf-8 -*-
from south.v2 import DataMigration

from emailusernames.utils import migrate_usernames

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.

        # This will migrate usernames to emails
        # so that users can login with their email.
        migrate_usernames()

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        
    }

    complete_apps = ['manager']
    symmetrical = True
