import sys,os
sys.path.append('E:/Django projects/BTP/Recommender/')
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

import csv
from website.models import Musical

with open('E:/Django projects/BTP/Recommender/Recommender/new_classify/new_musical.csv') as f:
  reader = csv.reader(f, delimiter=',')
  i=0
  for row in reader:
         i+=1
         if i%2!=0:
             created = Musical.objects.get_or_create(mu_name=str(row[1]),mu_number=row[0])
print 'done'
