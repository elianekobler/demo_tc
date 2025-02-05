#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 11:35:50 2024

This is a script to plot the global TC tracks forecast from ECMWF daily.
Output: .png still image and and .html for the interactive plot

@author: Pui Man (Mannie) Kam
"""

import warnings
warnings.filterwarnings("ignore")

import os
import pandas as pd
import numpy as np

import plotly.graph_objects as go
import matplotlib as mpl
import matplotlib.cm as cm_mp
from matplotlib.colors import BoundaryNorm, ListedColormap

from climada_petals.hazard import TCForecast
from climada.hazard import TCTracks

from tc_tracks_func import filter_storm, _correct_max_sustained_wind_speed
from plot_func import (
    plot_global_tracks, plot_empty_base_map, 
    plot_interactive_map, plot_empty_interactive_map
)

SAVE_FIG_DIR = "/net/n2o/wcr/Sandbox/website/demo_tc/images/{forecast_time}/"

tr_fcast = TCForecast()
tr_fcast.fetch_ecmwf()
tr_filter = filter_storm(tr_fcast)
tr_filter.equal_timestep(3.)
_correct_max_sustained_wind_speed(tr_filter)

# extract datetime information
run_datetime = tr_fcast.data[0].run_datetime
datetime_temp = run_datetime.astype('datetime64[s]').astype(str)
formatted_datetime = datetime_temp.replace('T', '_')[:-6] + 'UTC'

# create directory to store the figure
if not os.path.exists(SAVE_FIG_DIR.format(forecast_time=formatted_datetime)):
    os.makedirs(SAVE_FIG_DIR.format(forecast_time=formatted_datetime))

# plotting the global overview in .png
if len(tr_filter.data)==0:
    axis_png = plot_empty_base_map()
    axis_png.set_title(f"Forecast time: {formatted_datetime}\n"
                   f"Current number of active storms: 0",
                   fontdict={"fontsize": 14})
else:
    tr_unique_storm_id = [tr.sid for tr in tr_filter.data]
    tr_storm_id_list = list(set(tr_unique_storm_id))

    axis_png = plot_global_tracks(tr_filter)
    axis_png.set_title(f"Forecast time: {formatted_datetime}\n"
                   f"Current number of active storms: {str(len(tr_storm_id_list))}",
                   fontdict={"fontsize": 14})

axis_png.figure.savefig(SAVE_FIG_DIR.format(forecast_time=formatted_datetime) +"ECMWF_TC_tracks_" +formatted_datetime +".png")

# plotting the global overview in interactive map
if len(tr_filter.data)==0:
    fig_interactive = plot_empty_interactive_map()
else:
    fig_interactive = plot_interactive_map(tr_filter)

fig_interactive.write_html(SAVE_FIG_DIR.format(forecast_time=formatted_datetime) +"ECMWF_TC_tracks_interactive_map_" +formatted_datetime +".html")