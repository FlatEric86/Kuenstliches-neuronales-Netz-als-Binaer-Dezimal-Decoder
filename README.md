# Kuenstliches-neuronales-Netz-als-Binaer-Dezimal-Decoder
Ein einfaches einschichtiges neuronales Netz zum Konvertieren von 16 Bit binäre Integer Zahlen in dezimale Zahlen.

Dieses künstliche neuronale Netz ist in der Lage 16 Bit Integer in Dezimalzahlen zu konvertieren.
Interessant ist, dass es lediglich ein Hidden-Layer benötigt um dieses Problem zu lösen.

Mit dem Skript t_data_gen.py können sowohl Trainingsdaten (schon vorliegend als t_data.csv) sowie Validierungsdaten (vorliegend als validation_data.csv) generiert werden.

Das Skript ANN.py wird zum Trainieren des neuronalen Netzes benötigt.

Mit dem Skript model_validation.py kann die Modellgüte in Form der Accuracy bestimmt werden.

Mit dem aktuellen Modellstand (repräsentiert durch die Datei weights.pt) wird ein Accuracy von 0.9981 erreicht.

