#!/bin/bash

dir="/Library/WebServer/Documents/demo/nature/source/assets/images/AfricanBlackSoap/"
imglist=$(find $dir -size +400k -name "*jpg" -not -path "*/rawpics/*"  -not -path "*/sets/*")
for img in $imglist;
	#do echo $img
	do ~/Dev/p3sandox/imgresize.py $img
done
