#!/bin/sh
#$ -N CREST_model_31
#$ -cwd
#$ -l h_rt=24:00:00
#$ -l h_rss=4G
#$ -pe sharedmem 4

. /etc/profile.d/modules.sh
module load anaconda
source activate crest_env

crest model_31.xyz --gfn2 --alpb methanol --parallel 4