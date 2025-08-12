# homepage

Die Website der Freiwilligen Feuerwehr Wenns

## Bearbeiten

Um Änderungen an der Seite vorzunehmen, muss man sich zuerst auf Github registrieren und dann in die Organisation durch ein bestehendes Mitglied eingeladen werden. Auf der Homepage findet sich auf jeder Seite ein Bearbeiten-Link (ganz unten). Damit kommt man dann bequem zur Seite die man ändern will.

Beim Bearbeiten müssen einige Dinge beachtet werden:

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

Ich entwickle die Seite unter [Arch Linux](https://archlinux.org) mit [VS Code](https://code.visualstudio.com). Dafür müssen ein paar Sachen installiert werden. Wenn ihr unter Windows 11 unterwegs seid, macht es Sinn das [unter WSL zu installieren](https://wiki.archlinux.org/title/Install_Arch_Linux_on_WSL).

```
sudo pacman -S git git-lfs python python-pip nodejs npm hugo make
```

Danach kann man das Repository wie gewohnt aus checken und per `make install` installieren. Der lokale Server zum Entwickeln lässt sich mit `make serve` starten. Damit kann man die Seite auch im WLAN daheim auf dem Handy testen. Zusätzlich werden Änderungen an den Templates automatisch mit `make watch` aktualisiert.

Noch ein paar Worte zur technischen Umsetzung:

- **Hugo**: [Hugo](https://gohugo.io) ist ein statischer Seitengenerator. Die Homepage wird somit aus mehreren Dokumenten und Bildern zusammengebaut bevor sie dann auf einen Server hochgeladen wird. Das hat mehrere Vorteile:
  - **Sicherheit**: Auf dem Server rennt keine Datenbank, kein System das regelmäßig Updates braucht. Der Server selbst ist eigentlich _dumm_ und muss nur das _fixundfertige_ HTML ausliefern.
  - **Geschwindigkeit**: Die Seiten werden sehr schnell zusammengebaut und geladen.
  - **Einfachheit**: Es ist sehr wenig Code im Spiel. Die Homepage setzt sich aus einigen Ordnern, Dokumenten und Bildern zusammen und wird bereits vorher "zusammengebaut".
  - **Transparenz**: Die Vorgänge sind für jeden transparent und nachvollziehbar.
- **Tailwind CSS**: Für das Frontend habe ich [Tailwind CSS](https://tailwindcss.com) verwendet. Damit kann man schnell und einfach moderne Layouts umsetzen ohne sich viel Kopf machen zu müssen.
- **Org-mode**: Für sämtliche Inhalte werden [org-mode](https://orgmode.org/quickstart.html) Dateien verwendet. Das ist so ähnlich wie Markdown und wird sowohl von Hugo als auch von Github unterstützt. Am besten schaut man sich die Syntax von anderen Dateien im Projekt ab.
- **Git Large File Storage (LFS)**: Die vielen Bilder (14000+) werden mithilfe von [Git LFS](https://git-lfs.com/) getrackt. Dadurch bleibt das Repository klein und handlich. Die ersten 10 GB sind kostenlos und sollten mehr als ausreichend sein für eine Weile.
- **Github Actions**: Mit jedem Commit auf dem `main` Branch, wird die Seite neu gebaut. Also bei jeder noch so kleinen Änderung. Außerdem läuft der Importer in regelmäßigen Abständen mehrmals am Tag seine Runden. Sollten Probleme mit den Workflows auftreten, kann man den Status anhand der Badges oben ablesen.

### Importer

Der Importer **schaut sich immer die letzten 5 Posts auf Facebook an** und überprüft ob es sich um einen Beitrag handelt, der einen Titel hat. Es werden **nur Beiträge mit Titel importiert**. Titel werden durch 3 Bindestriche am Anfang und am Ende gekennzeichnet, zB `--- Katze auf Baum ---`. Außerdem werden sämtliche Emojis aus den Beiträgen entfernt.

Um auf Updates von Seiten des ÖA-Team's zu reagieren, werden die aktuellen Beiträge **immer überschrieben**. Wenn ein aktueller Beitrag für die Homepage nachbearbeitet werden soll, empfiehlt es sich daher im Ordner eine `.lock` Datei anzulegen. Dadurch wird verhindert, dass der jeweilige Beitrag überschrieben wird.

Bereits importierte Beiträge müssen ggf. von Hand gelöscht werden. Wenn man sie von Facebook löscht werden sie **nicht automatisch auf der Homepage gelöscht**. Hin und wieder muss man einfach etwas nachhelfen.

Als Beitragsbild wird die erste Datei im Ordner verwendet. Man kann auch selber eines festlegen indem man ein Bild in `cover.webp` umbenennt.

Auch wenn der Importer viel Arbeit abnimmt — er **ist nicht fehlerfrei** und wird laufend verbessert.

### Server

Der Server hat **2 Kerne, 2 GB RAM** und eine 60 GB SSD

Das Betriebssystem ist [Arch Linux](https://archlinux.org),
als Webserver kommt [Caddy](https://caddyserver.com) zum Einsatz.

Der Server und die Domain sind bei [netcup](https://netcup.de) registriert.

### Backup

Mein Homeserver pullt das Repository regelmäßig (per Cronjob) und verteilt es mithilfe von [Syncthing](https://syncthing.net). Das Repository wird zusätzlich auf den Server gepusht (mirror). 
Ein ZIP-Archiv sollte regelmäßig an das ÖA-Team verteilt werden. Evtl macht es auch Sinn auf den Google- bzw. Microsoft-Account der Feuerwehr eine Sicherung abzulegen.
