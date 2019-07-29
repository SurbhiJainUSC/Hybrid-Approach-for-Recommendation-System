from django.shortcuts import render
from .forms import LoginForm
from .models import Name,Action,Adventure,Animation,Children,Comedy,Crime,Documentary,Drama,Fantasy,Filmnoir
from .models import Horror,Musical,Mystery,Romance,Scifi,Thriller,War,Western,Carts,Ratings,Rating
from django.http import HttpResponseRedirect , HttpResponse
from django.contrib.auth import authenticate, login, logout
import json
from django.contrib.staticfiles.templatetags.staticfiles import static
import os
from django.conf import settings
#for fpgrowth
import sys
import itertools
import timeit
import operator
from .fpgrowth import FPNode,FPTree,generate_association_rules
from .user_cf import nearest
from .item_to_item import similar
# Create your views here.

def delete(request):
	mid=request.POST.get("mid")
	userid=request.session['userid']
	carts=Carts.objects.filter(userid=userid,number=mid).delete()
	return HttpResponseRedirect('/profile/')

def cart(request):
	var=request.POST.get('code1')
	names = Name.objects.filter(m_name__iexact = var )
	for name in names:
		userid=request.session['userid']
		number=name.number
		mname=name.m_name
		if not Carts.objects.filter(userid=userid,number=number):
			carts = Carts.objects.create(
	                            userid= userid,
	                            number = number,
	                            mname=mname)
			carts.save()
		return HttpResponseRedirect('/profile/')
	return HttpResponseRedirect('/movie/')


def profile(request):
	user=request.session['userid']
	items = Carts.objects.filter(userid__iexact = user )
	leng=items.count()
	
	context={
	'items':items,
	'len':leng,
	
	}

 	return render(request,'profile.html',context)
def history(request):
	user=request.session['userid']

	history=Rating.objects.filter(userid__iexact = user)
	context={
	'history':history,
	}

	return render(request,'history.html',context)

def getnamesview(request):
	if request.is_ajax():
		q = request.GET.get('term', '')
		names = Name.objects.filter(m_name__istartswith = q ).order_by("m_name")
		names1 = Name.objects.filter(m_name__icontains = q ).order_by("m_name")

		results = []
		
		for name in names:
			name_json = {}
			name_json['id'] = name.number
			name_json['label'] = name.m_name
			name_json['value'] = name.m_name
			results.append(name_json)

		for name in names1:
			if name not in names:
				name_json = {}
				name_json['id'] = name.number
				name_json['label'] = name.m_name
				name_json['value'] = name.m_name
				results.append(name_json)

		
		data = json.dumps(results[:15])
	else:
	 	data = 'fail'
	mimetype = 'application/json'
	return HttpResponse(data, mimetype)

def Login(request):
	logout(request)
	username = password = ''
	if request.method=='POST':
		form=LoginForm(request.POST)
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				request.session['userid']=username
				return HttpResponseRedirect('/movie/')
			
		else:
			title='Username or Password do not match!!'

		
	else:
		form=LoginForm()
		title=''
	context={
		"title":title,
		"form":form,
	}

	return render(request,'signin.html',context)

def Movie(request):
	namelist=Name.objects.all()
		
	context={
		"namelist":namelist,
		}
	return render(request,"movie.html",context)

def Actions(request):
	namelist=Action.objects.all()
	
	context={
	"namelist":namelist,
	}
	return render(request,"action.html",context)

def Adventures(request):
	namelist=Adventure.objects.all()
	
	context={
	"namelist":namelist,
	}
	return render(request,"adventure.html",context)

def Animations(request):
	namelist=Animation.objects.all()
	
	context={
	"namelist":namelist,
	}
	return render(request,"animation.html",context)

def Childrens(request):
	namelist=Children.objects.all()
	
	context={
	"namelist":namelist,
	}
	return render(request,"children.html",context)

def Comedys(request):
	namelist=Comedy.objects.all()
	
	context={
	"namelist":namelist,
	}
	return render(request,"comedy.html",context)

def Crimes(request):
	namelist=Crime.objects.all()
	
	context={
	"namelist":namelist,
	}
	return render(request,"crime.html",context)

def Documentarys(request):
	namelist=Documentary.objects.all()
	
	context={
	"namelist":namelist,
	}
	return render(request,"documentary.html",context)

def Dramas(request):
	namelist=Drama.objects.all()
	
	context={
	"namelist":namelist,
	}
	return render(request,"drama.html",context)

def Fantasys(request):
	namelist=Fantasy.objects.all()
	
	context={
	"namelist":namelist,
	}
	return render(request,"fantasy.html",context)

def Filmnoirs(request):
	namelist=Filmnoir.objects.all()
	
	context={
	"namelist":namelist,
	}
	return render(request,"filmnoir.html",context)

def Horrors(request):
	namelist=Horror.objects.all()
	
	context={
	"namelist":namelist,
	}
	return render(request,"horror.html",context)

def Musicals(request):
	namelist=Musical.objects.all()
	
	context={
	"namelist":namelist,
	}
	return render(request,"musical.html",context)

