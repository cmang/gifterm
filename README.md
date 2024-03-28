![gifterm-demo](https://user-images.githubusercontent.com/261501/143030396-f0f82a21-c1c4-4a84-ac06-9a4407465382.gif)

# Gifterm

This program plays animated GIF files in text terminals, such as a Linux console, OS X Terminal or Windows DOS console. It can also view other image files (jpeg, png, bmp, etc).

## Requirements

Python 3.x

Python modules: Pillow and Colorama (PIL might work if you don't have Pillow)

You can probably install the modules using your OS package manager, or by running:

    easy_install pillow colorama

or:

    pip install pillow colorama

## Usage

To view a file:

    gifterm filename.gif

To view the files in a directory:

    gifterm /path/to/folder

Keyboard commands:

    space - pause/resume
    d - display info On/Off
    n - next file
    p - previous file
    R - random file
    c - next character set 
    C - previous character set 
    s - smoothing On/Off
    i - invert On/Off
    m - monochrome On/Off
    h - high-color (256 color) On/Off
    = or + - increase extra delay
    - - decrease extra delay
    f - fast mode (ignore frame delay)
    b - increase brightness
    B - decrease brightness
    U - toggle Utf-8 Encoding
    r - redraw screen
    ? - show help
    q - quit

    While paused:
    k - next frame
    j - previous frame
    < - first frame
    > - last frame

Command-line arguments:

    usage: gifterm [-h] [-s] [-i] [-A] [-B] [-U] [-H] [-L] [-m] [-c CHARS] [-b BRIGHT]
                   [-o OUTFILE]
                   [filenames [filenames ...]]
     
    positional arguments:
      filenames             image file or files to view, or path to images
     
    optional arguments:
      -h, --help            show this help message and exit
      -s, --smoothing       enable smoothing filter (may slow playback)
      -i, --inverse         invert video
      -A, --ascii           Use IBM-PC extended ASCII block characters (iso-8859-1
                            encoding)
      -B, --block           Use filled block character set
      -U, --utf8            Use Unicode block characters (UTF-8 Encoding)
      -H, --hicolor         Use xterm 256 color mode (Default)
      -L, --locolor         Use 16 color mode
      -m, --mono            Monochrome (no color)
      -c CHARS, --chars CHARS
                            Custom character set, brightest to dimmest.. eg:
                            --chars='Ii; '
      -b BRIGHT, --bright BRIGHT
                            Set brightness level, eg: --bright=5
      -o OUTFILE, --outfile OUTFILE
                            Output to file

## Credits/Licensing

Copyright (c) 2015-2024 Sam Foster. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


