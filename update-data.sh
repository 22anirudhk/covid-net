#! /bin/bash

pushd /home/akotamraju/Hackathon-Secret

rm -rf "Data/state_data.csv"

python "CovidNetAI.py"

ssh -T git@github.com

git remote set-url origin git@github.com:22anirudhk/Hackathon-Secret.git

git add "Data/state_data.csv"
git add "Data/predicted_data.csv"
git add "Models/*"

current_date=$(date +'%c')
git commit -m "Automated Predictions Update. ${current_date}"

git push

popd
