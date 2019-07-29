from math import sqrt
import csv,operator,timeit
class nearest:
    
    def __init__(self):
        self.k = 50
        self.data = {}
        self.cntuser=0
        self.n = 50

    def loadMovieLens(self,path=''):
          
          i = 0
          f = open(path,'r')
          for line in f:
                 i += 1
                 fields = line.split(',')
                 user = int(fields[0])
                 movie = fields[1]
                 rating =float(fields[2])
                 if user in self.data:
                    currentRatings = self.data[user]
                 else:
                    currentRatings = {}
                    self.cntuser=self.cntuser+1
                 currentRatings[movie] = rating
                 self.data[user] = currentRatings
          f.close()
          #print self.data


    def pearson(self, rating1, rating2):
        sum_xy = 0
        sum_x = 0
        sum_y = 0
        sum_x2 = 0
        sum_y2 = 0
        n = 0
        for key in rating1:
            if key in rating2:
                n += 1
                x = rating1[key]
                y = rating2[key]
                sum_xy += x * y
                sum_x += x
                sum_y += y
                sum_x2 += pow(x, 2)
                sum_y2 += pow(y, 2)
        if n == 0:
            return 0
        denominator = (sqrt(sum_x2 - pow(sum_x, 2) / n)* sqrt(sum_y2 - pow(sum_y, 2) / n))
        if denominator == 0:
            return 0
        else:
            return (sum_xy - (sum_x * sum_y) / n) / denominator
            
    
    

    def computeNearestNeighbor(self,username):
           distances = []
           d=[]
           for instance in self.data:
                if instance != username:
                    distance = self.pearson(self.data[username],self.data[instance])
                    distances.append((instance, distance))
           distances.sort(key=lambda artistTuple: artistTuple[1],reverse=True)
           return distances[0:self.k]
           

    def recommendcf(self, user):
        
        recommendation = {}
        nearest = self.computeNearestNeighbor(user)
        #print nearest
        userRating=self.data[user]
        total=0.0
        for i in range(0,self.k):
            #print 'Nearest user:',nearest[i][0]
            total+=nearest[i][1]
        for i in range(0,self.k):
            weight=nearest[i][1]/total
            neighborRating=self.data[nearest[i][0]]
            for movie in neighborRating:
                if movie not in userRating:
                    if movie not in recommendation:
                        recommendation[movie]=(neighborRating[movie]*weight)
                    else:
                        recommendation[movie]+=neighborRating[movie]*weight
        recommendation=sorted(recommendation.items(),key=operator.itemgetter(1),reverse=True)
        #print 'Recommendations:'
        cnt=0
        rec=[]
        for i in range(0,len(recommendation)):
            if cnt>=self.n:
                break
            rec.append(recommendation[i][0])
            cnt+=1
        return rec
        
        
        

        
#r=nearest()
#r.loadMovieLens('C:/Users/Hp/Desktop/Comparison/user.csv')
#r.loadMovieLens('C:/Users/Hp/Desktop/Comparison/ratings.csv')
#r.recommend(7)
#user CF recommends movies not rated by that user


