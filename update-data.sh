#! /bin/bash

pushd "/Hackathon-Secret"

cd "Hackathon-Secret/"

rm -rf "Data/state_data.csv"

python "CovidNetAI.py"

git add .

current_date=$(date +'%m/%d/%Y')
git commit -m "Update predictions. ${current_date}"

git push

popd "/Hackathon-Secret"

