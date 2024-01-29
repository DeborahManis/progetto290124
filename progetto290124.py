#importo le librerie che mi serviranno
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importo il file csv
data=pd.read_csv (r'C:\Users\Debor\Downloads\C_17_dataset_114_0_upFile.csv',sep = ';' , encoding='iso-8859-15', header =0 )
print(data.head(5)) #stampo per vedere se funziona

#seleziono le colonne che mi servono per rispondere alla domanda: quanti posti letto per regione?
Colonne = ['Descrizione Regione' , 'Totale posti letto' ]
dataColonne = data[Colonne]
print(dataColonne.head(5)) # stampo per vedere se funziona

# raggruppo e sommo
sommaPosti = dataColonne.groupby('Descrizione Regione')['Totale posti letto'].sum().reset_index()
print(sommaPosti)

#calcoliamo la regione che ha piu posti letto ( max) e i meno posti letto
sommaPosti1 = data.groupby("Descrizione Regione")["Totale posti letto"].sum().sort_values(ascending=True)
max = sommaPosti1[-1:]   #seleziono l'ultima riga per ottenere il massimo
min = sommaPosti1[0:1]   #seleziono la prima per ottenere il minimo
print("minimo", min)
print("massimo",max)


# Grafico
x = sommaPosti['Descrizione Regione']
y = sommaPosti['Totale posti letto']
plt.figure(figsize=(6,4))
plt.barh(x, y)
plt.title('Tot Posti letto per regione')
plt.xlabel('Posti letto')
plt.ylabel('Regione')
plt.show()

#calcolo il tot posti letto per tipo di struttura e per regioni
posti_per_tipo_struttura = data.groupby(["Descrizione Regione" , "Descrizione tipo struttura"]) ["Totale posti letto"].sum()
print(posti_per_tipo_struttura)

# #calcolo la media per tipo di struttura e per regioni
media_tipo_struttura = data.groupby(["Descrizione tipo struttura", "Descrizione Regione"]) ["Totale posti letto"].mean().reset_index()
print(media_tipo_struttura)

#somma posti letto per disciplina
SommaPostiDisciplina = data.groupby(['Tipo di Disciplina'])['Totale posti letto'].sum().reset_index()
print(SommaPostiDisciplina)

# per trovare il numero dei posti letto suddivisi per regione e per tipo di disciplina:
posti_letto = data.loc[:,["Descrizione Regione","Tipo di Disciplina","Totale posti letto"]]
tabella_tipo_disciplina_regioni=posti_letto.groupby(["Descrizione Regione","Tipo di Disciplina"]).sum("Totale posti letto").reset_index()
print(tabella_tipo_disciplina_regioni)

# Per trovare le discipline che hanno il numero più alto di posti letto in ogni regione:
regione_max=posti_letto.groupby(["Descrizione Regione","Tipo di Disciplina"]).sum().sort_values(by="Totale posti letto",ascending=False).reset_index()
print(regione_max.head())

# Per trovare le discipline che hanno il numero più basso di posti letto in ogni regione:
print(regione_max.tail())