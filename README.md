This script will create a set of compressed images from a single raw (read: large) file.

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
