#!/bin/bash

# add you personal directories
#activate climada environment and run python scripts for impact calculation
source /home/"user"/miniforge3/bin/activate
source activate /home/"user"/miniforge3/envs/climada_env
python /wcr/tc_imp_forecast/TC_imp_forecast/git_repo/TC_impact_forecast_sandbox/plot_tracks_overview_daily.py
echo "All scripts executed successfully."