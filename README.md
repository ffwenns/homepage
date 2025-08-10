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

Infos dazu folgen noch...

### Github Actions

Infos dazu folgen noch...

### Importer

Infos dazu folgen noch...

### Server

Der Server hat **2 Kerne, 2 GB RAM, eine 60 GB SSD** und ist zusammen mit
der Domain bei [netcup](https://netcup.de) registriert.

Das Betriebssystem ist [Arch Linux](https://archlinux.org),
als Webserver kommt [Caddy](https://caddyserver.com) zum Einsatz.
