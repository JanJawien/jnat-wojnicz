# jnat-wojnicz

## Instrukcja obsługi

Program składa się z trzech plików wykonywalnych: jnat_zipf.py, jnat_connetwork.py oraz jnat_bigrams.py, służących kolejno do analizy prawa zipfa, generowania sieci połączeń oraz zliczania bigramów.
Aby pliki były analizowane poprawnie, plik jnat_bigrams.py musi być uruchomiony po wcześniejszym uruchomieniu pliku jnat_connetwork.py, ze względu na tworzony plik tekstowy z listą słów podzialoną znakami interpunkcyjnymi.
W każdym z plików, na samym początku znajdują się listy znaków, wykrywane jako poprawne w analizowanych tekstach. Można te listy dowolnie zmieniać w celu analizy np. tekstów napisanych w innych językach. W plikach jnat.connetwork.py oraz jnat_bigrams.py znajduje się również lista znaków interpunkcyjnych na podstawie której tekst rozdziela później poprawne zdania. Programy są przystosowane do analizowania dowolnych plików .txt, wystarczy interesujący nas plik wrzucić do folderu inputs oraz zmienić odpowiednio nazwę pliku w kodzie źródłowym.
Podczas analizy zipfa możliwa jest zmiana wyświetlanej statystyki.
Tworzone wykresy zapisywane są do pliku w folderze outputs.
