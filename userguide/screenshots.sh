#!/bin/sh

# this program produces a list of all images in IMAGEDIR,
# a list of images that are probably manually created,
# and a script to copy automated screenshots back into
# IMAGEDIR.

IMAGEDIR="images"
TMPDIR="/tmp"
IMAGELIST="${TMPDIR}/userguide-imagelist.txt"
IMAGESCRIPT="${TMPDIR}/imagecopy.sh"
MANUALIMAGES="${TMPDIR}/manual-imagelist.txt"

IMAGES=$( ls ${IMAGEDIR}/*.png )

echo ${IMAGES} > ${IMAGELIST}
echo "list of all User Guide images: ${IMAGELIST}"

echo "SRCDIR=\"changeme\"" > ${IMAGESCRIPT}
echo "DESTDIR=\"changemetoo\"" >> ${IMAGESCRIPT}
for image in ${IMAGES}; do
  name=$( basename $image )
  echo "scp \${SRCDIR}/$name \${DESTDIR}/$name" >> ${IMAGESCRIPT}
done
echo "image copy script: ${IMAGESCRIPT}"

echo "Oddly-sized, probably manually-created images" > ${MANUALIMAGES}
echo > ${MANUALIMAGES}
for image in ${IMAGES}; do
  wxh=$( identify $image | cut -w -f3 )
  height=$( echo $wxh | cut -dx -f2 )
  if [ $height -lt 1049 ];then
    echo "manual image: $image $wxh" >> ${MANUALIMAGES}
  fi
done
echo "manual images list: ${MANUALIMAGES}"
