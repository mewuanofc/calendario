import datetime

import locale
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

diaatual = datetime.datetime.now()

dia = diaatual.day
mes = diaatual.month
ano = diaatual.year
dia_semanal = diaatual.strftime('%A')

print(f"O dia é {dia}, mês é {mes}, o ano é {ano} e o dia semanal é {dia_semanal}.")