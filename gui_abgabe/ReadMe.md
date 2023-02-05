
# Bewertete Abgabe GUI
## Abgabe: 6. Februar 2023 (Anfang dritte Prüfungswoche)
## Dominic Moser & Simon Steigmeier

## Aufgabe
Schreibt eine GUI, um die Mandelbrot-Menge darzustellen!
Features (nach Schwierigkeit geordnet)

    - Die Applikation hat ein Fenster mit der Darstellung der Mandelbrotmenge, ein paar Steuerelementen daneben und ein Hauptmenü.
    - Bei Klick auf einen Punkt der Mandelbrotmenge wird mit fixem Faktor gezoomt und das Bild neu aufgebaut (die GUI ist zu der Zeit nicht ansprechbar)
    - Unter den Steuerelementen hat es einen Button "Reset", mit dem der Zoom rückgängig gemacht wird und wieder die Standardansicht angezeigt wird.
    - Unter den Steuerelementen hat es eine Möglichkeit, den Zoomfaktor beim Klicken einzustellen zwischen 1.2 und 4.0 in Schritten von 0.1
    - Jedes Steuerelement hat einen "Tooltip"
    - Das Hauptmenü hat einen Eintrag "File" dem Unterpunkt "Save" mit dem das aktuelle Mandelbrot-Bild als PNG abgespeichert werden kann und einen Unterpunkt "Quit" zum Verlassen des Programms.
    - Wird das Programm geschlossen (Kreuz oben rechts, File->Quit) und das aktuelle Bild wurde nicht gespeichert: Anzeige eines Dialogs ("Wollen Sie wirklich das Programm verlassen?") mit den 3 Optionen Programm verlassen ohne speichern, Zurück ins Programm und Speichern.
    - Das Fenster des Programms kann variabel vergrössert/verkleinert werden. Dabei bleibt der Bereich der Steuerelement in der Grösse fix, der Bereich, der das Fraktal darstellt vergrössert und verkleinert sich; das Fraktal wird nicht jedes Mal neu berechnet, nur das Bild skaliert
    - Die Berechnung wird in einem separaten Thread gemacht, so dass die GUI nicht einfriert.
    - Während der Berechnung wird irgendwo eine Balkenanzeige angezeigt, die den Fortschritt der Berechnung anzeigt.

## Allerlei
- Das `main.py` beinhaltet die GUI-Funktionen
- Die `.ui` Dateien sind für die GUI-Darstellung
- Das `icon.png` ist das Bild, welches im oberen linken Ecken angezeigt wird
- Die Ordner:
  - `autosaved_img`:
    - Hier werden alle berechneten Mandelbrot Bilder gespeichert (jedes Mal, wenn reingezoomt wurde)
  - `img_src`:
    - Hier drin sind alle wichtigen Bilder (Startbild u.s.w :-))
  - `saved_img_by_gui`:
    - Hier drin sind die Bilder, welche explizit via GUI gespeichert wurden, entweder beim Verlassen oder übers Menue
- Im file `calc_sep_class.py` wurde versucht die Berechnung in einer sep. Klasse zu implementieren, dies funktioniert jedoch nicht

## Get Metadata
### `get_metadata_from_saved_png.py`
Während bez. vor der Berechnung des Mandelbrotes werden Metadaten erhoben & gespeichert (from PIL.PngImagePlugin import PngInfo). Eine Ausgabe:
````commandline
path: C:\Users\simi_\Documents\FHGR\VM\Phyton\Semester_5\SW_Entwicklung\Git_ordner_gui\gui_abgabe

folder --> autosaved_img:

filename: mandelbrot_1_zoom_faktor_1.2.png
	timestamp --> 	04. February 2023 21:58:39
	image_counter --> 	1
	counter_gui_saved --> 	1
	calculation time [s] --> 	8.817427158355713
	zoom_faktor --> 	1.2
	Mandelbrot_x_min --> 	-0.0966666666666669
	Mandelbrot_x_max --> 	3.2366666666666664
	Mandelbrot_y_min --> 	-1.9366666666666668
	Mandelbrot_y_max --> 	1.3966666666666667
````
- path:
  - Der Pfad, in welchem die Ordner `autosaved_img` & `saved_images_by_gui` gesucht und, hoffentlich, auch gefunden werden
- folder :
  - Zeigt an, in welchem Ordner die nachfolgenden Bilder gefunden wurde
- filename:
  - Der jeweilige Name von dem gespeicherten Bild
- timestamp:
  - Zeit und Datum wann das Bild gespeichert wurde
- image_counter:
  - Gibt an, wie oft bereits gezoomt wurde, Start @ 1
- counter_gui_saved:
  - Gibt an, wie oft via GUI gespeichert wurde
- calculation time:
  - Zeit, welche für die Berechnung gebraucht wurde
- zoom_faktor:
  - Wie gross der eingestellte Zoom-Faktor war
- Mandelbrot_x_min, Mandelbrot_x_max:
  - Die jeweiligen Koordinaten für die Mandelbrot Berechnung 


## Find the kitten :-)















