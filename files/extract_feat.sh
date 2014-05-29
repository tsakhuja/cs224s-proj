#!/bin/bash

# Class: CS224S
# Assignment: HW4
# Author: Frank Liu
#
# Extracts a series of audio features for emotion detection using the openSMILE
# library.
#
# CS224S students - YOU SHOULD NOT MODIFY THIS FILE!

# add some essential path and file names
configfile='cs224s.conf'

# dataset folder
case $1 in
0 ) dataset='train';;
1 ) dataset='test';;
* ) echo "Unknown dataset number" && exit 1;
esac
datapath=data/$dataset

echo 'Acquiring audio features for dataset' $dataset

# check the OS version - students who want to run separately on their personal
# machines need this line of code (can technically run 32-bit version on any
# machine, but 64-bit version will improve runtime for large datasets)
os=$(uname -m)
if [ $os == "x86_64" ] 
then
  echo 'Running 64-bit feature extractor'
  execname='SMILExtract'
else
  echo 'Running 32-bit feature extractor'
  execname='SMILExtract_standalone_32bit_generic'
fi

# extract the features!
# can technically use 'find', but split into 5 loops to make things clear
rm feats/$dataset.lsvm
for fname in $datapath/BRK/* # anger
do
  echo 'Extracting features for' $fname
  openSMILE/$execname -C config/$configfile -I $fname -O feats/$dataset.lsvm -noconsoleoutput
done
for fname in $datapath/BRM/* # despair
do
  echo 'Extracting features for' $fname
  openSMILE/$execname -C config/$configfile -I $fname -O feats/$dataset.lsvm -noconsoleoutput
done
for fname in $datapath/GRW/* # happiness
do
  echo 'Extracting features for' $fname
  openSMILE/$execname -C config/$configfile -I $fname -O feats/$dataset.lsvm -noconsoleoutput
done
for fname in $datapath/LRM/* # neutral
do
  echo 'Extracting features for' $fname
  openSMILE/$execname -C config/$configfile -I $fname -O feats/$dataset.lsvm -noconsoleoutput
done
for fname in $datapath/LRR/* # sadness
do
  echo 'Extracting features for' $fname
  openSMILE/$execname -C config/$configfile -I $fname -O feats/$dataset.lsvm -noconsoleoutput
done
for fname in $datapath/MCR/* # sadness
do
  echo 'Extracting features for' $fname
  openSMILE/$execname -C config/$configfile -I $fname -O feats/$dataset.lsvm -noconsoleoutput
done
for fname in $datapath/ROR/* # sadness
do
  echo 'Extracting features for' $fname
  openSMILE/$execname -C config/$configfile -I $fname -O feats/$dataset.lsvm -noconsoleoutput
done
for fname in $datapath/RRM/* # sadness
do
  echo 'Extracting features for' $fname
  openSMILE/$execname -C config/$configfile -I $fname -O feats/$dataset.lsvm -noconsoleoutput
done
for fname in $datapath/RUM/* # sadness
do
  echo 'Extracting features for' $fname
  openSMILE/$execname -C config/$configfile -I $fname -O feats/$dataset.lsvm -noconsoleoutput
done
for fname in $datapath/SQK/* # sadness
do
  echo 'Extracting features for' $fname
  openSMILE/$execname -C config/$configfile -I $fname -O feats/$dataset.lsvm -noconsoleoutput
done
for fname in $datapath/SQL/* # sadness
do
  echo 'Extracting features for' $fname
  openSMILE/$execname -C config/$configfile -I $fname -O feats/$dataset.lsvm -noconsoleoutput
done
for fname in $datapath/TMP/* # sadness
do
  echo 'Extracting features for' $fname
  openSMILE/$execname -C config/$configfile -I $fname -O feats/$dataset.lsvm -noconsoleoutput
done

# remove the log file at the end (don't need it for CS224S)
rm smile.log
