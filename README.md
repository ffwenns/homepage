# homepage

Die Website der Freiwilligen Feuerwehr Wenns

[![Build](https://github.com/ffwenns/homepage/actions/workflows/build.yml/badge.svg)](https://github.com/ffwenns/homepage/actions/workflows/build.yml)

## Bearbeiten

Um Änderungen an der Seite vorzunehmen, muss man sich zuerst **auf Github registrieren** und dann in die Organisation durch ein bestehendes Mitglied eingeladen werden. Auf der Homepage findet sich auf jeder Seite **ein Link zum Bearbeiten** (ganz unten).

Beim Bearbeiten bitte einige Dinge beachten:

- Die **Ordnerstruktur muss beibehalten werden**.
- Die ganzen Beiträge sind unter `/posts` in Jahre sortiert und werden automatisch importiert.
- Die Inhalte über die Feuerwehr selber finden sich unter `/content` wieder.
- Die Bilder im **Format webp, 1280 Pixel breit mit Qualität 80** hochladen werden.
- Dateinamen ohne Leerzeichen, klein geschrieben.

### Bilder

Um die Bilder umzuwandeln, kann man entweder einen [Online-Konverter](https://www.freeconvert.com/de/webp-converter) verwenden oder die [converter.bat](./scripts/converter.bat) unter Windows ausführen. Dazu müsst ihr euch zuerst [Imagemagick herunterladen und installieren](https://imagemagick.org/script/download.php#windows). Anschließend werden durch einen Doppelklick auf die Datei alle Bilder im selben Ordner in das entsprechende Format konvertiert.

### Shortcodes

Infos dazu folgen noch...

## Entwicklung

Ich entwickle die Seite unter [Arch Linux](https://archlinux.org) mit [VS Code](https://code.visualstudio.com). Wenn ihr unter Windows 11 unterwegs seid, macht es Sinn das [unter WSL zu machen](https://wiki.archlinux.org/title/Install_Arch_Linux_on_WSL).

```
sudo pacman -S git git-lfs python python-pip nodejs npm hugo make
```

Danach kann man das Repository wie gewohnt aus checken und per `make install` installieren.

Der lokale Server zum Entwickeln lässt sich mit `make serve` starten. Damit kann man die Seite auch im WLAN daheim auf dem Handy testen. Zusätzlich werden Änderungen am Design automatisch mit `make watch` aktualisiert.

Noch ein paar Worte zur technischen Umsetzung:

- **Hugo**: [Hugo](https://gohugo.io) ist ein statischer Seitengenerator. Die Homepage wird somit aus mehreren Dokumenten und Bildern zusammengebaut bevor sie dann auf einen Server hochgeladen wird.
- **Org-mode**: Für die Inhalte werden [org-mode](https://orgmode.org/quickstart.html) Dateien verwendet. Das ist so ähnlich wie Markdown und wird sowohl von Hugo als auch von Github unterstützt.
- **Tailwind CSS**: Für das Frontend habe ich [Tailwind CSS](https://tailwindcss.com) verwendet. Damit kann man schnell und einfach moderne Layouts umsetzen ohne sich viel Kopf machen zu müssen.
- **Git Large File Storage (LFS)**: Die vielen Bilder (14000+) werden mithilfe von [Git LFS](https://git-lfs.com/) getrackt.
- **Github Actions**: Mit jeder Änderung wird die Homepage automatisch neu gebaut.

### Importer

Der Importer **schaut sich immer die aktuellen Posts auf Facebook an** und überprüft ob es sich um einen Beitrag handelt, der einen Titel hat. Es werden **nur Beiträge mit Titel importiert**. Titel werden durch 3 Bindestriche gekennzeichnet, zB `--- Katze auf Baum ---`.

Um auf Updates von Seiten des ÖA-Team's zu reagieren, werden die aktuellen Beiträge **immer überschrieben**. Wenn man einen aktuellen Beitrag auf der Homepage bearbeiten will, sollte man ihn daher mit `#+LOCK: t` sperren. Das Beitragsbild wird automatisch festgelegt und entspricht dem ersten Bild im Ordner. Man kann aber auch selbst einen festlegen, indem man ein Bild in `cover.webp` umbenennt.

Bereits importierte Beiträge müssen ggf. von Hand gelöscht werden. Wenn man sie von Facebook löscht werden sie **nicht automatisch auf der Homepage gelöscht**. Hin und wieder muss man einfach etwas nachhelfen.

### Server

- [VPS nano G11s](https://www.netcup.com/de/server/vps/vps-nano-g11s-6m)
- 2 vCore (x86)
- 2 GB RAM
- 60 GB SSD
