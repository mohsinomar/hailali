from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

cat_choice = (
		('Ammonitrate', 'Ammonitrate'),
		('Sulfat_potasse', 'Sulfat_potasse'),
		('MAP', 'MAP'),
                    ('Nitrat_potasse', 'Nitrat_potasse'),
		('Calcium', 'Calcium'),
		('Complet', 'Complet'),
                    ('Acide', 'Acide'),
                    ('Sequestrine', 'Sequestrine'),
                    ('Uree_46', 'Uree_46'),
                    ('Kimia', 'Kimia'),
	)


class Engrais(models.Model):
          date=models.DateTimeField(auto_now=True,blank=True)
          categorie = models.CharField(max_length=50, blank=True, null=True,choices=cat_choice)        
          entree=models.CharField(max_length=100, blank=True)
          cumul_entree=models.CharField(max_length=100, blank=True)
          sortie=models.CharField(max_length=100, blank=True)
          cumul_sortie=models.CharField(max_length=100, blank=True)
          stock=models.CharField(max_length=100, blank=True)
          

          class Meta:
                    abstract = True

          def __str__(self):
                    return self.categorie
          
class Engrais_berhil(Engrais):
          pass

class Engrais_drisse(Engrais):
          pass

class Engrais_Aoulouz(Engrais):
          pass

class Engrais_Mariem(Engrais):
          pass

class Engrais_Rgaigue(Engrais):
               
          pass
class Engrais_Maryem2(Engrais):
               
          pass
class Engrais_zbirate(Engrais):
               
          pass
class Engrais_raisin(Engrais):
          pass

class Engrais_bananier1(Engrais):
          pass

class Engrais_bananier2(Engrais):
          pass

class Engrais_lglidi(Engrais):
          pass


class Engrais_benmbark(Engrais):
          pass


#**********************************************************************
catag_choice = (
    ('Karaté', 'Karaté'),
  	('Blouz', 'Blouz'),
  	('AG3', 'AG3'),
    ('Agrale', 'Agrale'),
  	('Coperniko', 'Coperniko'),
  	('Confidor', 'Confidor'),
    ('Valmec', 'Valmec'),
    ('Joker', 'Joker'),
    ('Pixel', 'Pixel'),
    ('Coperide', 'Coperide'),
    ('Mospelan', 'Mospelan'),
    ('Rodo', 'Rodo'),
    ('Fozika', 'Fozika'),
    ('Movinto', 'Movinto'),
    ('enfidor-speed', 'enfidor-speed'),
    ('Magnome', 'Magnome'),
    ('Samba', 'Samba'),
    ('Fozika_ca', 'Fozika_ca'),
    ('Soufre', 'Soufre'),

)
choix = (
    ('od berhil', 'od berhil'),
  	('od driss', 'od driss'),
  	('aoulouz', 'aoulouz'),
    ('meryem 1', 'meryem 1'),
  	('meryem 2', 'meryem 2'),
  	('plombier', 'plombier'),
    ('zbirate ', 'zbirate '),
    ('raisinier ', 'raisinier '),
    ('lglidi ', 'lglidi '),
    ('benmbrek/jkini/mhijib', 'benmbrek/jkini/mhijib'),
    ('bananier 1', 'bananier 1'),
    ('bananier 2', 'bananier 2'),
    

)
class Pesticide(models.Model):          
          date=models.DateTimeField(auto_now=True,blank=True)
          category = models.CharField(max_length=50, blank=True, null=True,choices=catag_choice) 
          groupe=models.CharField(max_length=100, blank=True)                 
          entree=models.CharField(max_length=100, blank=True)
          cumul_entree=models.CharField(max_length=100, blank=True)
          sortie=models.CharField(max_length=100, blank=True)
          destination=models.CharField(max_length=100, blank=True,choices=choix)
          cumul_sortie=models.CharField(max_length=100, blank=True)
          stock=models.CharField(max_length=100, blank=True)
          

          class Meta:
                    abstract = True

          def __str__(self):
                    return self.category
          
class Pesticide_berhil(Pesticide):
          pass
class Pesticide_drisse(Pesticide):
          pass
class Pesticide_Aoulouz(Pesticide):
          pass
class Pesticide_Mariem(Pesticide):
          pass
class Pesticide_Rgaigue(Pesticide):
          pass
class Pesticide_Maryem2(Pesticide):               
          pass
class Pesticide_zbirate(Pesticide):               
          pass
class Pesticide_raisin(Pesticide):
          pass
class Pesticide_bananier1(Pesticide):
          pass
class Pesticide_bananier2(Pesticide):
          pass
class Pesticide_lglidi(Pesticide):
          pass
class Pesticide_benmbark(Pesticide):
          pass
