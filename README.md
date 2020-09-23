# Kuenstliches-neuronales-Netz-als-Binaer-Dezimal-Decoder
Ein einfaches einschichtiges neuronales Netz zum Konvertieren von 16 Bit binäre Integer Zahlen in dezimale Zahlen.

Dieses künstliche neuronale Netz ist in der Lage 16 Bit Integer in Dezimalzahlen zu konvertieren.
Natürlich ist ein solcher "Konverter" overkill. Zumal a) die Rechenzeit höher ist als beim konventionellen Algorithmus und b) das Netz nicht mit einer 100%'igen Genauigkeit arbeitet. 

Mit dem Skript t_data_gen.py können sowohl Trainingsdaten (schon vorliegend als t_data.csv) sowie Validierungsdaten (vorliegend als validation_data.csv) generiert werden. Die Trainingsdaten wurden beim Trainieren in die eigentlichen Trainingsdaten und Testdaten gesplittet um Overfitting zu vermeiden bzw. den optimalen Zustand des Netzes zu Evaluieren. Die Validierungsdaten wurden zum Bestimmen der Modellgüte verwendet.
Die Trainingsdaten, Testdaten, sowie Validierungsdaten sind unabhängig voneinander und enthalten jeweils keine Duplikate aus den jeweils anderen Klassen.

Das Skript ANN.py wird zum Trainieren des neuronalen Netzes benötigt.

Mit dem Skript model_validation.py kann die Modellgüte in Form der Accuracy bestimmt werden.

Mit dem aktuellen Modellstand (repräsentiert durch die Datei weights.pt) wird ein Accuracy von 0.9981 erreicht. 

# ...und warum "nur" 0.9981 ???

Es liegen für die Validierung 20000 X-Y-Tupel vor von denen 19962 richtig klassifiziert wurden da:

<img src="https://latex.codecogs.com/gif.latex?0.9981*20000=19962 " /> 

ergo sind 38 X-Y-Tupel falsch klassifiziert wurden. Zwar ist eine Accuracy von 0.9981 etwas, das so ziemlich jeden Machine Learning Engineer vor Freude Purzelbäume schlagen lässt, aber wenn man die arithmetische Einfachheit bei diesem Problem bedenkt, sollten bessere Ergebnisse durchaus drin sein. 
Ein künstlicher Bias durch falsch gelabelte Daten ist immer der erste Gedanke, welcher aber in diesem Fall verworfen werden kann/sollte, da die Daten
automatisiert zusammen mit einem Tool aus einer Python-Standardbibliothek generiert wurden. Es sollte also angenommen werden, dass der Encoder auch fehlerfrei arbeitet, also die Daten korrekt gelabelt sind. 
Ein möglicher Grund könnte in der Verlustfunktion liegen. Es wurde der mittlere quadratische Fehler als Verlustfunktion gewählt. 

```math
SE = \frac{\sigma}{\sqrt{n}}
```


