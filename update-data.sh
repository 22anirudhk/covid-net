#! /bin/bash

#
# this script should not be run directly,
# instead you need to source it from your .bashrc,
# by adding this line:
#   . ~/bin/update-data.sh
#
function update-data() {
  echo $(SHELL)

  cd "Hackathon-Secret/"

  rm -rf "Data/state_data.csv"

  python "CovidNetAI.py"

  git add .

  current_date=$(date +'%m/%d/%Y')
  git commit -m "Update predictions. ${current_date}"

  git push
}
