# homepage

Die Website der Freiwilligen Feuerwehr Wenns

## Bearbeiten

Die Homepage lässt sich folgenden Link bearbeiten:

https://github.dev/ffwenns/homepage

Um Änderungen vorzunehmen, muss man sich zuerst auf Github registrieren und dann in die Organisation @ffwenns durch ein bestehendes Mitglied eingeladen werden. Beim Bearbeiten müssen einige Dinge beachtet werden:

- Die **Ordnerstruktur muss auf jeden Fall beibehalten werden**.
- Die ganzen Beiträge sind unter `/posts` in Jahre sortiert und werden automatisch importiert.
- Die Inhalte über die Feuerwehr selber finden sich unter `/content` wieder.
- Die Bilder sollten im **Format webp, 1280 Pixel breit mit Qualität 80** hochgeladen werden.
- Dateinamen bitte ohne Leerzeichen, klein geschrieben.

### Bilder

Um die Bilder umzuwandeln, kann man entweder einen [Online-Konverter](https://www.freeconvert.com/de/webp-converter) oder die [converter.bat](./converter.bat) unter Windows ausführen. Dazu müsst ihr euch zuerst [Imagemagick herunterladen und installieren](https://imagemagick.org/script/download.php#windows).

Anschließend werden durch einen Doppelklick auf die Datei alle Bilder im selben Ordner in das entsprechende Format konvertiert. Die Bilder können dann durch einen Rechtsklick oder per Drag and Drop im Browser hochgeladen werden.

### Shortcodes

Infos dazu folgen noch...

### Veröffentlichen

Möchte man die eigenen Änderungen veröffentlichen, **muss man sie committen**. Dazu wählt man die Änderungen aus und schreibt dann eine kurze Nachricht dazu was man geändert hat. Danach dauert es einen kurzen Moment bis die Seite neu gebaut und veröffentlicht wird.

## Entwicklung

Ich entwickle die Seite unter [Arch Linux](https://archlinux.org) mit [VS Code](https://code.visualstudio.com). Dafür müssen ein paar Sachen installiert werden.

```
sudo pacman -S git git-lfs python python-pip nodejs npm hugo make
```

Danach kann man das Repository wie gewohnt aus checken und per `make install` installieren. Der lokale Server zum Entwickeln lässt sich mit `make serve` starten. Damit kann man die Seite auch im WLAN daheim auf dem Handy testen. Zusätzlich werden Änderungen an den Templates automatisch mit `make watch` aktualisiert.

### Hugo

Infos dazu folgen noch...

### Tailwind CSS

Infos dazu folgen noch...

### Org-mode

Für sämtliche Inhalte werden [org-mode](https://orgmode.org/quickstart.html) Dateien verwendet. Das ist so ähnlich wie Markdown und wird sowohl von Hugo als auch von Github unterstützt. Am besten schaut man sich die Syntax von anderen Dateien im Projekt ab.

### Git Large File Storage (LFS)

Die vielen Bilder (14000+) bei den Beiträgen werden mithilfe von [Git LFS](https://git-lfs.com/) getrackt. Dadurch bleibt das Repository klein und handlich. Die ersten 10 GB sind kostenlos und sollten mehr als ausreichend sein für eine Weile.

### Github Actions

Mit jedem Commit auf dem `main` Branch, wird die Seite neu gebaut. Also bei jeder noch so kleinen Änderung. Außerdem läuft der Importer in regelmäßigen Abständen mehrmals am Tag seine Runden. Sollten Probleme mit den Workflows auftreten, kann man den Status anhand der Badges ganz oben ablesen.

### Importer

Der Importer **schaut sich immer die letzten 5 Posts auf Facebook an** und überprüft ob es sich um einen Beitrag handelt, der einen Titel hat. Es werden **nur Beiträge mit Titel importiert**. Titel werden durch 3 Bindestriche am Anfang und am Ende gekennzeichnet, zB `--- Katze auf Baum ---`. Außerdem werden sämtliche Emojis aus den Beiträgen entfernt.

Um auf Updates von Seiten des ÖA-Team's zu reagieren, werden die aktuellen Beiträge **immer überschrieben**. Wenn ein aktueller Beitrag für die Homepage nachbearbeitet werden soll, empfiehlt es sich daher im Ordner eine `.lock` Datei anzulegen. Dadurch wird verhindert, dass der jeweilige Beitrag überschrieben wird.

Bereits importierte Beiträge müssen ggf. von Hand gelöscht werden. Wenn man sie von Facebook löscht werden sie **nicht automatisch auf der Homepage gelöscht**. Hin und wieder muss man einfach etwas nachhelfen.

Als Beitragsbild wird die erste Datei im Ordner verwendet. Man kann auch selber eines festlegen indem man ein Bild in `cover.webp` umbenennt.

Auch wenn der Importer viel Arbeit abnimmt — er **ist nicht fehlerfrei** und wird laufend verbessert.

### Server

Der Server hat **2 Kerne, 2 GB RAM, eine 60 GB SSD** und ist zusammen mit
der Domain bei [netcup](https://netcup.de) registriert.

Das Betriebssystem ist [Arch Linux](https://archlinux.org),
als Webserver kommt [Caddy](https://caddyserver.com) zum Einsatz.

### Backup

Mein Homeserver pullt das Repository regelmäßig (per Cronjob) und verteilt es mithilfe von [Syncthing](https://syncthing.net) an meinen Desktop und Laptop. Das Repository wird zusätzlich auf den Server gepusht (mirror). Weitere Backups sind auf USB-Sticks und externen Festplatten vorhanden.

Ein ZIP-Archiv sollte regelmäßig an das ÖA-Team verteilt werden. Evtl macht es auch Sinn auf den Google- bzw. Microsoft-Account der Feuerwehr eine Sicherung abzulegen.
