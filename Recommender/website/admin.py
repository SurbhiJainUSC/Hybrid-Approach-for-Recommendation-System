from django.contrib import admin
from .models import Name,Action,Adventure,Animation,Children,Comedy,Crime,Documentary,Drama,Fantasy,Filmnoir
from .models import Horror,Musical,Mystery,Romance,Scifi,Thriller,War,Western,Carts,Ratings,Rating
# Register your models here.

class RatingsAdmin(admin.ModelAdmin):
	list_display=["userid","movieid","rating","mname"]
	class Meta:
		model=Ratings
admin.site.register(Ratings,RatingsAdmin)
class RatingAdmin(admin.ModelAdmin):
	list_display=["userid","movieid","rating","mname"]
	class Meta:
		model=Rating
admin.site.register(Rating,RatingAdmin)

class CartsAdmin(admin.ModelAdmin):
	list_display=["userid","number","mname"]
	class Meta:
		model=Carts
admin.site.register(Carts,CartsAdmin)

class NameAdmin(admin.ModelAdmin):
	list_display=["m_name","number"]
	class Meta:
		model=Name
admin.site.register(Name,NameAdmin)

class ActionAdmin(admin.ModelAdmin):
	list_display=["ac_name","ac_number"]
	class Meta:
		model=Action
admin.site.register(Action,ActionAdmin)

class AdventureAdmin(admin.ModelAdmin):
	list_display=["ad_name","ad_number"]
	class Meta:
		model=Adventure
admin.site.register(Adventure,AdventureAdmin)

class AnimationAdmin(admin.ModelAdmin):
	list_display=["an_name","an_number"]
	class Meta:
		model=Animation
admin.site.register(Animation,AnimationAdmin)

class ChildrenAdmin(admin.ModelAdmin):
	list_display=["ch_name","ch_number"]
	class Meta:
		model=Children
admin.site.register(Children,ChildrenAdmin)

class ComedyAdmin(admin.ModelAdmin):
	list_display=["co_name","co_number"]
	class Meta:
		model=Comedy
admin.site.register(Comedy,ComedyAdmin)

class CrimeAdmin(admin.ModelAdmin):
	list_display=["cr_name","cr_number"]
	class Meta:
		model=Crime
admin.site.register(Crime,CrimeAdmin)

class DocumentaryAdmin(admin.ModelAdmin):
	list_display=["do_name","do_number"]
	class Meta:
		model=Documentary
admin.site.register(Documentary,DocumentaryAdmin)

class DramaAdmin(admin.ModelAdmin):
	list_display=["dr_name","dr_number"]
	class Meta:
		model=Drama
admin.site.register(Drama,DramaAdmin)

class FantasyAdmin(admin.ModelAdmin):
	list_display=["fa_name","fa_number"]
	class Meta:
		model=Fantasy
admin.site.register(Fantasy,FantasyAdmin)

class FilmnoirAdmin(admin.ModelAdmin):
	list_display=["fi_name","fi_number"]
	class Meta:
		model=Filmnoir
admin.site.register(Filmnoir,FilmnoirAdmin)

class HorrorAdmin(admin.ModelAdmin):
	list_display=["ho_name","ho_number"]
	class Meta:
		model=Horror
admin.site.register(Horror,HorrorAdmin)

class MusicalAdmin(admin.ModelAdmin):
	list_display=["mu_name","mu_number"]
	class Meta:
		model=Musical
admin.site.register(Musical,MusicalAdmin)

class MysteryAdmin(admin.ModelAdmin):
	list_display=["my_name","my_number"]
	class Meta:
		model=Mystery
admin.site.register(Mystery,MysteryAdmin)

class RomanceAdmin(admin.ModelAdmin):
	list_display=["ro_name","ro_number"]
	class Meta:
		model=Romance
admin.site.register(Romance,RomanceAdmin)

class ScifiAdmin(admin.ModelAdmin):
	list_display=["sc_name","sc_number"]
	class Meta:
		model=Scifi
admin.site.register(Scifi,ScifiAdmin)

class ThrillerAdmin(admin.ModelAdmin):
	list_display=["th_name","th_number"]
	class Meta:
		model=Thriller
admin.site.register(Thriller,ThrillerAdmin)

class WarAdmin(admin.ModelAdmin):
	list_display=["wa_name","wa_number"]
	class Meta:
		model=War
admin.site.register(War,WarAdmin)

class WesternAdmin(admin.ModelAdmin):
	list_display=["we_name","we_number"]
	class Meta:
		model=Western
admin.site.register(Western,WesternAdmin)

