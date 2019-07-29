
import sys,os
sys.path.append('E:/Django projects/Recommender/')
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

import csv
from django.contrib.auth.models import User

with open('E:/Django projects/Recommender/website/user_data.csv') as f:
  reader = csv.reader(f, delimiter=',')
  for row in reader:
         created = User.objects.create_user(row[0],"a@gmail.com",row[1])
         created.save()
print 'done'
