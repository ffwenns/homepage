# homepage

Die Website der Freiwilligen Feuerwehr Wenns

[![Build](https://github.com/ffwenns/homepage/actions/workflows/build.yml/badge.svg)](https://github.com/ffwenns/homepage/actions/workflows/build.yml)

## Bearbeiten

Beim Bearbeiten bitte einige Dinge beachten:

- die **Ordnerstruktur muss beibehalten werden**
- die ganzen Beiträge sind unter `/posts` in Jahre sortiert und werden automatisch importiert
- die Inhalte über die Feuerwehr selber finden sich unter `/content` wieder
- Mitglieder in den Ordner `/static/images/mitglieder` hochladen
- Bilder im **Format webp, 1280 Pixel breit mit Qualität 80** hochladen
- Dateinamen ohne Leerzeichen, klein geschrieben

## Entwicklung

Es müssen folgende Abhängigkeiten unter [Arch Linux](https://archlinux.org) installiert sein:

```
sudo pacman -S git git-lfs python python-pip nodejs npm hugo make
```

### Server

- [VPS nano G11s](https://www.netcup.com/de/server/vps/vps-nano-g11s-6m)
- 2 vCore (x86)
- 2 GB RAM
- 60 GB SSD
