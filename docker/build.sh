#!/bin/sh

cd /data/userguide
if [ $? -ne 0 ] ; then 
	echo "Missing /data/userguide! Please pass in source directory with -v <sourcedir>:/data"
	exit 1
fi

if [ -z "$@" ] ; then
	make html
	exit $?
else
	make $@
	if [ $? -ne 0 ] ; then exit 1; fi
fi
