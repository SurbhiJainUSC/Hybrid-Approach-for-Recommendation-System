import sys,os
sys.path.append('E:/Django projects/BTP/Recommender/')
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

import csv
from website.models import Comedy

with open('E:/Django projects/BTP/Recommender/Recommender/new_classify/new_comedy.csv') as f:
  reader = csv.reader(f, delimiter=',')
  i=0
  for row in reader:
         i+=1
         if i%2!=0:
             created = Comedy.objects.get_or_create(co_name=str(row[1]),co_number=row[0])
print 'done'
