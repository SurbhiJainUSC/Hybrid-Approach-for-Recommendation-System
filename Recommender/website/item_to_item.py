from math import sqrt
import csv
import operator,timeit
class similar:

    def __init__(self):
        self.cntmovie=0
        self.data={}
        self.cnt=[]
        self.n = 20
        self.genre = 19
        
    def loadMovieLens(self,path=""):
          
          cnt = 0
          f = open(path, 'r')
          for line in f:
              movie=[]
              if cnt>=1682:
                  break
              cnt+=1
              fields = line.split(',')
              moviename = int(fields[0])
              self.cntmovie=self.cntmovie+1
              for i in range(1,self.genre+1):
                 movie.append(int(fields[i]))
              name=fields[20]
              self.data[moviename]=movie
          #print self.data 
          f.close()

    def jaccard(self,x):
        start_time = timeit.default_timer()
        # x is the input list
        sim={}
            
        for i in range(0,len(x)):
            for j in range(1,self.cntmovie+1):
                cnt11=0
                cnt01=0
                cnt10=0
                for k in range(0,self.genre):
                    if self.data[x[i]][k]==1 and self.data[j][k]==1:
                        cnt11+=1
                    if self.data[x[i]][k]==0 and self.data[j][k]==1:
                        cnt01+=1
                    if self.data[x[i]][k]==1 and self.data[j][k]==0:
                        cnt10+=1
                if i==0:
                    sim[j]=float(cnt11)/(float(cnt11+cnt01+cnt10))
                else:
                    sim[j]=sim[j]+float(cnt11)/(float(cnt11+cnt01+cnt10))
        #print sim
        
        #recommendations
        print 'Recommendations:'
        sim=sorted(sim.items(),key=operator.itemgetter(1),reverse=True)
        rec=[]
        cnt=0
        for i in range(0,self.cntmovie):
            if sim[i][0] not in x:
                rec.append(sim[i][0])
                cnt+=1
            if cnt==self.n:
                break
        return rec[0:50]
        
            
                

#r=similar()
#r.loadMovieLens("C:/Users/Hp/Desktop/Comparison/item.csv")
#r.loadMovieLens("C:/Users/Hp/Desktop/Comparison/movies.csv")
#r.jaccard([310])
