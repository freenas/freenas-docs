#!/bin/sh

IMAGEDIR="images"
RSTFILES="*.rst snippets/*.rst"

TMPDIR="/tmp"

TMPIMG="${TMPDIR}/images.$$"
ls ${IMAGEDIR}/* > ${TMPIMG}

TMPUSED="${TMPDIR}/usedimages.$$"
perl -ne 'print $1, "\n" if /(images\/.*(?:png|jpg))/i' ${RSTFILES} | sort -u > ${TMPUSED}

printf "in .rst only\t\t\tin imagesdir only\t\tin both\n"
printf "(missing image)\t\t\t(possibly obsolete)\t\t(probably okay)\n"
printf "______________________________\t______________________________\t______________________________\n"
comm ${TMPUSED} ${TMPIMG} | perl -pe 's/\t/\t\t\t\t/g;'
