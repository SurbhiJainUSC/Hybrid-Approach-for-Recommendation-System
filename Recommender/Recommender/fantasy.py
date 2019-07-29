import sys,os
sys.path.append('E:/Django projects/BTP/Recommender/')
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

import csv
from website.models import Fantasy

with open('E:/Django projects/BTP/Recommender/Recommender/new_classify/new_fantasy.csv') as f:
  reader = csv.reader(f, delimiter=',')
  i=0
  for row in reader:
         i+=1
         if i%2!=0:
             created = Fantasy.objects.get_or_create(fa_name=str(row[1]),fa_number=row[0])
print 'done'
