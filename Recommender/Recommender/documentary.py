import sys,os
sys.path.append('E:/Django projects/BTP/Recommender/')
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

import csv
from website.models import Documentary

with open('E:/Django projects/BTP/Recommender/Recommender/new_classify/new_documentary.csv') as f:
  reader = csv.reader(f, delimiter=',')
  i=0
  for row in reader:
         i+=1
         if i%2!=0:
             created = Documentary.objects.get_or_create(do_name=str(row[1]),do_number=row[0])
print 'done'
