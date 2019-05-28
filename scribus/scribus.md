# Scribus

## scribus-0.png

RIP mrdocs / Peter Linnell

## scribus-1.png

Stable branch (1.4)

- maintainance relase 1.4.8
- avoid bugs in some verions of ghostscript 
- improve the font detection on windows 10

## scribus 

Development branch (1.5svn)

- Refactoring and improvements to the code quality:
  - Require C++11 and refactor the code to use a few C++11 features (nullptr, range for, override).
  - Fix lot of clang and clazy warnings.
  - Avoid big / deep indenting blocks.
- Create nightly Appimages.
- Many improvements to the Python Scripter API, often contributed by the users. (Now that scribs can run scripts from the command line).
- Lot of small fixes.
- Provide free RGB and CMYK ICC profiles that can be used by default.
- A few improvemnts for Complex Script Languages (Arabic, Hebrew, Hindic languages).
- Add a dark theme.
