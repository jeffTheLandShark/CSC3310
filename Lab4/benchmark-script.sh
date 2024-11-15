#!/bin/bash
#SBATCH --job-name=benchmarking    
#SBATCH --output=output_%j.txt      
#SBATCH --error=error_%j.txt         
#SBATCH --time=0-01:00                
#SBATCH --partition=teaching        
#SBATCH --gpus=1

# singularity exec --nv -B /data,/home/$USER /data/containers/msoe-tf2x.sif 
python3 benchmark.py