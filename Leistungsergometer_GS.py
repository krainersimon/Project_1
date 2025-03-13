performance_test= [] #Liste erstellen und id eingeben
first_experiment_id : int =100
for i in range (10):
  try:
    data ={
        "experiment_id": first_experiment_id + i, #dict erstellen mit allen Daten
        "Versuchsleiter": "Schwarz Gabriel",
        "Datum": "12.03.2025"
    }
    performance_test.append(data) # Daten der Liste hinzufügen
  except:
    print("Eingabe falsch")

print("Leistungstest_Daten:", performance_test)  #ausgabe der daten

First_five = performance_test [0:5]   # Liste mit den ersten 5 Ergebnissen erstellen und ausgeben
print("Die ersten 5 Ergebnisse:" , First_five)

Listcount = 0
for i in range (len(performance_test)): #Listenzähler null setzen, und mit modulu kontrollieren ob sie gerade sind
  if performance_test[i]["experiment_id"]%2 == 0:
    Listcount += 1# dann dem Listenzähler zugeben, wie viele gerade sind und ausgeben
print(Listcount)
