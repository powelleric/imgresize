This script will create a set of compressed images from a single raw (read: large) file.

## Example 

Starting directory structure showing a single large (12Mb) image.

```
> tree -hF
.
├── [ 12M]  drwoods-blacksoap-pouring.jpg
```

Directory after running script.  Original image has been moved to `rawpics/` directory and has been replaced with the smallest compressed image.  Additional compressed images are placed in the `sets/` directory.

```
> tree -hF
.
├── [ 24K]  drwoods-blacksoap-pouring.jpg
├── [ 102]  rawpics/
│   └── [ 12M]  drwoods-blacksoap-pouring.jpg
├── [ 136]  sets/
│   ├── [ 76K]  drwoods-blacksoap-pouring-2x.jpg
│   └── [170K]  drwoods-blacksoap-pouring-3x.jpg
```

## Usage

The basic usage of the program is:

```
imgresize.py <img_to_resize>
```

To process all the large files in a given directory, the following set of commands can be used.  This will find all JPEG files larger than 400K. Note, that the `rawpics/` and `sets/` directories must be included from the search.

`find /Library/WebServer/Documents/demo/nature/source/assets/images/AfricanBlackSoap/ -size +400k -name "*jpg" -not -path "*/rawpics/*" -not -path "*/sets/*" -print0 | xargs -0 ~/Dev/p3sandox/imgresize.py`
