import sys,os
sys.path.append('E:/Django projects/BTP/Recommender/')
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

import csv
from website.models import Name

with open('E:/Django projects/BTP/Recommender/Recommender/movie_name.csv') as f:
  reader = csv.reader(f, delimiter=',')
  i=0
  for row in reader:
         i+=1
         if i>1622:
             created = Name.objects.get_or_create(m_name=str(row[1]),number=row[0])
print 'done'