def Mysterys(request):
	namelist=Mystery.objects.all()
	
	context={
	"namelist":namelist,
	}
	return render(request,"mystery.html",context)

def Romances(request):
	namelist=Romance.objects.all()
	
	context={
	"namelist":namelist,
	}
	return render(request,"romance.html",context)

def Scifis(request):
	namelist=Scifi.objects.all()
	
	context={
	"namelist":namelist,
	}
	return render(request,"scifi.html",context)

def Thrillers(request):
	namelist=Thriller.objects.all()
	
	context={
	"namelist":namelist,
	}
	return render(request,"thriller.html",context)

def Wars(request):
	namelist=War.objects.all()
	
	context={
	"namelist":namelist,
	}
	return render(request,"war.html",context)

def Westerns(request):
	namelist=Western.objects.all()
	
	context={
	"namelist":namelist,
	}
	return render(request,"western.html",context)

def Logout(request):
	user=request.session['userid']
	carts=Carts.objects.filter(userid=user).delete()
	logout(request)
	return HttpResponseRedirect('/')

def recommend(request):
	sys.setrecursionlimit(1000)
	start_time = timeit.default_timer()
	userid = request.session['userid']
	items = Carts.objects.filter(userid__iexact = userid ).order_by('number')
	leng=items.count()
	if leng==0:
		context={
		'len':leng,
		}
	else:
		url=os.path.join(settings.STATIC_ROOT,"csv/transaction/"+str(userid)+".csv")
		data=open(url,'r')

		#print "file name"
		#print data
		lines = data.readlines()
		big_dataset = [None] * len(lines)
		for i, line in enumerate(lines):
			big_dataset[i] = [int(x) for x in lines[i].split()]
		support_threshold=7
		min_confidence = 0.7
		tree = FPTree(big_dataset, support_threshold, None, None)
		patterns = tree.mine_patterns(support_threshold)
		rules = generate_association_rules(patterns, min_confidence)

		
		number_of_rules = 500
		s=[]
		d={}
		low = 3
		high=7
		while len(rules) < number_of_rules:
			support_threshold = int((high+low)/2)
			tree = FPTree(big_dataset, support_threshold, None, None)
			patterns = tree.mine_patterns(support_threshold)
			rules = generate_association_rules(patterns, min_confidence)
			if(len(rules) > number_of_rules):
				break;
			else:
				high=support_threshold
		
		inp = '('
		if items.count() == 1:
			for i in items:
				inp+=str(i.number)+","
			inp += ')'
		else:
			for i in items:
				inp+=str(i.number)+", "
			inp = inp[:-2]
			inp+=')'
		
		#print "a"
		#print type(inp)
		for rule in rules.keys():
			#print rule
			if str(rule)==inp:
				#print inp," ==> ",rules[rule][0]
				f=str(rules[rule][0]).strip('(').strip(')').strip('').split(',')
				for field in f:
					if field is not '':
						s.append(int(field.strip(' ')))

		"""print s
		for i in items:
			print i.number"""
		for rule in rules.keys():
			for i in items:
				srule=str(rule)
				#print str(i.number)
				if srule.find(' '+str(i.number)+',')>=0:
					#print rule," ==> ",rules[rule][0]
					f=str(rules[rule][0]).strip('(').strip(')').strip('').split(',')
					for field in f:
						if field is not '':
							s.append(int(field.strip(' ')))
				elif srule.find(' '+str(i.number)+')')>=0:
					#print rule," ==> ",rules[rule][0]
					f=str(rules[rule][0]).strip('(').strip(')').strip('').split(',')
					for field in f:
						if field is not '':
							s.append(int(field.strip(' ')))
				elif srule.find('('+str(i.number)+',')>=0:
					#print rule," ==> ",rules[rule][0]
					f=str(rules[rule][0]).strip('(').strip(')').strip('').split(',')
					for field in f:
						if field is not '':
							s.append(int(field.strip(' ')))

		#print "b"
		#print s
		sim=[]
		for i in items:
			sim.append(int(i.number))

		#print s



		recommendation=[]
		for i in s:
			if i not in recommendation:
				if i not in sim:
					recommendation.append(i)

		print recommendation


		cnt=1
		diction={}
		for k in sim:
			url=os.path.join(settings.STATIC_ROOT,'csv/similar.csv')
			g=open(url,'r')
			#print g
			if cnt!=1:
				for i,line in enumerate(g):
					if i==k-1:
						filed=line.split(',')
						for j in range(0,1682):
							diction[j+1]+=(float(filed[j]))

			else:
				for i,line in enumerate(g):
					if i==k-1:
						filed=line.split(',')
						for j in range(0,1682):
							diction[j+1]=(float(filed[j]))
			cnt+=1
		#print "c"
		for i in sim:
			diction[i]=-1.0

		sorted_diction = sorted(diction.items(), key=operator.itemgetter(1),reverse=True) 
		for i in range(0,70):
			if sorted_diction[i][0] not in recommendation:
				if sorted_diction[i][0] not in sim:
					recommendation.append(sorted_diction[i][0])

		
		result=[]
		for r in recommendation:
			res=Name.objects.get(number__iexact=str(r))
			result.append(res)
		#result=result[:50]


		"""
		for i in result:
			print i
		"""
		result=result[:50]
		context={
		'result':result,
		'len':leng,
		}
		elapsed = timeit.default_timer() - start_time
		print elapsed
	return render(request,'recommend.html',context)

