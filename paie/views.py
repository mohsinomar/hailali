

from paie.forms import PesticideBRForm,PesticideDRForm,PesticideAOForm,EngraisBRForm, EngraisDRForm, EngraisAOForm
from django.shortcuts import get_object_or_404, render, redirect
from.models import*
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from.forms import*
import xlwt
import datetime
from django.http import HttpResponse
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.contrib import messages


def home(request):
          title = 'Groupe Hailali' 
          my_template='home.html'
          if request =='mobile':
                        my_template='mobile_template.html'
          return render(request,my_template,{'title':title})

@login_required
def index(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          title='Liste des employés'
          
          return render(request,'index.html',{'title':title})


def index(request):
          title='Liste des employés'
          return render(request,'index.html',{'title':title})



def pesticide(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          return render(request,'pesticide.html')


def affiche(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          title='Gestion de la caisse'
          items = Caisse.objects.all()          
          return render(request,'caisse.html',{'items':items,'title':title})


def display1(request):          
          if not request.user.is_authenticated:
                        return redirect('home')
          has_perm =True
          if request.user.has_perm('paie.view ouled_berhil'):
                   title='Liste des employés'
                   items=Ouled_berhil.objects.all()
                   subjects=Achat_berhil.objects.all()
                   context={ 
                          'has_perm':has_perm, 
                          'title' : title,               
                          'items' : items,
                          'subjects' : subjects,                   
                          'header' : "Ouled_berhils",                    
          }
          else:
                        
                    return redirect('home')
          return render(request,'index.html',context) 



def display11(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          
          subjects=Achat_berhil.objects.all()
          context={
           
           'subjects' : subjects,
           'header' : "Ouled_berhils",
          }
          return render(request,'index.html',context)



def display111(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          title = 'Liste de consommation des engrais'
          form = StockSearchForm(request.POST or None)
          elements=Engrais_berhil.objects.all()
          context={
           "title": title,        
           'elements' : elements,
           'header' : "Engrais_berhils",
           "form": form,
          }
          if request.method == 'POST':          
                  elements = Engrais_berhil.objects.filter(categorie__icontains=form['categorie'].value(),
                                                          
                                                            )
                  context={
                      "form": form,
	                  "title": title,
                      "elements" : elements,
                      'header' : "Engrais_berhils",

                  }                 
				                                 
          return render(request,'engrais.html',context)

def display1111(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          title = 'Liste de consommation des pesticides'
          form = StockSearchPSForm(request.POST or None)
          orderes=Pesticide_berhil.objects.all()
          context={
           "title": title,
           'orderes' : orderes,
           'header' : "Pesticide_berhils",
           "form": form,
          }
          if request.method == 'POST' :                        
                  orderes = Pesticide_berhil.objects.filter(category__icontains=form['category'].value(),
                                                            destination__icontains=form['destination'].value()
                                                           
                                                            )
                  context={
                      "form": form,
	                  "title": title,
                      "orderes" : orderes,
                      'header' : "Pesticide_berhils",
                  }  
          return render(request,'pesticide.html',context)

def caisse1(request):
          
          if not request.user.is_authenticated:
                        return redirect('home')
          has_perm =True
          if request.user.has_perm('paie.view caisse_berhil'):
                        items=caisse_berhil.objects.all()
                        title ='Gestion de la caisse'
          
                        context={  
                                   
                              'items' : items,
                              'title':title,                   
                              'header' : "OD_berhil --"
                                          "OD_drisse --"
                                          "Aoulouz ",
                              'has_perm':has_perm
                    
          }
          else:
                        
                        return redirect('home')

          return render(request,'caisse.html',context) 
          
                 









def delete_desktop(request, pk):
          Ouled_berhil.objects.filter(id=pk).delete()
          items=Ouled_berhil.objects.all()
          context={
                    'items' : items
          }
          return render(request,'index.html', context)





def delete_desktop1(request, pk):
          if not request.user.is_authenticated:
                    return redirect('home')
          Achat_berhil.objects.filter(id=pk).delete()
          subjects=Achat_berhil.objects.all()
          context={
                    'subjects' : subjects
          }
          return render(request,'index.html', context)






def export_excel1(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Ouled_berhil' + \
                  str(datetime.datetime.now()) + '.xls'
                  
              
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Ouled_berhil')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j','base','ancienneté','pf','sb','cnss','amo' , 'net_p']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Ouled_berhil.objects.all().values_list(
                  'np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j',
                  'base','ancienneté','pf','sb','cnss','amo' , 'net_p')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response

def export_excel11(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Engrais_Ouled_berhil' + \
                  str(datetime.datetime.now()) + '.xls'
                  
              
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Engrais_Ouled_berhil')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows= Engrais_berhil.objects.all().values_list(
                  'categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response

def export_excel1111(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Pesticide_Ouled_berhil' + \
                  str(datetime.datetime.now()) + '.xls'
                  
              
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Pesticide_Ouled_berhil')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows= Pesticide_berhil.objects.all().values_list(
                  'category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response

def export_caisse1(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=caisse_berhil' + \
                  str(datetime.datetime.now()) + '.xls'
                  
              
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('caisse_berhil')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=caisse_berhil.objects.all().values_list(
                  'libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response


def export_excel111(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Achat_berhil' + \
                  str(datetime.datetime.now()) + '.xls'
                  
              
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Achat_Ouled_berhil')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['desg','Qté', 'pu', 'pt']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Achat_berhil.objects.all().values_list(
                  'desg','Qté', 'pu', 'pt')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response


########################################################
##########################################################
#********************OULED DRISSE*******************************************  


def display2(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          has_perm =True
          if request.user.has_perm('paie.view ouled_drisse'):
                      title='Liste des employés'
                      items=Ouled_drisse.objects.all()
                      subjects=Achat_drisse.objects.all()

                      context={ 
                              'has_perm':has_perm,
                              'title' : title,
                              'items' : items,
                              'subjects' : subjects,
                              'header' : "Ouled_drisses"
          }
          else:
                        
                    return redirect('home')
          return render(request,'index.html',context)

def caisse2(request):
          if not request.user.is_authenticated:
                        return redirect('home')

          has_perm =True
          if request.user.has_perm('paie.view ouled_drisse'):
                      items=caisse_drisse.objects.all()
                      title ='Gestion de la caisse'

                      context={
                              'has_perm':has_perm,
                              'items' : items,
                              'title':title,
                              'header' : "Ouled_drisse"
          }
          else:
                        
                    return redirect('home')
          return render(request,'caisse.html',context)











def delete_laptop1(request, pk):
          if not request.user.is_authenticated:
                    return redirect('home')
          Achat_drisse.objects.filter(id=pk).delete()
          subjects=Achat_drisse.objects.all()
          context={
                    'subjects' : subjects
          }
          return render(request,'index.html', context)



def display22(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          subjects=Achat_drisse.objects.all()
          context={
           'subjects' : subjects,
           'header' : "Od_drisses"
          }
          return render(request,'index.html',context)




def delete_laptop(request, pk):
          if not request.user.is_authenticated:
                        return redirect('home')
          Ouled_drisse.objects.filter(id=pk).delete()
          items=Ouled_drisse.objects.all()
          context={
                    'items' : items
          }
          return render(request,'index.html', context)






def export_excel2(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Ouled_drisse.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Ouled_drisse')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j','base','ancienneté','pf','sb','cnss','amo' , 'net_p']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Ouled_drisse.objects.all().values_list(
                  'np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j',
                  'base','ancienneté','pf','sb','cnss','amo' , 'net_p')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response             


def export_excel22(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Engrais_Ouled_drisse.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Engrais_Ouled_drisse')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Engrais_drisse.objects.all().values_list(
                  'categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response  

def export_caisse2(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=caisse_drisse.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Ouled_drisse')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=caisse_drisse.objects.all().values_list('libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response


def display2222(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          title = 'Liste des consommations des pesticides'
          form = StockSearchPSForm(request.POST or None)
          orderes=Pesticide_drisse.objects.all()
          context={
           "title": title,
           'orderes' : orderes,
           'header' : "Pesticide_drisses",
           "form": form,
          }
          if request.method == 'POST':          
                  orderes = Pesticide_drisse.objects.filter(category__icontains=form['category'].value(),
                                                           
                                                            )
                  context={
                      "form": form,
	                  "title": title,
                      "orderes" : orderes,

                  }  
          return render(request,'pesticide.html',context)


def display222(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          title = 'Liste des consommations des engrais'
          form = StockSearchForm(request.POST or None)
          elements=Engrais_drisse.objects.all()
          context={
           "title": title,        
           'elements' : elements,
           'header' : "Engrais_drisses",
           "form": form,
          }
          if request.method == 'POST':          
                  elements = Engrais_drisse.objects.filter(categorie__icontains=form['categorie'].value(),
                                                          
                                                            )
                  context={
                      "form": form,
	                  "title": title,
                      "elements" : elements,
                  }                 
				                                 
          return render(request,'engrais.html',context)
def export_excel222(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Achat_Ouled_drisse.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Achat_Ouled_drisse')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['desg','Qté', 'pu', 'pt']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Achat_drisse.objects.all().values_list(
                 'desg','Qté', 'pu', 'pt')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response 
def export_excel2222(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Pesticide_Ouled_drisse.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Pesticide_Ouled_drisse')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Pesticide_drisse.objects.all().values_list(
                  'category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response
############################################################################
#********************AOULOUZ*******************************************
def display3(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          has_perm =True
          if request.user.has_perm('paie.view ouled_drisse'):
                    items=Aoulouz.objects.all()
                    subjects=Achat_Aoulouz.objects.all()
                    title='Liste des employés'
                    context={ 
                        'has_perm':has_perm,
                        'title' : title,
                        'items' : items,
                        'subjects' : subjects,
                        'header' : "Aoulouzs"
          }
          else:
                        
                    return redirect('home')
          return render(request,'index.html',context)


def display333(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          title = 'Liste de consommation des engrais'
          form = StockSearchForm(request.POST or None)
          elements=Engrais_Aoulouz.objects.all()
          context={
           "title": title,        
           'elements' : elements,
           'header' : "Engrais_Aoulouzs",
           "form": form,
          }
          if request.method == 'POST':          
                  elements = Engrais_Aoulouz.objects.filter(categorie__icontains=form['categorie'].value(),
                                                          
                                                            )
                  context={
                      "form": form,
	                  "title": title,
                      "elements" : elements,
                      'header' : "Engrais_Aoulouzs",
                      

                  }                 				                                 
          return render(request,'engrais.html',context)


def display3333(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          title = 'Liste des consommations des pesticides'
          form = StockSearchPSForm(request.POST or None)
          orderes=Pesticide_Aoulouz.objects.all()
          context={
           "title": title,
           'orderes' : orderes,
           'header' : "Pesticide_Aoulouzs",
           "form": form,
          }
          if request.method == 'POST':          
                  orderes = Pesticide_Aoulouz.objects.filter(category__icontains=form['category'].value(),
                                                           
                                                            )
                                                        
                  context={
                      "form": form,
	                  "title": title,
                      "orderes" : orderes,
                      'header' : "Pesticide_Aoulouzs",

                  }  
          return render(request,'pesticide.html',context)


def display33(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          subjects=Achat_Aoulouz.objects.all()
          context={
           'subjects' : subjects,
           'header' : "Aoulozs"
          }
          return render(request,'index.html',context)



def caisse3(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          has_perm =True
          if request.user.has_perm('paie.view ouled_drisse'):
                     items=caisse_Aoulouz.objects.all()
                     title ='Gestion de la caisse'
                     context={
                         'has_perm':has_perm,
                          'items' : items,
                          'title':title,
                          'header' : "Aoulouz"
          }
          else:
                        
                    return redirect('home')
          return render(request,'caisse.html',context)






def delete_mobile(request, pk):
          if not request.user.is_authenticated:
                        return redirect('home')
          Aoulouz.objects.filter(id=pk).delete()
          items=Aoulouz.objects.all()
          context={
                    'items' : items
          }
          return render(request,'index.html', context)

def delete_mobile1(request, pk):
          if not request.user.is_authenticated:
                    return redirect('home')
          Achat_Aoulouz.objects.filter(id=pk).delete()
          subjects=Achat_Aoulouz.objects.all()
          context={
                    'subjects' : subjects
          }
          return render(request,'index.html', context)


def export_excel3(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Aoulouz.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Aoulouz')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j','base','ancienneté','pf','sb','cnss','amo' , 'net_p']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Aoulouz.objects.all().values_list(
                  'np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j',
                  'base','ancienneté','pf','sb','cnss','amo' , 'net_p')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response


def export_excel33(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Engrais_Aoulouz.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Engrais_Aoulouz')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Engrais_Aoulouz.objects.all().values_list(
                  'categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response
def export_excel333(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Achat_Aoulouz.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Achat_Aoulouz')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['desg','Qté', 'pu', 'pt']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Achat_Aoulouz.objects.all().values_list(
                  'desg','Qté', 'pu', 'pt')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response




def export_excel3333(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Pesticide_Aoulouz.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Pesticide_Aoulouz')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Pesticide_Aoulouz.objects.all().values_list(
                  'category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response


def export_caisse3(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=caisse_Aoulouz.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('caisse_Aoulouz')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=caisse_Aoulouz.objects.all().values_list(
                  'libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response







def edit_mobile1(request,pk):
          return edit_achat(request, pk, Achat_Aoulouz, MobileFormo)







def export_excel4(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Mariem.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Mariem')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j','base','ancienneté','pf','sb','cnss','amo' , 'net_p']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Mariem.objects.all().values_list(
                  'np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j',
                  'base','ancienneté','pf','sb','cnss','amo' , 'net_p')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response

def export_excel5(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Plombier.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Plombier')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j','base','ancienneté','pf','sb','cnss','amo' , 'net_p']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Rgaigue.objects.all().values_list(
                  'np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j',
                  'base','ancienneté','pf','sb','cnss','amo' , 'net_p')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response








def detail(request, pk):
              title = 'Detail de rapport'
              article = Article.objects.get(id=pk)         
              return render(request,'detail.html', {"article": article,'title':title})



          
                 






def display4(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          items=Mariem.objects.all()
          title='Liste des employés'
          subjects=Achat_Mariem.objects.all()
          context={
                    'title' : title,
                    'items' : items,
                    'subjects':subjects,
                    'header' : "Mariems"
          }
          return render(request,'index.html',context)

def display5(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          title='Liste des employés'
          items=Rgaigue.objects.all()
          subjects=Achat_rgaigue.objects.all()
          context={
                    'title' : title,
                    'items' : items,
                    'subjects':subjects,
                    'header' : "Plombier"
          }
          return render(request,'index.html',context)

def add_employé(request,cls):
          if not request.user.is_authenticated:
                        return redirect('home')
          if request.method == "POST":
                    form = cls(request.POST)
                    if form.is_valid():
                              form.save()
                              return redirect('index')
          else:
                    form = cls()
                    return render(request,'add_new.html',{'form': form})



###########################################################################
def add_depense(request,cls):
                   
          if request.method == "POST":
                    form = cls(request.POST)
                    if form.is_valid():
                              form.save()
                              return redirect('index')
          else:
                    form = cls()
          return render(request,'ajouter_nv.html',{'form': form})

def add_desktop1(request):
          return add_depense(request,DesktopFormo)

def add_laptop1(request):
          return add_depense(request,LaptopFormo)

def add_mobile1(request):
          return add_depense(request,MobileFormo)
def add_Mariema(request):
          return add_depense(request,MariemFormo)
def add_Rgaiguea(request):
          return add_depense(request,RgaigueFormo)
def add_Rgaiguea(request):
          return add_depense(request,RgaigueFormo)

def add_Rgaiguea(request):
          return add_depense(request,RgaigueFormo)

def add_Rgaiguea(request):
          return add_depense(request,RgaigueFormo)

def add_Rgaiguea(request):
          return add_depense(request,RgaigueFormo)

def add_Rgaiguea(request):
          return add_depense(request,RgaigueFormo)

def add_Rgaiguea(request):
          return add_depense(request,RgaigueFormo)

def add_Rgaiguea(request):
          return add_depense(request,RgaigueFormo)
###########################################################################  





def edit_achat(request, pk, model, cls):
          if not request.user.is_authenticated:
                    return redirect('home')
          subject = get_object_or_404(model, pk=pk)
          if request.method == "POST":
                    form = cls(request.POST, instance=subject)
                    if form.is_valid():
                              form.save()
                              return redirect('index')
          else:
                    form=cls(instance=subject)

                    return render(request,'modifier-item.html', {'form' : form})





def delete_mariem(request, pk):
          if not request.user.is_authenticated:
                        return redirect('home')
          Mariem.objects.filter(id=pk).delete()
          items=Mariem.objects.all()
          context={
                    'items' : items
          }
          return render(request,'index.html', context)

def delete_rgaigue(request, pk):
          if not request.user.is_authenticated:
                        return redirect('home')
          Rgaigue.objects.filter(id=pk).delete()
          items=Rgaigue.objects.all()
          context={
                    'items' : items
          }
          return render(request,'index.html', context)



def delete_lglidi(request, pk):
          if not request.user.is_authenticated:
                        return redirect('home')
          lglidi.objects.filter(id=pk).delete()
          items=lglidi.objects.all()
          context={
                    'items' : items
          }
          return render(request,'index.html', context)

def delete_benmbark(request, pk):
          if not request.user.is_authenticated:
                        return redirect('home')
          benmbark.objects.filter(id=pk).delete()
          items=benmbark.objects.all()
          context={
                    'items' : items
          }
          return render(request,'index.html', context)


def delete_raisin(request, pk):
          if not request.user.is_authenticated:
                        return redirect('home')
          raisin.objects.filter(id=pk).delete()
          items=raisin.objects.all()
          context={
                    'items' : items
          }
          return render(request,'index.html', context)

def delete_bananier1(request, pk):
          if not request.user.is_authenticated:
                        return redirect('home')
          bananier1.objects.filter(id=pk).delete()
          items=bananier1.objects.all()
          context={
                    'items' : items
          }
          return render(request,'index.html', context)


def delete_bananier2(request, pk):
          if not request.user.is_authenticated:
                        return redirect('home')
          bananier2.objects.filter(id=pk).delete()
          items=bananier2.objects.all()
          context={
                    'items' : items
          }
          return render(request,'index.html', context)

def delete_zbirate(request, pk):
          if not request.user.is_authenticated:
                        return redirect('home')
          zbirate.objects.filter(id=pk).delete()
          items=zbirate.objects.all()
          context={
                    'items' : items
          }
          return render(request,'index.html', context)


def delete_maryem2(request, pk):
          if not request.user.is_authenticated:
                        return redirect('home')
          Maryem2.objects.filter(id=pk).delete()
          items=Maryem2.objects.all()
          context={
                    'items' : items
          }
          return render(request,'index.html', context)
#############################################################
def caisse(request):             
          if not request.user.is_authenticated:
                        return redirect('home')
          title ='Gestion de la caisse'
          return render(request,'caisse.html',{'title':title})


"""""
#################################################################
#################################################################
#################################################################


          """""


           


def export_excel44(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Engrais_Mariem.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Engrais_Mariem')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Engrais_Mariem.objects.all().values_list(
                  'categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response

def export_excel55(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Engrais_Plombier.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Engrais_plombier')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Engrais_Rgaigue.objects.all().values_list(
                  'categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response
              ##################################
def engrais(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          return render(request,'engrais.html')


def display444(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          title = 'Liste de consommation des engrais'
          form = StockSearchForm(request.POST or None)
          elements=Engrais_Mariem.objects.all()
          context={
           "title": title,        
           'elements' : elements,
           'header' : "Engrais Hawara",
           "form": form,
          }
          if request.method == 'POST':          
                  elements = Engrais_Mariem.objects.filter(categorie__icontains=form['categorie'].value(),
                                                          
                                                            )
                  context={
                      "form": form,
	                  "title": title,
                      "elements" : elements,
                      'header' : "Engrais Hawara",

                  }                 
				                                 
          return render(request,'engrais.html',context)
def display555(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          title = 'Liste des consommations des engrais'
          form = StockSearchForm(request.POST or None)
          elements=Engrais_Rgaigue.objects.all()
          context={
           "title": title,        
           'elements' : elements,
           'header' : "engrais_plombier",
           "form": form,
          }
          if request.method == 'POST':          
                  elements = Engrais_Rgaigue.objects.filter(categorie__icontains=form['categorie'].value(),
                                                          
                                                            )
                  context={
                      "form": form,
	                  "title": title,
                      "elements" : elements,
                  }                 
				                                 
          return render(request,'engrais.html',context)
##########################################################################
# #######################################################################          
def add_consomation(request,cls):
          if not request.user.is_authenticated:
                        return redirect('home')         
          if request.method == "POST":
                    form = cls(request.POST)
                    if form.is_valid():
                              form.save()
                              return redirect('engrais')
          else:
                    form = cls()
          return render(request,'add_engrais.html',{'form': form})
def add_desktop111(request):
          return add_consomation(request,EngraisBRForm)

def add_laptop111(request):
          return add_consomation(request,EngraisDRForm)

def add_mobile111(request):
          return add_consomation(request,EngraisAOForm)


def edit_consomation(request, pk, model, cls):
          if not request.user.is_authenticated:
                    return redirect('home')
          subject = get_object_or_404(model, pk=pk)
          if request.method == "POST":
                    form = cls(request.POST, instance=subject)
                    if form.is_valid():
                              form.save()
                              return redirect('engrais')
          else:
                    form=cls(instance=subject)
                    return render(request,'modifier-item.html', {'form' : form})    




"""""
#################################################################
#################################################################
#################################################################
"""""



             


def export_excel4444(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Pesticide_Mariem.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Pesticide_Mariem')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Pesticide_Mariem.objects.all().values_list(
                  'category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response

def export_excel5555(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Pesticide_plombier.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Pesticide_plombier')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Pesticide_Rgaigue.objects.all().values_list(
                  'category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response










def display4444(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          title = 'Liste de consommation des pesticides'
          form = StockSearchPSForm(request.POST or None)
          orderes=Pesticide_Mariem.objects.all()
          context={
           "title": title,
           'orderes' : orderes,
           'header' : "Pesticide Hawara",
           "form": form,
          }
          if request.method == 'POST':                        
                  orderes = Pesticide_Mariem.objects.filter(category__icontains=form['category'].value(),
                                                           
                                                            )
                  context={
                      "form": form,
	                  "title": title,
                      "orderes" : orderes,
                      'header' : "Pesticide Hawara",
                  }  
          return render(request,'pesticide.html',context)
def display5555(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          title = 'Liste des consommations des pesticides'
          form = StockSearchPSForm(request.POST or None)
          orderes=Pesticide_Rgaigue.objects.all()
          context={
           "title": title,
           'orderes' : orderes,
           'header' : "Pesticide_Rgaigues",
           "form": form,
          }
          if request.method == 'POST':          
                  orderes = Pesticide_Rgaigue.objects.filter(category__icontains=form['category'].value(),
                                                           
                                                            )
                  context={
                      "form": form,
	                  "title": title,
                      "orderes" : orderes,

                  }  
          return render(request,'pesticide.html',context)

###############################################################
def display666(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          title = 'Liste de consommation des Engrais'
          form = StockSearchForm(request.POST or None)
          elements=Engrais_Maryem2.objects.all()
          context={
           "title": title,
           'elements' : elements,
           'header' : "engrais_maryem2",
           "form": form,
          }
          if request.method == 'POST':                        
                  elements = Engrais_Maryem2.objects.filter(categorie__icontains=form['categorie'].value(),
                                                           
                                                            )
                  context={
                      "form": form,
	                  "title": title,
                      "elements" : elements,
                  }  
          return render(request,'engrais.html',context)

def display6666(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          title = 'Liste de consommation des pesticides'
          form = StockSearchPSForm(request.POST or None)
          orderes=Pesticide_Maryem2.objects.all()
          context={
           "title": title,
           'orderes' : orderes,
           'header' : "Pesticide_maryem2",
           "form": form,
          }
          if request.method == 'POST':                        
                  orderes = Pesticide_Maryem2.objects.filter(category__icontains=form['category'].value(),
                                                           
                                                            )
                  context={
                      "form": form,
	                  "title": title,
                      "orderes" : orderes,
                  }  
          return render(request,'pesticide.html',context)

def export_excel66(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Engrais_maryem2.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Engrais_maryem2')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Engrais_Maryem2.objects.all().values_list(
                  'categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response

def export_excel6666(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Pesticide_maryem2.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Pesticide_maryem2')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['category','date','entree','cumul_entree','sortie','cumul_sortie','stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Pesticide_Maryem2.objects.all().values_list(
                  'category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response
#############################################################
def display777(request):
            if not request.user.is_authenticated:
                    return redirect('home')
            title = 'Liste des consommations des Engrais'
            form = StockSearchForm(request.POST or None)
            elements=Engrais_zbirate.objects.all()
            context={
            "title": title,
            'elements' : elements,
            'header' : "engrais_zbirate",
            "form": form,
          }
            if request.method == 'POST':          
                  elements = Engrais_zbirate.objects.filter(categorie__icontains=form['categorie'].value(),
                                                           
                                                            )
                  context={
                      "form": form,
	                  "title": title,
                      "elements" : elements,

                  }  
            return render(request,'engrais.html',context)


def display7777(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          title = 'Liste des consommations des pesticides'
          form = StockSearchPSForm(request.POST or None)
          orderes=Pesticide_zbirate.objects.all()
          context={
           "title": title,
           'orderes' : orderes,
           'header' : "Pesticide_zbirate",
           "form": form,
          }
          if request.method == 'POST':          
                  orderes = Pesticide_drisse.objects.filter(category__icontains=form['category'].value(),
                                                           
                                                            )
                  context={
                      "form": form,
	                  "title": title,
                      "orderes" : orderes,

                  }  
          return render(request,'pesticide.html',context)


def export_excel77(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Engrais_zbirate.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Engrais_zbirate')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Engrais_zbirate.objects.all().values_list(
                  'categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response


def export_excel7777(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Pesticide_zbirate.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Pesticide_zbirate')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Pesticide_zbirate.objects.all().values_list(
                  'category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response



def export_excel77(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Engrais_zbirate.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Engrais_zbirate')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Engrais_zbirate.objects.all().values_list(
                  'categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response


def export_excel88(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Engrais_bananier2.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Engrais_bananier2')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Engrais_bananier2.objects.all().values_list(
                  'categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response

def export_excel99(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Engrais_bananier1.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Engrais_bananier1')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Engrais_bananier1.objects.all().values_list(
                  'categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response



def export_excel10(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Engrais_raisin.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Engrais_raisin')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Engrais_raisin.objects.all().values_list(
                  'categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response



def export_excelb(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Engrais_benmbark.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Engrais_benmbark')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Engrais_benmbark.objects.all().values_list(
                  'categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response



def export_excel12(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Engrais_lglidi.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Engrais_lglidi')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Engrais_lglidi.objects.all().values_list(
                  'categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response








def display8888(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          title = 'Liste des consommations des pesticides'
          form = StockSearchPSForm(request.POST or None)
          orderes=Pesticide_bananier2.objects.all()
          context={
           "title": title,
           'orderes' : orderes,
           'header' : "Pesticide_bananier2",
           "form": form,
          }
          if request.method == 'POST':          
                  orderes = Pesticide_bananier2.objects.filter(category__icontains=form['category'].value(),
                                                           
                                                            )
                                                        
                  context={
                      "form": form,
	                  "title": title,
                      "orderes" : orderes,

                  }  
          return render(request,'pesticide.html',context)



def display888(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          title = 'Liste des consommations des engraiss'
          form = StockSearchPSForm(request.POST or None)
          elements=Engrais_bananier2.objects.all()
          context={
           "title": title,
           'elements' :elements,
           'header' : "Engrais_bananier2",
           "form": form,
          }
          if request.method == 'POST':          
                  elements = Engrais_bananier2.objects.filter(categorie__icontains=form['categorie'].value(),
                                                           
                                                            )
                                                        
                  context={
                      "form": form,
	                  "title": title,
                      'elements' :elements,

                  }  
          return render(request,'engrais.html',context)

def display999(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          title = 'Liste des consommations des engraiss'
          form = StockSearchPSForm(request.POST or None)
          elements=Engrais_bananier1.objects.all()
          context={
           "title": title,
           'elements' :elements,
           'header' : "Engrais_bananier1",
           "form": form,
          }
          if request.method == 'POST':          
                  elements = Engrais_bananier1.objects.filter(categorie__icontains=form['categorie'].value(),
                                                           
                                                            )
                                                        
                  context={
                      "form": form,
	                  "title": title,
                      'elements' :elements,

                  }  
          return render(request,'engrais.html',context)



def display100(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          title = 'Liste des consommations des engraiss'
          form = StockSearchPSForm(request.POST or None)
          elements=Engrais_raisin.objects.all()
          context={
           "title": title,
           'elements' :elements,
           'header' : "Engrais_raisin",
           "form": form,
          }
          if request.method == 'POST':          
                  elements = Engrais_raisin.objects.filter(categorie__icontains=form['categorie'].value(),
                                                           
                                                            )
                                                        
                  context={
                      "form": form,
	                  "title": title,
                      'elements' :elements,

                  }  
          return render(request,'engrais.html',context)

def display101(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          title = 'Liste des consommations des engraiss'
          form = StockSearchPSForm(request.POST or None)
          elements=Engrais_benmbark.objects.all()
          context={
           "title": title,
           'elements' :elements,
           'header' : "Engrais_benmbark",
           "form": form,
          }
          if request.method == 'POST':          
                  elements = Engrais_benmbark.objects.filter(categorie__icontains=form['categorie'].value(),
                                                           
                                                            )
                                                        
                  context={
                      "form": form,
	                  "title": title,
                      'elements' :elements,

                  }  
          return render(request,'engrais.html',context)



def display102(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          title = 'Liste des consommations des engraiss'
          form = StockSearchPSForm(request.POST or None)
          elements=Engrais_lglidi.objects.all()
          context={
           "title": title,
           'elements' :elements,
           'header' : "Engrais_lglidi",
           "form": form,
          }
          if request.method == 'POST':          
                  elements = Engrais_lglidi.objects.filter(categorie__icontains=form['categorie'].value(),
                                                           
                                                            )
                                                        
                  context={
                      "form": form,
	                  "title": title,
                      'elements' :elements,

                  }  
          return render(request,'engrais.html',context)



def export_excel888(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Engrais_bananier2.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Engrais_bananier2')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Engrais_bananier2.objects.all().values_list(
                  'categorie','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response


def export_excel8888(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Pesticide_bananier2.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Pesticide_bananier2')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Pesticide_bananier2.objects.all().values_list(
                  'category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response

def display9999(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          title = 'Liste de consommation des pesticides'
          form = StockSearchPSForm(request.POST or None)
          orderes=Pesticide_bananier1.objects.all()
          context={
           "title": title,
           'orderes' : orderes,
           'header' : "Pesticide_bananier1",
           "form": form,
          }
          if request.method == 'POST':                        
                  orderes = Pesticide_Mariem.objects.filter(category__icontains=form['category'].value(),
                                                           
                                                            )
                  context={
                      "form": form,
	                  "title": title,
                      "orderes" : orderes,
                  }  
          return render(request,'pesticide.html',context)

def export_excel999(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Engrais_bananier1.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Engrais_bananier1')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Engrais_bananier1.objects.all().values_list(
                  'category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response
def export_excel9999(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Pesticide_bananier1.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Pesticide_bananier1')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Pesticide_bananier1.objects.all().values_list(
                  'category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response

def display1010(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          title = 'Liste des consommations des pesticides'
          form = StockSearchPSForm(request.POST or None)
          orderes=Pesticide_raisin.objects.all()
          context={
           "title": title,
           'orderes' : orderes,
           'header' : "Pesticide_raisin",
           "form": form,
          }
          if request.method == 'POST':          
                  orderes = Pesticide_Rgaigue.objects.filter(category__icontains=form['category'].value(),
                                                           
                                                            )
                  context={
                      "form": form,
	                  "title": title,
                      "orderes" : orderes,

                  }  
          return render(request,'pesticide.html',context)


def export_excel100(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Engrais_raisin.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Engrais_raisin')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Engrais_raisin.objects.all().values_list(
                  'category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response

def export_excel1010(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Pesticide_raisin.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Pesticide_raisin')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Pesticide_raisin.objects.all().values_list(
                  'category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response


def display1011(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          title = 'Liste de consommation des pesticides'
          form = StockSearchPSForm(request.POST or None)
          orderes=Pesticide_benmbark.objects.all()
          context={
           "title": title,
           'orderes' : orderes,
           'header' : "Pesticide_benmbark",
           "form": form,
          }
          if request.method == 'POST':                        
                  orderes = Pesticide_Mariem.objects.filter(category__icontains=form['category'].value(),
                                                           
                                                            )
                  context={
                      "form": form,
	                  "title": title,
                      "orderes" : orderes,
                  }  
          return render(request,'pesticide.html',context)

def export_excel101(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Engrais_benmbark.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Engrais_benmbark')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Engrais_benmbark.objects.all().values_list(
                  'category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response

def export_excel1011(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Pesticide_benmbark.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Pesticide_benmbark')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Pesticide_benmbark.objects.all().values_list(
                  'category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response

def display1012(request):
          if not request.user.is_authenticated:
                    return redirect('home')
          title = 'Liste des consommations des pesticides'
          form = StockSearchPSForm(request.POST or None)
          orderes=Pesticide_lglidi.objects.all()
          context={
           "title": title,
           'orderes' : orderes,
           'header' : "Pesticide_lglidi",
           "form": form,
          }
          if request.method == 'POST':          
                  orderes = Pesticide_Rgaigue.objects.filter(category__icontains=form['category'].value(),
                                                           
                                                            )
                  context={
                      "form": form,
	                  "title": title,
                      "orderes" : orderes,

                  }  
          return render(request,'pesticide.html',context)

def export_excel102(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Engrais_lglidi.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Engrais_lglidi')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Engrais_lglidi.objects.all().values_list(
                  'category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response


def export_excel1012(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Pesticide_lglidi.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Pesticide_lglidi')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Pesticide_lglidi.objects.all().values_list(
                  'category','date','entree', 'cumul_entree', 'sortie', 'cumul_sortie', 'stock')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response
          ######################################################
################################################################
def add_consomme(request,cls):
          if not request.user.is_authenticated:
                        return redirect('home')         
          if request.method == "POST":
                    form = cls(request.POST)
                    if form.is_valid():
                              form.save()
                              return redirect('pesticide')
          else:
                    form = cls()
          return render(request,'add_engrais.html',{'form': form})


def edit_pesti(request, pk, model, cls):
          if not request.user.is_authenticated:
                    return redirect('home')
          subject = get_object_or_404(model, pk=pk)
          if request.method == "POST":
                    form = cls(request.POST, instance=subject)
                    if form.is_valid():
                              form.save()
                              return redirect('pesticide')
          else:
                    form=cls(instance=subject)

                    return render(request,'modifier-item.html', {'form' : form})    





class AddArticle(CreateView):
          model=Article
          form_class=ArticleForm
          template_name='ajouter-article.html'
          success_url="/my-admin/my-articles"

          def form_valid(self,form):
          
                    form.instance.user=self.request.user
                    return super().form_valid(form)  
#################################################################
###################################################################
#######################################################################






def caisse4(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          items=caisse_Mariem.objects.all()
          title ='Gestion de la caisse'
          context={
                    'items' : items,
                    'title':title,
                    'header' : "Hawara"
          }
          return render(request,'caisse.html',context)

def caisse5(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          items=caisse_Rgaigue.objects.all()
          title ='Gestion de la caisse'
          context={
                    'items' : items,
                    'title':title,
                    'header' : "Plombier"
          }
          return render(request,'caisse.html',context)
#####################################################################
#####################################################################
#####################################################################


########################################################
########################################################
########################################################
             



def export_caisse4(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=caisse_Mariem.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('caisse_Mariem')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=caisse_Mariem.objects.all().values_list(
                  'libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response

def export_caisse5(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=caisse_plombier.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('caisse_plombier')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=caisse_Rgaigue.objects.all().values_list(
                  'libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response









########################################################
##########################################################

###########################################################
            



def export_excel444(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Achat_Mariem.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Achat_Mariem')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['desg','Qté', 'pu', 'pt']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Achat_Mariem.objects.all().values_list(
                  'desg','Qté', 'pu', 'pt')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response

def export_excel555(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Achat_plombier.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Achat_plombier')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['desg','Qté', 'pu', 'pt']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Achat_rgaigue.objects.all().values_list(
                  'desg','Qté', 'pu', 'pt')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response









def edit_achat(request, pk, model, cls):
          if not request.user.is_authenticated:
                    return redirect('home')
          subject = get_object_or_404(model, pk=pk)
          if request.method == "POST":
                    form = cls(request.POST, instance=subject)
                    if form.is_valid():
                              form.save()
                              return redirect('index')
          else:
                    form=cls(instance=subject)

                    return render(request,'modifier-item.html', {'form' : form})    
                        

#########____________________________###########################____________________

def display6(request):
          
          if not request.user.is_authenticated:
                        return redirect('home')
          items=lglidi.objects.all()
          title='Liste des employés'
          subjects=Achat_lglidi.objects.all()
          context={  
                    'title' : title,              
                    'items' : items,
                    'subjects' : subjects,                   
                    'header' : "lglidi",
                    
          }
          return render(request,'index.html',context) 


def display7(request):
          
          if not request.user.is_authenticated:
                        return redirect('home')
          items=benmbark.objects.all()
          title='Liste des employés'
          subjects=Achat_benmbark.objects.all()
          context={  
                     'title' : title,              
                    'items' : items,
                    'subjects' : subjects,                   
                    'header' : "benmbark",
                    
          }
          return render(request,'index.html',context) 


def display8(request):
          
          if not request.user.is_authenticated:
                        return redirect('home')
          items=raisin.objects.all()
          title='Liste des employés'
          subjects=Achat_raisin.objects.all()
          context={  
                     'title' : title,              
                    'items' : items,
                    'subjects' : subjects,                   
                    'header' : "raisin",
                    
          }
          return render(request,'index.html',context) 


def display9(request):
          
          if not request.user.is_authenticated:
                        return redirect('home')
          items=bananier1.objects.all()
          title='Liste des employés'
          subjects=Achat_bananier1.objects.all()
          context={  
                     'title' : title,              
                    'items' : items,
                    'subjects' : subjects,                   
                    'header' : "bananier1",
                    
          }
          return render(request,'index.html',context) 

def displayban2(request):
          
          if not request.user.is_authenticated:
                        return redirect('home')
          items=bananier2.objects.all()
          title='Liste des employés'
          subjects=Achat_bananier2.objects.all()
          context={  
                    'title' : title,               
                    'items' : items,
                    'subjects' : subjects,                   
                    'header' : "bananier2",
                    
          }
          return render(request,'index.html',context) 

def displayzbi(request):
          
          if not request.user.is_authenticated:
                        return redirect('home')
          items=zbirate.objects.all()
          title='Liste des employés'
          subjects=Achat_zbirate.objects.all()
          context={  
                    'title' : title,               
                    'items' : items,
                    'subjects' : subjects,                   
                    'header' : "zbirate",
                    
          }
          return render(request,'index.html',context) 

def displaymar(request):
          
          if not request.user.is_authenticated:
                        return redirect('home')
          items=Maryem2.objects.all()
          title='Liste des employés'
          subjects=Achat_Maryem2.objects.all()
          context={  
                    'title' : title,              
                    'items' : items,
                    'subjects' : subjects,                   
                    'header' : "maryem2",
                    
          }
          return render(request,'index.html',context) 

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
def export_ouvgli(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=lglidi' + \
                  str(datetime.datetime.now()) + '.xls'
                  
              
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('lglidi')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j','base','ancienneté','pf','sb','cnss','amo' , 'net_p']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=lglidi.objects.all().values_list(
                  'np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j',
                  'base','ancienneté','pf','sb','cnss','amo' , 'net_p')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response 
def export_achatgli(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Achat_lglidi' + \
                  str(datetime.datetime.now()) + '.xls'
                  
              
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Achat_lglidi')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['desg','Qté', 'pu', 'pt']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Achat_lglidi.objects.all().values_list(
                  'desg','Qté', 'pu', 'pt')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response



def export_ouvbenm(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=benmbark' + \
                  str(datetime.datetime.now()) + '.xls'
                  
              
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('benmbark')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j','base','ancienneté','pf','sb','cnss','amo' , 'net_p']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=benmbark.objects.all().values_list(
                  'np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j',
                  'base','ancienneté','pf','sb','cnss','amo' , 'net_p')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response 




def export_achatbenm(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Achat_benmbark' + \
                  str(datetime.datetime.now()) + '.xls'
                  
              
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Achat_benmbark')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['desg','Qté', 'pu', 'pt']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Achat_benmbark.objects.all().values_list(
                  'desg','Qté', 'pu', 'pt')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response


def export_ouvzbi(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=zbirate' + \
                  str(datetime.datetime.now()) + '.xls'
                  
              
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('zbirate')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j','base','ancienneté','pf','sb','cnss','amo' , 'net_p']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=zbirate.objects.all().values_list(
                  'np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j',
                  'base','ancienneté','pf','sb','cnss','amo' , 'net_p')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response        
          




def export_achatzbi(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Achat_zbirate' + \
                  str(datetime.datetime.now()) + '.xls'
                  
              
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Achat_zbirate')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['desg','Qté', 'pu', 'pt']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Achat_zbirate.objects.all().values_list(
                  'desg','Qté', 'pu', 'pt')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response


def export_ouvmer(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=maryem2' + \
                  str(datetime.datetime.now()) + '.xls'
                  
              
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('maryem2')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j','base','ancienneté','pf','sb','cnss','amo' , 'net_p']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Maryem2.objects.all().values_list(
                  'np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j',
                  'base','ancienneté','pf','sb','cnss','amo' , 'net_p')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response        
          




def export_achatmer(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Achat_maryem2' + \
                  str(datetime.datetime.now()) + '.xls'
                  
              
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Achat_maryem2')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['desg','Qté', 'pu', 'pt']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Achat_Maryem2.objects.all().values_list(
                  'desg','Qté', 'pu', 'pt')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response



def export_ouvban1(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=bananier1' + \
                  str(datetime.datetime.now()) + '.xls'
                  
              
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('bananier1')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j','base','ancienneté','pf','sb','cnss','amo' , 'net_p']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=bananier1.objects.all().values_list(
                  'np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j',
                  'base','ancienneté','pf','sb','cnss','amo' , 'net_p')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response        
          




def export_achatban1(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Achat_bananier1' + \
                  str(datetime.datetime.now()) + '.xls'
                  
              
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Achat_bananier1')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['desg','Qté', 'pu', 'pt']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Achat_bananier1.objects.all().values_list(
                  'desg','Qté', 'pu', 'pt')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response

def export_ouvban2(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=bananier2' + \
                  str(datetime.datetime.now()) + '.xls'
                  
              
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('bananier2')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j','base','ancienneté','pf','sb','cnss','amo' , 'net_p']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=bananier2.objects.all().values_list(
                  'np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j',
                  'base','ancienneté','pf','sb','cnss','amo' , 'net_p')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response        
          




def export_achatban2(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Achat_bananier2' + \
                  str(datetime.datetime.now()) + '.xls'
                  
              
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Achat_bananier2')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['desg','Qté', 'pu', 'pt']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Achat_bananier2.objects.all().values_list(
                  'desg','Qté', 'pu', 'pt')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response

def export_ouvrais(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=raisin' + \
                  str(datetime.datetime.now()) + '.xls'
                  
              
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('raisin')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j','base','ancienneté','pf','sb','cnss','amo' , 'net_p']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=raisin.objects.all().values_list(
                  'np','sdb', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'nb_j',
                  'base','ancienneté','pf','sb','cnss','amo' , 'net_p')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response        
          




def export_achatrais(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=Achat_raisin' + \
                  str(datetime.datetime.now()) + '.xls'
                  
              
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('Achat_raisin')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['desg','Qté', 'pu', 'pt']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=Achat_raisin.objects.all().values_list(
                  'desg','Qté', 'pu', 'pt')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response
###################################################################
###################caisse##########################""
def export_caisse6(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=caisse_lglidi.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('caisse_lglidi')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=caisse_lglidi.objects.all().values_list(
                  'libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response

def export_caisse7(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=caisse_benmbark.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('caisse_benmbark')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=caisse_benmbark.objects.all().values_list(
                  'libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response


def export_caisse8(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=caisse_raisin.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('caisse_raisin')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=caisse_raisin.objects.all().values_list(
                  'libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response


def export_caisse9(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=caisse_bananier1.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('caisse_bananier1')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=caisse_bananier1.objects.all().values_list(
                  'libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response

def export_caisse10(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=caisse_bananier2.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('caisse_bananier2')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=caisse_bananier2.objects.all().values_list(
                  'libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response

def export_caisse11(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=caisse_zbirate.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('caisse_zbirate')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=caisse_zbirate.objects.all().values_list(
                  'libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response


def export_caisse12(request):
              
              response=HttpResponse(content_type='application/ms-excel')
              response['Content-Disposition']='attachment; filename=caisse_maryem2.xls'
                  
              wb = xlwt.Workbook(encoding='utf-8')
              ws = wb.add_sheet('caisse_maryem2')
              row_num=0
              font_style=xlwt.XFStyle()
              font_style.font.bold=True
              columns=['libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde']
              for col_num in range(len(columns)):
                            ws.write(row_num, col_num,columns[col_num],font_style)
              font_style=xlwt.XFStyle()
              rows=caisse_Maryem2.objects.all().values_list(
                  'libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde')

              for row in rows:
                            row_num+=1
                            for col_num in range(len(row)):
                                          ws.write(row_num,col_num,str(row[col_num]),font_style)
              wb.save(response)
              return response
#########################################display###################

def caisse6(request):
          
          if not request.user.is_authenticated:
                        return redirect('home')
          items=caisse_lglidi.objects.all()
          title ='Gestion de la caisse'
          context={  
                                   
                    'items' : items,
                    'title' :title,                   
                    'header' : "Lglidi",
                    
          }
          return render(request,'caisse.html',context) 

def caisse7(request):
          
          if not request.user.is_authenticated:
                        return redirect('home')
          items=caisse_benmbark.objects.all()
          title ='Gestion de la caisse'
          context={  
                                   
                    'items' : items,
                    'title':  title,                   
                    'header' : "Benmbark",
                    
          }
          return render(request,'caisse.html',context)

def caisse8(request):
          
          if not request.user.is_authenticated:
                        return redirect('home')
          items=caisse_raisin.objects.all()
          title ='Gestion de la caisse'
          context={  
                                   
                    'items' : items,
                    'title':title,                   
                    'header' : "Raisin",
                    
          }
          return render(request,'caisse.html',context)

def caisse9(request):
          
          if not request.user.is_authenticated:
                        return redirect('home')
          items=caisse_bananier1.objects.all()
          title ='Gestion de la caisse'
          context={  
                                   
                    'items' : items,
                    'title':title,                  
                    'header' : "Bananier1",
                    
          }
          return render(request,'caisse.html',context)

def caisse10(request):
          
          if not request.user.is_authenticated:
                        return redirect('home')
          title ='Gestion de la caisse'
          items=caisse_bananier2.objects.all()
          
          context={  
                                   
                    'items' : items,
                    'title' : title,
                                       
                    'header' : "Bananier2",
                    
          }
          return render(request,'caisse.html',context)
def caisse11(request):
          
          if not request.user.is_authenticated:
                        return redirect('home')
          title ='Gestion de la caisse'             
          items=caisse_zbirate.objects.all()
          
          context={  
                                   
                    'items' : items,
                     'title' : title,                   
                    'header' : "Zbirate",
                    
          }
          return render(request,'caisse.html',context)

def caisse12(request):
          
          if not request.user.is_authenticated:
                        return redirect('home')

          title ='Gestion de la caisse'
          items=caisse_Maryem2.objects.all()
          
          context={  
                                   
                    'items' : items,
                     'title':title,                  
                    'header' : "Maryem2",
                    
          }
          return render(request,'caisse.html',context)
