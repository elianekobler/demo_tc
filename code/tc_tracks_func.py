#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 11:35:50 2024

Useful functions for extracting TC tracks from ECMWF.

@author: Pui Man (Mannie) Kam
"""
from climada_petals.hazard import TCForecast
from climada.hazard import TCTracks

WIND_CONVERSION_FACTOR = 1. / 0.88

# Function to categorize wind speed
def categorize_wind(speed):
    if speed < 17.49:
        return -1  # Tropical depression
    elif speed < 32.92:
        return 0  # Tropical storm
    elif speed < 42.7:
        return 1  # Category 1
    elif speed < 49.39:
        return 2  # Category 2
    elif speed < 58.13:
        return 3  # Category 3
    elif speed < 70.48:
        return 4  # Category 4
    elif speed < 1000:
        return 5  # Category 5
    else:
        return 999

def filter_storm(fcast: TCForecast):
    """
    

    Parameters
    ----------
    fcast : climada.TCForecast
        The set of forecast data from ECMWF

    Returns
    -------
    fcast_filter : climada.TCForecast
        TCForecast class with storms which are named storm

    """
    tr_name_list = [tr.name for tr in fcast.data]
    tr_name_list = list(set(tr_name_list))
    
    fcast_filter = TCTracks()

    for tr_name in tr_name_list:

        if tr_name[:2].isdigit():
            continue
        
        else:
            fcast_filter.append(fcast.subset({
                'name': tr_name,
                'is_ensemble': True
            }).data)
    
    
    return fcast_filter

def _correct_max_sustained_wind_speed(tc_forecast: TCForecast,
                                      wind_conversion_factor: float = WIND_CONVERSION_FACTOR) -> None:
    """
    Converts the maximum sustained wind speed by a given factor. The sustained wind speed is defined as the wind speed
    which has not been underrun by any measurement within a given time interval.
    Note that the operation of multiplying by a constant factor is simplifying reality and a more complex method
    should be used eventually
    :param tc_forecast: The tracks object to which the modification is applied
    :param wind_conversion_factor: The factor by which the maximum sustained wind will be modified
    :return:
    """
    for dataset in tc_forecast.data:
        dataset['max_sustained_wind'] *= wind_conversion_factor