# weewx-historygenerator
Copyright 2013-2016  Nick Dajda <nick.dajda@gmail.com>
Copyright 2021-2023 Jonathan Koren <jonathan@jonathankoren.com>

## What is it?
Creates a color coded tables summarizing monthly statistics, 
suitable for displaying historical data.

## Prerequisites
Tested on Weewx release 3.0.1.
Works with all databases.
Observes the units of measure and display formats specified in skin.conf.

WILL NOT WORK with Weewx prior to release 3.0.
  -- Use this version for 2.4 - 2.7:  https://github.com/brewster76/fuzzy-archer/releases/tag/v2.0

## Installation
1) run the installer (from the git directory):

    wee_extension --install .

2) restart weewx:

    sudo /etc/init.d/weewx stop
    sudo /etc/init.d/weewx start

This will install the extension into the weewx/user/ directory.  

# Description
To use it, add this generator to search_list_extensions in skin.conf:

```
[CheetahGenerator]
    search_list_extensions = user.historygenerator.MyXSearch
```

1) The `$alltime` tag:

Allows tags such as $alltime.outTemp.max for the all-time max
temperature, or $seven_day.rain.sum for the total rainfall in the last
seven days.

2) Nice colourful tables summarising history data by month and year:

Adding the section below to your skins.conf file will create these new tags:
   `$min_temp_table`
   `$max_temp_table`
   `$avg_temp_table`
   `$rain_table`
   `$max_aqi_pm2_5_table`

```
############################################################################################
#
# HTML month/year colour coded summary table generator
#
[HistoryReport]
    # minvalues, maxvalues and colours should contain the same number of elements.
    #
    # For example,  the [min_temp] example below, if the minimum temperature measured in
    # a month is between -50 and -10 (degC) then the cell will be shaded in html colour code #0029E5.
    #

    # Default is temperature scale
    minvalues = -50, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35
    maxvalues =  -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 60
    colours =   "#0029E5", "#0186E7", "#02E3EA", "#04EC97", "#05EF3D2, "#2BF207", "#8AF408", "#E9F70A", "#F9A90B", "#FC4D0D", "#FF0F2D"
    monthnames = Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec

    # The Raspberry Pi typically takes 15+ seconds to calculate all the summaries with a few years of weather date.
    # refresh_interval is how often in minutes the tables are calculated.
    refresh_interval = 60

    [[min_temp]]                           # Create a new Cheetah tag which will have a _table suffix: $min_temp_table
        obs_type = outTemp                 # obs_type can be any weewx observation, e.g. outTemp, barometer, wind, ...
        aggregate_type = min               # Any of these: 'sum', 'count', 'avg', 'max', 'min'

    [[max_temp]]
        obs_type = outTemp
        aggregate_type = max

    [[avg_temp]]
        obs_type = outTemp
        aggregate_type = avg

    [[rain]]
        obs_type = rain
        aggregate_type = sum

        # Override default temperature colour scheme with rain specific scale
        minvalues = 0, 25, 50, 75, 100, 150
        maxvalues = 25, 50, 75, 100, 150, 1000
        colours = "#E0F8E0", "#A9F5A9", "#58FA58", "#2EFE2E", "#01DF01", "#01DF01"

    [[max_aqi_pm2_5]]
        data_binding = aqi_binding
        obs_type = aqi_pm2_5
        aggregate_type = max
        aggregate_threshold = 0, count        # https://earlywarning.usgs.gov/usraindry/rdreadme.php
        minvalues =  0,  51, 101, 151, 201, 301
        maxvalues = 50, 100, 150, 200, 300, 500
        colours = "#00e400", "#ffff00", "#ff7e00", "#ff0000", "#8f3f97", "#7e0023"
```