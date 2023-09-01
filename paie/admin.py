from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


admin.site.register(Article)

@admin.register(Ouled_berhil,Ouled_drisse,Aoulouz,Mariem,Rgaigue,Maryem2,zbirate,raisin,bananier1,bananier2,lglidi,benmbark)
class ViewAdmin(ImportExportModelAdmin):
          pass
class OuledberhilAdmin(ImportExportModelAdmin):
          pass

@admin.register(caisse_berhil,caisse_drisse,caisse_Aoulouz,caisse_Mariem,caisse_Rgaigue,caisse_Maryem2,caisse_zbirate,caisse_raisin,caisse_bananier1,caisse_bananier2,caisse_lglidi,caisse_benmbark)
class CaisseAdmin(ImportExportModelAdmin):
          pass

@admin.register(Engrais_berhil,Engrais_drisse,Engrais_Aoulouz,Engrais_Mariem,Engrais_Rgaigue,Engrais_Maryem2,Engrais_zbirate,Engrais_raisin,Engrais_bananier1,Engrais_bananier2,Engrais_lglidi,Engrais_benmbark)
class ViewAdmin(ImportExportModelAdmin):
          pass

@admin.register(Pesticide_berhil,Pesticide_drisse,Pesticide_Aoulouz,Pesticide_Mariem,Pesticide_Rgaigue,Pesticide_Maryem2,Pesticide_zbirate,Pesticide_raisin,Pesticide_bananier1,Pesticide_bananier2,Pesticide_lglidi,Pesticide_benmbark)
class ViewAdmin(ImportExportModelAdmin):
          
          pass
@admin.register(Achat_berhil,Achat_drisse,Achat_Aoulouz, Achat_Mariem, Achat_rgaigue,Achat_Maryem2,Achat_zbirate,Achat_raisin,Achat_bananier1,Achat_bananier2,Achat_lglidi,Achat_benmbark)
class ViewAdmin(ImportExportModelAdmin):
          pass




