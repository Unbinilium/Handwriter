## A simple command line tool to generating handwriting-liked text for printing

## Handwriter Features
- **Generate handwriting-liked** text for printing from text file
- **Simulating handwriting** is compatible with Chinese and  almost all languages with Unicode encoded
- **Custom handwriting font** supported and each character's font is randomly generated 
- **Each character size is randomly disturbed** and margin in vertical position is randomly generated 
- **Written in C++** which provides epic performance and Export as HTML by default with standard HTML API

## Test Enviroment
- macOS 10.15 with XCode 11.2 and Safari
- Windows 10 20H1 Professional with Visual Studio Community 2019 and Chrome Version 78

## Usage
Firstly, you have to **download** `handwriter.cpp` or copy its source code to you IDE. If you wonder using the default font presets, just clone Handwriter directly:
```
gitclone https://github.com/Unbinilium/Handwriter.git
```
Secondly, please run `handwriter.cpp` with **arguments configured**, and arguments should follow the template example below:
```
handwriter.cpp <TEXT PATH> <OUT PUT PATH> <FONT(1) PATH> <FONT(2) PATH> ... <FONT(n) PATH>
```
Each argument is split by space ` ` and follow the example sequence, text file in `<TEXT PATH>`could not be empty and `<OUT PUT PATH>` should **contain the file name with file extension** `.html`, fonts path number is limited by `int` size. Be careful the handwriter requires at least 1 font path.

For example we can use 4 custom fonts to simulating handwriting from `/usr/local/example.txt`:
```
handwriter.cpp "/handwriter-master/example.txt" "/handwriter-master/example.html" "/handwriter-master/font/font1.ttf" "/handwriter-master/font/font2.otf" "/handwriter-master/font/font3.woff" "https://fonts.gstatic.com/example.woff2"
```
It simply convert `example.txt` to `example.html` with  handwriting-liked font style, so it's convenient to use different types fonts which only determined by your browser. Also the path formart is flexible, local path or URL are both ok.

For further customization like *HTML Title*, *Font Size* and *Magin Space*, edit the `#define` in `handwriter.cpp`:
```cpp
#define HTML_TITLE         "Handwriter"
#define FONT_SIZE_MIN      21
#define FONT_SIZE_MAX      25
#define FONT_SIZE_PRECISON 0.1
#define MARGIN_MIN         5.0
#define MARGIN_MAX         5.5
#define MARGIN_PRECISION   0.01
```

Lastly double click to **open the generated HTML in your browser** and print it with your printer, fake handwriting got!

## What's more
Currently it only a very simple idea and in a very low level of completion, it actually with a very clumsy algorithm. For whom like your teacher may see through yor trick easily. 

For more reall handwriting generation, more degrees of freedom transform is required, such as horizontal position, vertical position and font size. And the whole of each word should be randomly disturbed including its stroke rotation angle. Also random but not temporarily random, algorithm for pen presure, nit move speed and so on is required. And it better to use mechanical arm to simulating handwriting instead of printer.

I wrote this program just for fun and learn characters encode principle deeper by practicing. Obviously to make this perfect, using C++ and HTML is not a good idea.

## Author & Acknowledge
Handwriter Written by <a href="https://github.com/Unbinilium" target="_blank">Unbinilium</a>. All font presets are from Internet, some Chinese font from  <a href="https://www.hanyi.com.cn/" target="_blank">HanYi</a>.
