# Kuenstliches-neuronales-Netz-als-Binaer-Dezimal-Decoder
Ein einfaches einschichtiges neuronales Netz zum Konvertieren von 16 Bit binäre Integer Zahlen in dezimale Zahlen.

Dieses künstliche neuronale Netz ist in der Lage 16 Bit Integer in Dezimalzahlen zu konvertieren.
Natürlich ist ein solcher "Konverter" overkill. 

Mit dem Skript t_data_gen.py können sowohl Trainingsdaten (schon vorliegend als t_data.csv) sowie Validierungsdaten (vorliegend als validation_data.csv) generiert werden. Die Trainingsdaten wurden beim Trainieren in die eigentlichen Trainingsdaten und Testdaten gesplittet um Overfitting zu vermeiden bzw. den optimalen Zustand des Netzes zu Evaluieren. Die Validierungsdaten wurden zum Bestimmen der Modellgüte verwendet.
Die Trainingsdaten, Testdaten, sowie Validierungsdaten sind unabhängig voneinander und enthalten jeweils keine Duplikate aus den jeweils anderen Klassen.
Grundsätzlich handelt es sich bei diesem Modell um eine Regression da von einem Wert aus dem binären Zahlenraum in den Raum der natürlichen Zahlen abgebildet wird. Um die Güte eines Modells durch eine geeignete Metrik abzubilden, bedient man sich bei Regressionen gerne dem Korrelationskoeffizienten oder der Kovarianz, wohingegen bei Klassifizierungsproblemen etwa die Accuracy verwendet wird. Interessanter weise lässt sich trotzdem diesen Modell hier eine Regression ist, die Accuracy als mögliche Metrik verwenden. Denn der Funktionswert des Modells wird durch Rundung in einen etweder exakten oder falschen Wert transformiert. Um nun also die Güte des Modells zu validieren, interessiert nicht mehr, wie weit sich Validierungswert und Modellwert unterscheiden, sondern ob sie gleich sind oder eben nicht. Insofern kann die Accuracy durchaus als Metrik verwendet werden. Sie beschreibt also in wievielen Fällen das Neuronale Netz den exakten Dezimalwert aus dem Binärwert errechnet hat.

Das Skript ANN.py wird zum Trainieren des neuronalen Netzes benötigt.

Mit dem Skript model_validation.py kann die Modellgüte in Form der Accuracy bestimmt werden.

Das Modell hat eine Accuracy von 1.0 welche sich durch 20000 modellunabhängigen Validierungsdaten, welche ergo alle richtig berechnet wurden, ergibt.








