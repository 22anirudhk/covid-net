#! /bin/bash

pushd /home/akotamraju/Hackathon-Secret

rm -rf "Data/state_data.csv"

python "CovidNetAI.py"

ssh -T git@github.com

git remote set-url origin git@github.com:22anirudhk/Hackathon-Secret.git

git add .

current_date=$(date +'%c')
git commit -m "Update predictions. ${current_date}"

git push

popd
