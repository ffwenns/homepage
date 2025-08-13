@echo off
setlocal enabledelayedexpansion

REM Set the maximum width and quality for the WebP conversion
set "MAX_WIDTH=1280"
set "QUALITY=80"

REM Check if ImageMagick is installed and available
where magick >nul 2>&1
if errorlevel 1 (
    echo ImageMagick is not installed or not in your PATH. Please install it from https://imagemagick.org/script/download.php#windows
    pause
    exit /b 1
)

REM Get all image files in the current directory
for %%f in (*.jpg *.jpeg *.png *.bmp *.tiff) do (
    set "FILE_NAME=%%~nf"
    set "OUTPUT_FILE=%%~dpnf.webp"

    REM Check if WebP file already exists
    if not exist "%%~dpnf.webp" (
        REM Get the original image width
        for /f %%w in ('magick identify -format "%%w" "%%f"') do set "WIDTH=%%w"

        REM Determine if resizing is needed
        if !WIDTH! gtr !MAX_WIDTH! (
            echo Converting "%%f" to WebP with resizing...
            magick "%%f" -resize !MAX_WIDTH!x -quality !QUALITY! "!OUTPUT_FILE!"
        ) else (
            echo Converting "%%f" to WebP without resizing...
            magick "%%f" -quality !QUALITY! "!OUTPUT_FILE!"
        )
    ) else (
        echo Skipping "%%f" as "%%~nf.webp" already exists.
    )
)

echo Conversion complete!
pause
