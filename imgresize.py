#!/usr/bin/env python

import argparse, os
from os.path import basename, dirname, exists, splitext
import subprocess
import shutil


SIZES = [
    {"size": "1x", "dimension": 400},
    {"size": "2x", "dimension": 800},
    {"size": "3x", "dimension": 1200}]
SIZECUTOFF = 400000
OUTDIR = "sets/"
RAWDIR = "rawpics/"



def resize2folder(path, size):
    outdir = "outputdir/"
    cmd = ("mogrify -path {outdir} -filter Triangle -define filter:support=2 "
           "-thumbnail {size} -unsharp 0.25x0.08+8.3+0.045 -dither None "
           "-posterize 136 -quality 82 -define jpeg:fancy-upsampling=off "
           "-define png:compression-filter=5 -define png:compression-level=9 "
           "-define png:compression-strategy=1 -define png:exclude-chunk=all "
           "-interlace none -colorspace sRGB {path}").format(
               outdir=outdir, size=size, path=path)
    try:
        subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as err:
        print('ERROR:', err)
    else:
        print("Converted!")

def resize(img, size, output):
    # mogrify command and arguments taken from SmashingMagazine article
    cmd = ("mogrify -write {output} -filter Triangle -define filter:support=2 "
           "-thumbnail {size} -unsharp 0.25x0.08+8.3+0.045 -dither None "
           "-posterize 136 -quality 82 -define jpeg:fancy-upsampling=off "
           "-define png:compression-filter=5 -define png:compression-level=9 "
           "-define png:compression-strategy=1 -define png:exclude-chunk=all "
           "-interlace none -colorspace sRGB {img}").format(
               output=output, size=size, img=img)
    print(cmd)
    try:
        subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as err:
        print('ERROR:', err)
    else:
        print("Converted!")

def batch_resize(image_file):
    imgdir = dirname(image_file)
    outdir, rawdir = init_dirs(imgdir)
    rawimg = archive_raw_img(image_file, rawdir)

    # small image replaces original image
    preset = SIZES[0]
    outname = basename(image_file)
    outpath = os.path.join(imgdir, outname)
    resize(rawimg, preset["dimension"], outpath)

    # medium & large images go to sets/ directory
    for preset in (SIZES[1], SIZES[2]):
        outname = append_size(basename(image_file), preset["size"])
        outpath = os.path.join(outdir, outname)
        resize(rawimg, preset["dimension"], outpath)

    #for preset in SIZES:
        #output_name = append_size(basename(image_file), preset["size"])
        #output_path = dirname(image_file) + "/" + OUTDIR + output_name
        ## TODO - only need to check output path once per image
        #check_output_path(output_path)
        #resize(image_file, preset["dimension"], output_path)

def check_output_path(path):
    outdir = dirname(path)
    if not exists(outdir):
        os.mkdir(outdir)

def archive_raw_img(img, d):
    return shutil.move(img, d)

def init_dirs(rootdir):
    outdir = os.path.join(rootdir, OUTDIR)
    rawdir = os.path.join(rootdir, RAWDIR)
    for d in (outdir, rawdir):
        if not exists(d):
            os.mkdir(d)
    return (outdir, rawdir)

def is_rawsize(img):
    return os.path.getsize(img) >= SIZECUTOFF

def append_size(filepath, size):
    name, ext = splitext(filepath)
    return name + "-" + str(size) + ext

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('image', action='store', help='Image to compress')
    args = parser.parse_args()

    if is_rawsize(args.image):
        print("Resizing image... {}".format(args.image))
        batch_resize(args.image)
    else:
        print(("Image ({}) is already smaller than the size cutoff. "
              "No action will be taken").format(args.image))

    #picdir = "/Users/eric/Dev/p3sandox/"
    #picdir = "/Library/WebServer/Documents/demo/nature/source/assets/images/"
    #rawpic = "african-blacksoap-groupshot.jpg"
    #rawpic = "about-photo.jpg"
    #picpath = picdir + rawpic


#resize(picpath, 400)
#resize(picpath, 800)
#resize(picpath, 1200)
#mtime = os.path.getmtime(picpath)
#print(mtime)
#print(append_name(picpath, "small"))
