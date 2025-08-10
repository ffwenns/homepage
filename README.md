# homepage

Die Website der Freiwilligen Feuerwehr Wenns

## Bearbeiten

Die Homepage lässt sich über folgenden Link bearbeiten:

https://github.dev/ffwenns/homepage

Um Änderungen vorzunehmen, muss man sich zuerst auf Github registrieren und dann in die Organisation durch ein bestehendes Mitglied eingeladen werden. Beim Bearbeiten müssen einige Dinge beachtet werden:

- Die **Ordnerstruktur muss auf jeden Fall beibehalten werden**.
- Die ganzen Beiträge sind unter `/posts` in Jahre sortiert und werden automatisch importiert.
- Die Inhalte über die Feuerwehr selber finden sich unter `/content` wieder.
- Die Bilder sollten im **Format webp, max. 1280 Pixel breit mit Qualität 80** hochgeladen werden.
- Dateinamen bitte ohne Leerzeichen, klein geschrieben.

### Bilder

Um die Bilder umzuwandeln, kann man entweder einen [Online-Konverter](https://www.freeconvert.com/de/webp-converter) oder die `converter.bat` unter Windows ausführen. Dazu müsst ihr euch zuerst [Imagemagick herunterladen und installieren](https://imagemagick.org/script/download.php#windows).

Anschließend werden durch einen Doppelklick auf die Datei alle Bilder im selben Ordner in das entsprechende Format konvertiert. Die Bilder können dann durch einen Rechtsklick im Browser hochgeladen werden.

### Shortcodes

Infos dazu folgen noch...

### Veröffentlichen

Möchte man die eigenen Änderungen veröffentlichen, **muss man sie committen**. Dazu öffnet man die Source Control Ansicht (<kbd>Strg</kbd> + <kbd>Shift</kbd> + <kbd>E</kbd>), wählt die Änderungen aus und schreibt dann eine kurze Nachricht was man geändert hat. Danach dauert es einen kurzen Moment bis die Seite neu gebaut und veröffentlicht wird.

## Entwicklung

Ich entwickle die Seite unter [Arch Linux](https://archlinux.org) mit [VS Code](https://code.visualstudio.com).

Dafür müssen zunächst ein paar Abhängigkeiten installiert werden.

```
sudo pacman -S git git-lfs nodejs npm make hugo python python-requests
```

Danach kann man das Repository wie gewohnt aus checken.

Der lokale Server zum Entwickeln lässt sich mit `make serve` starten.

Damit kann man die Seite auch im WLAN daheim auf dem Handy testen.

### Hugo

Infos dazu folgen noch...

### Tailwind CSS

Infos dazu folgen noch...

### Org-mode

Für sämtliche Inhalte werden [org-mode](https://orgmode.org/quickstart.html) Dateien verwendet. Das ist so ähnlich wie Markdown und wird sowohl von Hugo als auch von Github unterstützt.

### Git Large File Storage (LFS)

Die vielen Bilder (14000+) werden mithilfe von [Git LFS](https://git-lfs.com/) getrackt. Dadurch bleibt das Repository klein und schnell. Die ersten 10 GB sind kostenlos und sollten mehr als ausreichend sein für eine Weile.

### Github Actions

Mit jedem Commit auf dem ~main~ Branch, wird die Seite neu gebaut. Also bei jeder noch so kleinen Änderung. Außerdem läuft der Importer in regelmäßigen Abständen mehrmals am Tag seine Runden.

### Importer

Der Importer schaut sich immer die letzten 5 Posts auf Facebook an und:

- überprüft ob es sich um einen Beitrag handelt, der einen Titel hat
- es werden nur Beiträge mit Titel importiert, zB `--- Katze auf Baum ---`
- um auf Updates von Seiten des ÖA-Team's zu reagieren, werden die aktuellsten Beiträge immer überschrieben
- wenn ein aktueller Beitrag für die Homepage nachbearbeitet werden will, empfiehlt es sich im Ordner dazu eine `.lock` Datei anzulegen
- dadurch wird verhindert, dass der Beitrag überschrieben wird
- bereits importierte Beiträge müssen ggf. manuell gelöscht werden
- sämtliche Emojis werden aus den Beiträgen entfernt
- als Beitragsbild wird die erste Datei im Ordner verwendet
- alternativ kann auch eines festgelegt werden mit `cover.webp`

### Server

Der Server hat **2 Kerne, 2 GB RAM, eine 60 GB SSD** und ist zusammen mit
der Domain bei [netcup](https://netcup.de) registriert.

Das Betriebssystem ist [Arch Linux](https://archlinux.org),
als Webserver kommt [Caddy](https://caddyserver.com) zum Einsatz.

### Backup

- Mein Homeserver pullt das Repository regelmäßig (per Cronjob) und
- verteilt es mithilfe von [Syncthing](https://syncthing.net) an meinen Computer und Laptop.
- Das Repository wird zusätzlich auf den Server gepusht (mirror).
- Ein Archiv sollte regelmäßig an das ÖA-Team verteilt werden.
