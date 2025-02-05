# demo_tc
As part of the Weather and Climate Risks group work at ETH, several sandbox-type websites have been created. This repository documents a simple website designed to display tropical cyclone track forecasts.
A live version of the resulting webpage is hosted at ETH Zurich under the following link: [https://data.iac.ethz.ch/WCR_sandbox/demo_tc/](https://data.iac.ethz.ch/WCR_sandbox/demo_tc/)

Note that while here only hazard data is shown (i.e. TC tracks), the functionality remains unchanged when calculating expected impacts within the [code](./code/)-folder.
Furthermore, in this demonstrator only one figure is shown per selected event. This can easily be extended to show multiple figures for the selected event (e.g. hazard, and estimated impact)

An example for a sandbox-type website with a large number of plots for each event is the Swiss Hail Insights website developed within the [scClim project ](https://scclim.ethz.ch/).
This website is password protected, and access requests can be sent to [Valentin Gebhart](mailto:valentin.gebhart@usys.ethz.ch) or [Timo Schmid](mailto:timo.schmid@usys.ethz.ch)


### Functionality
The basic functionality is a .html webpage ([index.html]((./index.html))) showing a Figure, which is can be changed by selecting different dates.
The functions which change the image files depending on the selected date are stored in [functions.js](./functions.js).
Furthermore, the scripts to generate the TC-track images are in the [code](./code/)-folder.
Lastly the shell script [run_track_forecasts.sh](./run_track_forecast.sh) runs the python scripts, can be automatically run every day (or more frequent) on any linux server with a crontab command (see e.g. [here](https://www.geeksforgeeks.org/crontab-in-linux-with-examples/) for details )


### Contributors
The code for the website is written by Eliane Kobler, and the code for the tropical cyclone download and figure generation are written by Mannie Kam.
