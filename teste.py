from datetime import datetime

data_atual = datetime.now()
ptbr = "%d/%m/%Y"

print(data_atual.strftime(ptbr))


data = "2024-06-20 14:03"
en = "%Y-%m-%d %H:%M"

converte = datetime.strptime(data, en)

print(converte)
print(type(converte))


date_string = "2023-05-01" 
date_obj = datetime.strptime(date_string, "%Y-%d-%m") 

print (date_obj)