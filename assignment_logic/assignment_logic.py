# #division of coefficient per class

# ateco_value = codice_ateco_user[0:5]

# if ateco_value == "47.81":
#     coefficiente_redditivita = 0.4
#     gruppo_di_settore = "Commercio  ambulante di prodotti alimentari ebevande"
# elif ateco_value == "47.82" or ateco_value == "47.89":
#     coefficiente_redditivita = 0.54
#     gruppo_di_settore = "Commercio  ambulante di  altri  prodotti"

# #division of coefficient per gruppo

# ateco_value = float(codice_ateco_user[0:4])

# if ateco_value == 46.1:
#     coefficiente_redditivita = 0.62
#     gruppo_di_settore = "Intermediari del commercio"

# elif (ateco_value >= 46.2 and ateco_value <= 46.9) or (ateco_value >= 47.1 and ateco_value <= 47.7) or (ateco_value == 47.9):
#     coefficiente_redditivita = 0.4
#     gruppo_di_settore = "Commercio all’ingrosso e  al  dettaglio"


# # division of coefficient per divisione

# ateco_classe = float(codice_ateco_user[0:2])

# if ateco_classe == 10 or ateco_value == 11:
#     coefficiente_redditivita = 0.4
#     gruppo_di_settore = "Industrie alimentari e delle bevande"
# elif ateco_value == 45:
#     coefficiente_redditivita = 0.4
#     gruppo_di_settore = "Commercio all'ingrosso ee al dettaglio"
# elif (ateco_value >= 41 and ateco_value <= 43) or ateco_value == 68:
#     coefficiente_redditivita = 0.86
#     gruppo_di_settore = "Costruzioni  e  attività immobiliari"
# elif ateco_value == 55 or ateco_value == 56:
#     coefficiente_redditivita = 0.4
#     gruppo_di_settore = "Attività  dei  servizi  di alloggio  e  di  ristorazione"
# elif (ateco_value >= 64 and ateco_value <= 66) or (ateco_value >= 69 and ateco_value <= 75) or (ateco_value == 85) or (ateco_value >= 86 and ateco_value <= 88):
#     coefficiente_redditivita = 0.78
#     gruppo_di_settore = "Attività  professionali, scientifiche,  tecniche, sanitarie,  di  istruzione, servizi  finanziari  e  assicurativi"
# else:
#     coefficiente_redditivita = 0.67
#     gruppo_di_settore = "Altre attività economiche"