def cf(request):
	start_time = timeit.default_timer()
	n=nearest()
	url=os.path.join(settings.STATIC_ROOT,'csv/ratings.csv')
	n.loadMovieLens(url)
	userid = request.session['userid']
	items = Carts.objects.filter(userid__iexact = userid ).order_by('number')
	leng=items.count()
	if leng==0:
		context={
		'len':leng,
		}
	else:
		recommendations = n.recommendcf(int(userid))
		result=[]
		for r in recommendations:
			res=Name.objects.get(number__iexact=str(r))
			result.append(res)
		result=result[:50]
		context={
		'result':result,
		'len':leng,
		}
	elapsed = timeit.default_timer() - start_time
	print 'Time required:',elapsed
	return render(request,'cf.html',context)

def item(request):
	start_time = timeit.default_timer()
	n=similar()
	url=os.path.join(settings.STATIC_ROOT,'csv/movies.csv')
	n.loadMovieLens(url)
	userid = request.session['userid']
	items = Carts.objects.filter(userid__iexact = userid ).order_by('number')
	leng=items.count()
	if leng==0:
		context={
		'len':leng,
		}
	else:
		it=[]
		for i in items:
			it.append(int(i.number))
		recommendations = n.jaccard(it)
		#print recommendations
		result=[]
		for r in recommendations:
			res=Name.objects.get(number__iexact=str(r))
			result.append(res)
		result=result[:50]
		context={
		'result':result,
		'len':leng,
		}
	elapsed = timeit.default_timer() - start_time
	print 'Time required:',elapsed
	return render(request,'item.html',context)

def arm(request):
	sys.setrecursionlimit(1000)
	start_time = timeit.default_timer()
	userid = request.session['userid']
	items = Carts.objects.filter(userid__iexact = userid ).order_by('number')
	leng=items.count()
	if leng==0:
		context={
		'len':leng,
		}
	else:
		url=os.path.join(settings.STATIC_ROOT,'csv/newtrans.csv')
		data=open(url,'r')
		lines = data.readlines()
		big_dataset = [None] * len(lines)
		for i, line in enumerate(lines):
			big_dataset[i] = [int(x) for x in lines[i].split()]
		support_threshold = 30
		tree = FPTree(big_dataset, support_threshold, None, None)
		#print "pattern ni bane"
		patterns = tree.mine_patterns(support_threshold)
		s=[]
		d={}
		min_confidence = 0.7

		#print "rules ni bane"
		rules = generate_association_rules(patterns, min_confidence)
		
		inp = '('
		if items.count() == 1:
			for i in items:
				inp+=str(i.number)+","
			inp += ')'
		else:
			for i in items:
				inp+=str(i.number)+", "
			inp = inp[:-2]
			inp+=')'
		
		#print "a"
		#print type(inp)
		for rule in rules.keys():
			#print rule
			if str(rule)==inp:
				#print inp," ==> ",rules[rule][0]
				f=str(rules[rule][0]).strip('(').strip(')').strip('').split(',')
				for field in f:
					if field is not '':
						s.append(int(field.strip(' ')))

		"""print s
		for i in items:
			print i.number"""
		for rule in rules.keys():
			for i in items:
				srule=str(rule)
				#print str(i.number)
				if srule.find(' '+str(i.number)+',')>=0:
					#print rule," ==> ",rules[rule][0]
					f=str(rules[rule][0]).strip('(').strip(')').strip('').split(',')
					for field in f:
						if field is not '':
							s.append(int(field.strip(' ')))
				elif srule.find(' '+str(i.number)+')')>=0:
					#print rule," ==> ",rules[rule][0]
					f=str(rules[rule][0]).strip('(').strip(')').strip('').split(',')
					for field in f:
						if field is not '':
							s.append(int(field.strip(' ')))
				elif srule.find('('+str(i.number)+',')>=0:
					#print rule," ==> ",rules[rule][0]
					f=str(rules[rule][0]).strip('(').strip(')').strip('').split(',')
					for field in f:
						if field is not '':
							s.append(int(field.strip(' ')))

		#print s
		sim=[]
		for i in items:
			sim.append(int(i.number))

		recommendation=[]
		for i in s:
			if i not in recommendation:
				if i not in sim:
					recommendation.append(i)

		#print recommendation


		
		result=[]
		for r in recommendation:
			res=Name.objects.get(number__iexact=str(r))
			result.append(res)
		result=result[0:50]
		l=len(result)
		context={
		'result':result,
		'len':leng,
		'l':l,
		}
		elapsed = timeit.default_timer() - start_time
		print elapsed
	return render(request,'arm.html',context)





	