#************************************************************************************
class Semaine(models.Model):
          user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
          np=models.CharField(max_length=100, blank=True)
          sdb=models.CharField(max_length=100, blank=True)
          j1=models.FloatField(max_length=100, blank=True)
          j2=models.FloatField(max_length=100, blank=True)
          j3=models.FloatField(max_length=100, blank=True)
          j4=models.FloatField(max_length=100, blank=True)
          j5=models.FloatField(max_length=100, blank=True)
          j6=models.FloatField(max_length=100, blank=True)
          j7=models.FloatField(max_length=100, blank=True)
          nb_j=models.FloatField(max_length=100, blank=True)
          base=models.CharField(max_length=100, blank=True)
          ancienneté=models.FloatField(max_length=100, blank=True)
          pf=models.FloatField(max_length=100, blank=True)
          sb=models.CharField(max_length=100, blank=True)
          cnss=models.FloatField(max_length=100, blank=True)
          amo=models.FloatField(max_length=100, blank=True)
          net_p=models.CharField(max_length=100, blank=True)  
          class Meta:
                    abstract = True
          def __str__(self):
                    return self.np        
class Ouled_berhil(Semaine):
          pass
class Ouled_drisse(Semaine):
          pass
class Aoulouz(Semaine):
          pass
class Mariem(Semaine):
          pass
class Rgaigue(Semaine):
          pass
class Maryem2(Semaine):
          pass
class zbirate(Semaine):
          pass
class raisin(Semaine):
          pass
class bananier1(Semaine):
          pass
class bananier2(Semaine):
          pass
class lglidi(Semaine):
          pass
class benmbark(Semaine):
          pass
#**************************************************************************************
class Caisse(models.Model):
          user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
          libelle=models.CharField(max_length=100,blank=True)
          recette=models.CharField(max_length=100,blank=True)
          cumul_recette=models.CharField(max_length=100,blank=True)
          depense=models.CharField(max_length=100,blank=True)
          cumul_depense=models.CharField(max_length=100,blank=True)
          solde=models.CharField(max_length=100,blank=True)                  
          class Meta:
                    abstract = True
          def __str__(self):
                    return self.libelle        
class caisse_berhil(Caisse):
          pass
class caisse_drisse(Caisse):
          pass
class caisse_Aoulouz(Caisse):
          pass
class caisse_Mariem(Caisse):
          pass
class caisse_Rgaigue(Caisse):
          pass
class caisse_Maryem2(Caisse):              
          pass
class caisse_zbirate(Caisse):              
          pass
class caisse_raisin(Caisse):
          pass
class caisse_bananier1(Caisse):
          pass
class caisse_bananier2(Caisse):
          pass
class caisse_lglidi(Caisse):
          pass
class caisse_benmbark(Caisse):
          pass
###############################################################
###############################################################
class Achat(models.Model):                   
          desg=models.CharField(max_length=100, blank=False)
          Qté=models.CharField(max_length=100, blank=True)
          pu=models.CharField(max_length=100, blank=True)
          pt=models.CharField(max_length=100, blank=False)
          class Meta:
                    abstract = True

          def __str__(self):
                    return self.desg
          
class Achat_berhil(Achat):
          pass

class Achat_drisse(Achat):
          pass

class Achat_Aoulouz(Achat):
          pass

class Achat_Mariem(Achat):
          pass

class Achat_rgaigue(Achat):
          pass

class Achat_Maryem2(Achat):
               
          pass
class Achat_zbirate(Achat):
               
          pass
class Achat_raisin(Achat):
          pass

class Achat_bananier1(Achat):
          pass

class Achat_bananier2(Achat):
          pass

class Achat_lglidi(Achat):
          pass

class Achat_benmbark(Achat):
          pass
##########################################################
##########################################################





catagoray_choice = (
		('Ouled_berhil', 'Ouled_berhil'),
		('Ouled_drisse', 'Ouled_drisse'),
		('Aoulouz', 'Aoulouz'),
        ('Mariem', 'Mariem'),
		('Maryem2', 'Maryem2'),
        ('Plombier', 'Plombier'),
        ('Zbirate', 'Zbirate'),
        ('Glidi', 'Glidi'),
        ('Ben_mbarek', 'Ben_mbarek'),
        ('Raisin', 'Raisin'),
        ('Bananier1', 'Bananier1'),
        ('Bananier2', 'Bananier2'),

	)
class Article(models.Model):         
          user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
          date=models.CharField(max_length=100, blank=True)
          titre=models.CharField(max_length=50, blank=True, null=True,choices=catagoray_choice)
          description=models.TextField()
          created_at = models.DateTimeField(auto_now_add=True)
          update_at = models.DateTimeField(auto_now=True)
          times = models.DateTimeField(auto_now_add=True, auto_now=False)
          

          def __str__(self):
               return self.titre
          def get_absolute_url(self):
                  return reverse("my_articles")

