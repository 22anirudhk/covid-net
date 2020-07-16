rm -rf Data/time_series_covid19_confirmed_US.csv
rm -rf Data/state_data.csv

wget https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv

#python CovidNetAI.py

git add .
git commit -m "Update predictions."
git push


