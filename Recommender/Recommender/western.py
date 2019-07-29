import sys,os
sys.path.append('E:/Django projects/BTP/Recommender/')
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

import csv
from website.models import Western

with open('E:/Django projects/BTP/Recommender/Recommender/new_classify/new_western.csv') as f:
  reader = csv.reader(f, delimiter=',')
  i=0
  for row in reader:
         i+=1
         if i%2!=0:
             created =Western.objects.get_or_create(we_name=str(row[1]),we_number=row[0])
print 'done'
