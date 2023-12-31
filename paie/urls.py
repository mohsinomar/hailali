from django.urls import re_path
from . views import *

urlpatterns=[
          re_path(r'^$',home,name='home'),
          
          re_path(r'^detail/(?P<pk>\d+)$',detail,name='detail'),
          re_path(r'^add-pub$',AddArticle.as_view(),name='add-pub'),
          re_path(r'^index$',index,name='index'),
          
          re_path(r'^caisse$',caisse,name='caisse'),                   
          re_path(r'^display1$',display1,name='display1'),
          re_path(r'^display2$',display2,name='display2'),
          re_path(r'^display3$',display3,name='display3'),
          re_path(r'^display4$',display4,name='display4'),
          re_path(r'^display5$',display5,name='display5'),
          re_path(r'^display6$',display6,name='display6'),
          re_path(r'^display7$',display7,name='display7'),
          re_path(r'^display8$',display8,name='display8'),
          re_path(r'^display9$',display9,name='display9'),
          re_path(r'^displayban2$',displayban2,name='displayban2'),
          re_path(r'^displayzbi$',displayzbi,name='displayzbi'),
          re_path(r'^displaymar$',displaymar,name='displaymar'),
          re_path(r'^display11$',display11,name='display11'),
          re_path(r'^display22$',display22,name='display22'),
          re_path(r'^display33$',display33,name='display33'),
          
          
          re_path(r'^delete_desktop1/(?P<pk>\d+)$',delete_desktop1,name='delete_desktop1'),
          re_path(r'^delete_laptop1/(?P<pk>\d+)$',delete_laptop1,name='delete_laptop1'),
          re_path(r'^delete_mobile1/(?P<pk>\d+)$',delete_mobile1,name='delete_mobile1'),
          #######################################################
          re_path(r'^caisse1$',caisse1,name='caisse1'),
          re_path(r'^caisse2$',caisse2,name='caisse2'),
          re_path(r'^caisse3$',caisse3,name='caisse3'),
          re_path(r'^caisse4$',caisse4,name='caisse4'),
          re_path(r'^caisse5$',caisse5,name='caisse5'),
          re_path(r'^caisse6$',caisse6,name='caisse6'),
          re_path(r'^caisse7$',caisse7,name='caisse7'),
          re_path(r'^caisse8$',caisse8,name='caisse8'),
          re_path(r'^caisse9$',caisse9,name='caisse9'),
          re_path(r'^caisse10$',caisse10,name='caisse10'),
          re_path(r'^caisse11$',caisse11,name='caisse11'),
          re_path(r'^caisse12$',caisse12,name='caisse12'),
          #####################################################
         
          re_path(r'^ajouter-employé11$',add_desktop1,name='ajouter-employé11'),
          re_path(r'^ajouter-employé22$',add_laptop1,name='ajouter-employé22'),
          re_path(r'^ajouter-employé33$',add_mobile1,name='ajouter-employé33'),
          re_path(r'^ajouter-employé44$',add_Mariema,name='ajouter-employé44'),
          re_path(r'^ajouter-employé55$',add_Rgaiguea,name='ajouter-employé55'),
          
          re_path(r'^edit_mobile1/(?P<pk>\d+)$',edit_mobile1,name='edit_mobile1'),
          re_path(r'^delete_desktop/(?P<pk>\d+)$',delete_desktop,name='delete_desktop'),
          re_path(r'^delete_laptop/(?P<pk>\d+)$',delete_laptop,name='delete_laptop'),
          re_path(r'^delete_mobile/(?P<pk>\d+)$',delete_mobile,name='delete_mobile'),
          re_path(r'^delete_mariem/(?P<pk>\d+)$',delete_mariem,name='delete_mariem'),
          re_path(r'^delete_rgaigue/(?P<pk>\d+)$',delete_rgaigue,name='delete_rgaigue'),
          re_path(r'^export_mobile1$',export_excel1,name='export_mobile1'),
          re_path(r'^export_mobile2$',export_excel2,name='export_mobile2'),
          re_path(r'^export_mobile3$',export_excel3,name='export_mobile3'),
          re_path(r'^export_mobile4$',export_excel4,name='export_mobile4'),
          re_path(r'^export_mobile5$',export_excel5,name='export_mobile5'),
          re_path(r'^export_mobile111$',export_excel111,name='export_mobile111'),
          re_path(r'^export_mobile222$',export_excel222,name='export_mobile222'),
          re_path(r'^export_mobile333$',export_excel333,name='export_mobile333'),
          re_path(r'^export_mobile444$',export_excel444,name='export_mobile444'),
          re_path(r'^export_mobile555$',export_excel555,name='export_mobile555'),
          
          re_path(r'^export_mobile888$',export_excel888,name='export_mobile888'),
          re_path(r'^export_mobile999$',export_excel999,name='export_mobile999'),
          re_path(r'^export_mobile100$',export_excel100,name='export_mobile100'),
          re_path(r'^export_mobile101$',export_excel101,name='export_mobile101'),
          re_path(r'^export_mobile102$',export_excel102,name='export_mobile102'),
          re_path(r'^export_mobile1111$',export_excel1111,name='export_mobile1111'),
          re_path(r'^export_mobile2222$',export_excel2222,name='export_mobile2222'),
          re_path(r'^export_mobile3333$',export_excel3333,name='export_mobile3333'),
          re_path(r'^export_mobile4444$',export_excel4444,name='export_mobile4444'),
          re_path(r'^export_mobile5555$',export_excel5555,name='export_mobile5555'),
          re_path(r'^export_mobile6666$',export_excel6666,name='export_mobile6666'),
          re_path(r'^export_mobile7777$',export_excel7777,name='export_mobile7777'),
          re_path(r'^export_mobile8888$',export_excel8888,name='export_mobile8888'),
          re_path(r'^export_mobile9999$',export_excel9999,name='export_mobile9999'),
          re_path(r'^export_mobile1010$',export_excel1010,name='export_mobile1010'),
          re_path(r'^export_mobile1011$',export_excel1011,name='export_mobile1011'),
          re_path(r'^export_mobile1012$',export_excel1012,name='export_mobile1012'),
          re_path(r'^export_mobile11$',export_excel11,name='export_mobile11'),
          re_path(r'^export_mobile22$',export_excel22,name='export_mobile22'),
          re_path(r'^export_mobile33$',export_excel33,name='export_mobile33'),
           re_path(r'^export_mobile44$',export_excel44,name='export_mobile44'),
          re_path(r'^export_mobile55$',export_excel55,name='export_mobile55'),
          re_path(r'^export_mobile66$',export_excel66,name='export_mobile66'),
          re_path(r'^export_mobile77$',export_excel77,name='export_mobile77'),
          re_path(r'^export_mobile88$',export_excel88,name='export_mobile88'),
          re_path(r'^export_mobile99$',export_excel99,name='export_mobile99'),
          re_path(r'^export_mobile10$',export_excel10,name='export_mobile10'),
          re_path(r'^export_mobileb$',export_excelb,name='export_mobileb'),
          re_path(r'^export_mobile12$',export_excel12,name='export_mobile12'),


          re_path(r'^export_ouvgli$',export_ouvgli,name='export_ouvgli'),
          re_path(r'^export_achatgli$',export_achatgli,name='export_achatgli'),
          re_path(r'^export_ouvbenm$',export_ouvbenm,name='export_ouvbenm'),
          re_path(r'^export_achatbenm$',export_achatbenm,name='export_achatbenm'),
          re_path(r'^export_ouvzbi$',export_ouvzbi,name='export_ouvzbi'),
          re_path(r'^export_achatzbi$',export_achatzbi,name='export_achatzbi'),
          re_path(r'^export_ouvmer$',export_ouvmer,name='export_ouvmer'),
          re_path(r'^export_achatmer$',export_achatmer,name='export_achatmer'),
          re_path(r'^export_ouvban1$',export_ouvban1,name='export_ouvban1'),
          re_path(r'^export_achatban1$',export_achatban1,name='export_achatban1'),
          re_path(r'^export_ouvban2$',export_ouvban2,name='export_ouvban2'),
          re_path(r'^export_achatban2$',export_achatban2,name='export_achatban2'),
          re_path(r'^export_ouvrais$',export_ouvrais,name='export_ouvrais'),
          re_path(r'^export_achatrais$',export_achatrais,name='export_achatrais'),


          re_path(r'^export_caisse1$',export_caisse1,name='export_caisse1'),
          re_path(r'^export_caisse2$',export_caisse2,name='export_caisse2'),
          re_path(r'^export_caisse3$',export_caisse3,name='export_caisse3'),
          re_path(r'^export_caisse4$',export_caisse4,name='export_caisse4'),
          re_path(r'^export_caisse5$',export_caisse5,name='export_caisse5'),
          re_path(r'^export_caisse6$',export_caisse6,name='export_caisse6'),
          re_path(r'^export_caisse7$',export_caisse7,name='export_caisse7'),
          re_path(r'^export_caisse8$',export_caisse8,name='export_caisse8'),
          re_path(r'^export_caisse9$',export_caisse9,name='export_caisse9'),
          re_path(r'^export_caisse10$',export_caisse10,name='export_caisse10'),
          re_path(r'^export_caisse11$',export_caisse11,name='export_caisse11'),
          re_path(r'^export_caisse12$',export_caisse12,name='export_caisse12'),


          re_path(r'^affiche$',affiche,name='affiche'),


          re_path(r'^engrais$',engrais,name='engrais'),
          re_path(r'^display111$',display111,name='display111'),
          re_path(r'^display222$',display222,name='display222'),
          re_path(r'^display333$',display333,name='display333'),
          re_path(r'^display444$',display444,name='display444'),
          re_path(r'^display555$',display555,name='display555'),
          re_path(r'^display666$',display666,name='display666'),
          re_path(r'^display777$',display777,name='display777'),
          re_path(r'^display888$',display888,name='display888'),
          re_path(r'^display999$',display999,name='display999'),
          re_path(r'^display100$',display100,name='display100'),
          re_path(r'^display101$',display101,name='display101'),
          re_path(r'^display102$',display102,name='display102'),
          re_path(r'^ajouter-employé111$',add_desktop111,name='ajouter-employé111'),
          re_path(r'^ajouter-employé222$',add_laptop111,name='ajouter-employé222'),
          re_path(r'^ajouter-employé333$',add_mobile111,name='ajouter-employé333'),
          re_path(r'^delete_desktop/(?P<pk>\d+)$',delete_desktop,name='delete_desktop'),
          
          re_path(r'^delete_lglidi/(?P<pk>\d+)$',delete_lglidi,name='delete_lglidi'),
          re_path(r'^delete_benmbark/(?P<pk>\d+)$',delete_benmbark,name='delete_benmbark'),
          re_path(r'^delete_raisin/(?P<pk>\d+)$',delete_raisin,name='delete_raisin'),
          re_path(r'^delete_maryem2/(?P<pk>\d+)$',delete_maryem2,name='delete_maryem2'),


          re_path(r'^pesticide$',pesticide,name='pesticide'),
          re_path(r'^display1111$',display1111,name='display1111'),
          re_path(r'^display2222$',display2222,name='display2222'),
          re_path(r'^display3333$',display3333,name='display3333'),
           re_path(r'^display4444$',display4444,name='display4444'),
          re_path(r'^display5555$',display5555,name='display5555'),
          re_path(r'^display6666$',display6666,name='display6666'),
          re_path(r'^display7777$',display7777,name='display7777'),
          re_path(r'^display8888$',display8888,name='display8888'),
          re_path(r'^display9999$',display9999,name='display9999'),
          re_path(r'^display1010$',display1010,name='display1010'),
          re_path(r'^display1011$',display1011,name='display1011'),
          re_path(r'^display1012$',display1012,name='display1012'),
         
          re_path(r'^delete_bananier1/(?P<pk>\d+)$',delete_bananier1,name='delete_bananier1'),
          re_path(r'^delete_bananier2/(?P<pk>\d+)$',delete_bananier2,name='delete_bananier2'),
          re_path(r'^delete_zbirate/(?P<pk>\d+)$',delete_zbirate,name='delete_zbirate'),

          
          
          
]
