#!/bin/sh

## Set the job name
#PBS -N run_network.py
#PBS -o /home/eherbert/Misc/BorgoreBot/output/
#PBS -e /home/eherbert/Misc/BorgoreBot/error/
#PBS -l nodes=1:ppn=36
#PBS -l walltime=72:00:00
#PBS -M eherbert@trinity.edu
#PBS -m abe

python /home/eherbert/Misc/BorgoreBot/network.py 5
