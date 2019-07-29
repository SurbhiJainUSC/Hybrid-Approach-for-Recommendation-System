import sys,os
sys.path.append('C:/Users/uchiha/Desktop/13-09-2015/BTP/Recommender/')
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

import csv
from website.models import Ratings

with open('C:/Users/uchiha/Desktop/13-09-2015/BTP/Recommender/Recommender/new_classify/ratings.csv') as f:
  reader = csv.reader(f, delimiter=',')
  i=0
  for row in reader:
         i+=1
         
         created = Ratings.objects.get_or_create(userid=row[0],movieid=row[1],rating=row[2])
print 'done'
