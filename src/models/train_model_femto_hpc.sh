#!/bin/bash
#SBATCH --account=rrg-mechefsk
#SBATCH --gres=gpu:1        # request GPU "generic resource"
#SBATCH --cpus-per-task=4   # maximum CPU cores per GPU request: 6 on Cedar, 16 on Graham.
#SBATCH --mem=12G      # memory per node
#SBATCH --time=0-00:10      # time (DD-HH:MM)
#SBATCH --output=%N-%j.out  # %N for node name, %j for jobID
#SBATCH --mail-type=ALL               # Type of email notification- BEGIN,END,F$
#SBATCH --mail-user=18tcvh@queensu.ca   # Email to which notifications will be $

module load StdEnv/2016.4
module load scipy-stack/2019b
source ~/weibull/bin/activate

python src/models/train_models.py femto