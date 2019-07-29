from django.db import models

# Create your models here.
class Ratings(models.Model):
	userid=models.CharField(max_length=100,blank=False)
	movieid=models.CharField(max_length=100,blank=False)
	rating=models.CharField(max_length=100,blank=False)
	mname=models.CharField(max_length=100,blank=False)

class Rating(models.Model):
	userid=models.CharField(max_length=100,blank=False)
	movieid=models.CharField(max_length=100,blank=False)
	rating=models.CharField(max_length=100,blank=False)
	mname=models.CharField(max_length=100,blank=False)


class Carts(models.Model):
	userid=models.CharField(max_length=100,blank=False)
	number=models.CharField(max_length=100,blank=False)
	mname=models.CharField(max_length=100,blank=False)

class Name(models.Model):
	m_name=models.CharField(max_length=100,blank=False)
	number=models.CharField(max_length=100,blank=False)

class Action(models.Model):
	ac_name=models.CharField(max_length=100,blank=False)
	ac_number=models.CharField(max_length=100,blank=False)

class Adventure(models.Model):
	ad_name=models.CharField(max_length=100,blank=False)
	ad_number=models.CharField(max_length=100,blank=False)

class Animation(models.Model):
	an_name=models.CharField(max_length=100,blank=False)
	an_number=models.CharField(max_length=100,blank=False)

class Children(models.Model):
	ch_name=models.CharField(max_length=100,blank=False)
	ch_number=models.CharField(max_length=100,blank=False)

class Comedy(models.Model):
	co_name=models.CharField(max_length=100,blank=False)
	co_number=models.CharField(max_length=100,blank=False)

class Crime(models.Model):
	cr_name=models.CharField(max_length=100,blank=False)
	cr_number=models.CharField(max_length=100,blank=False)

class Documentary(models.Model):
	do_name=models.CharField(max_length=100,blank=False)
	do_number=models.CharField(max_length=100,blank=False)

class Drama(models.Model):
	dr_name=models.CharField(max_length=100,blank=False)
	dr_number=models.CharField(max_length=100,blank=False)

class Fantasy(models.Model):
	fa_name=models.CharField(max_length=100,blank=False)
	fa_number=models.CharField(max_length=100,blank=False)

class Filmnoir(models.Model):
	fi_name=models.CharField(max_length=100,blank=False)
	fi_number=models.CharField(max_length=100,blank=False)

class Horror(models.Model):
	ho_name=models.CharField(max_length=100,blank=False)
	ho_number=models.CharField(max_length=100,blank=False)

class Musical(models.Model):
	mu_name=models.CharField(max_length=100,blank=False)
	mu_number=models.CharField(max_length=100,blank=False)

class Mystery(models.Model):
	my_name=models.CharField(max_length=100,blank=False)
	my_number=models.CharField(max_length=100,blank=False)

class Romance(models.Model):
	ro_name=models.CharField(max_length=100,blank=False)
	ro_number=models.CharField(max_length=100,blank=False)

class Scifi(models.Model):
	sc_name=models.CharField(max_length=100,blank=False)
	sc_number=models.CharField(max_length=100,blank=False)

class Thriller(models.Model):
	th_name=models.CharField(max_length=100,blank=False)
	th_number=models.CharField(max_length=100,blank=False)

class War(models.Model):
	wa_name=models.CharField(max_length=100,blank=False)
	wa_number=models.CharField(max_length=100,blank=False)

class Western(models.Model):
	we_name=models.CharField(max_length=100,blank=False)
	we_number=models.CharField(max_length=100,blank=False)

	