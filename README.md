## covidNet by Anirudh Kotamraju and Kailash Ranganathan 
### A Deep Learning Powered Coronavirus Visualization and Prediction Software


**Inspiration**

Coronavirus is undeniably the most major problem of current times, but it seems that quarantine and the effects it is having on the global market and on people’s lives are influencing a new wave of openings, and with it, an even stronger and more potent virus. 

People are not adhering to social distancing as much, and while we understand their perspectives to want to quickly resume their normal lives, we wanted to deliver an objective and informative way to show people that coronavirus is more potent and spreading faster than ever. 

To do this, we built covidNet, a realtime web app that uses up-to-date coronavirus data to display the growth of the virus in all US states and also use deep learning to give predictions and insights into how coronavirus will grow over the next 30 days using recurrent neural networks. This will be able to give a better insight into how coronavirus could grow over standard regression and curve-fitting models in place.  

**What it does**

covidNet delivers a neat and clean UI straight to your device that gives visual data for all 50 US states on total cases and how they have grown since the start of the coronavirus outbreak. But the main attraction is the prediction curves, where we trained individual “recurrent neural network” models for each of the 50 states to analyze how the virus has grown over the past few months and continue the curve to predict the virus’s cases over the next 30 days, a lookahead from today. Quick highlights for predicted (total) cases tomorrow, in 3 days, and in one week are also visible for each of the states. The website is updated daily. 

Each day, a Google Cloud Virtual Machine automatically starts up. It gets the new data for the day, and automatically trains each of the 50 models using the new Johns Hopkins data (not from scratch, but starting from the previous day’s trained models). It then uploads the new models’ predictions for the historical time and the next 30 days into a Github repository as well as the model files for the next day’s training. Whenever a user visits the website (hosted on Heroku), the predictions are taken from this Github repository. Thus, both our models and website are automatically always up to date with the newest trends in each state's fight against the pandemic. 

With this project, we are able to give well organized and accurate predictions using state-of-the-art deep learning methodologies of what the virus could become in each state if further action is not taken. We hope that this will help present the true danger of the uncontrolled virus and encourage preventive action to be taken in the future. 

**How we built it**

We used Dash and Plotly for our frontend, libraries especially relevant for visualizing data science results. With this, we are able to efficiently and effectively integrate our neural network prediction backend with a clean frontend all in Python with some CSS formatting. 

The model updating happens on a Google Cloud Virtual Machine. It is configured with CRON to automatically start up at a certain time and run a startup bash procedure each day. This procedure begins training the models and pushing the csv and model files to our main github repository, where these results are integrated with our frontend. It features a streamlined python script that fetches data from Johns Hopkins, formats it and retrains 50 state models, and saves those to files as well as their historical and 30 day future predictions to a csv.  The models are trained using 2 layer deep LSTM neural networks, with dropout rates of 0.2-0.3 implemented to prevent overfitting. The model files are saved so that on the next day, rather than starting training on the dataset and next day’s data from scratch, the training can load in the preexisting model and continue from there, making the model more accurate as time goes on. 

The website is live and anyone can access it at https://covid-net.herokuapp.com/. Because our training is scheduled, the website and models are automatically updated daily without us having to do anything. 

**Challenges we ran into**

Because LSTM’s are more complicated structurally (and time-dependent as opposed to normal ANNs) than normal feed-forward neural networks, our analysis of coronavirus time series from raw data was quite difficult. We spent a long time devising algorithms to convert the data from raw text (from the Johns Hopkins coronavirus dataset) to properly formatted and normalized tensors to run through our LSTM but were able to generalize this process and train a model given state data just by inputting the state name into our program. With this data our models devised, we were able to quickly create interactive graphs with it to display on our website. 

Furthermore, one of the most important parts is that the whole program updates daily automatically, meaning that we don't have to manually change anything and the models will automatically take data from the dataset, continue training from the previous day's models, and fit to the new data while becoming more accurate. This was extremely hard, as we had to go from a python script that ran one model at a time to one that took data, formatted it, and trained and saved all models in an organized manner. Furthermore, integrating the frontend and backend using Github was also a challenge between configuring the GCP Virtual Machine and Heroku. 

**Accomplishments that we're proud of**

We are proud that we were able to write the neural network, train 50 individual models on 50 individual datasets (one for each state), and deliver it in a functioning and visually pleasing UI in the timeframe of the Hackathon. We were able to functionally link the backend neural network Tensorflow model with the frontend Dash and Plotly web app and in the end, could deliver a useful and easy to use visualization of current coronavirus statistics for all 50 states and our deep learning predictions for future cases starting with the next 30 days. Because daily updates from a virtual machine have zero room for error (or the whole website comes crashing down), our process for automatic updates is robust, reliable, and organized well so that connections between backend and frontend are clear (through GitHub). We are also proud of the completely automated model and data update process, which updates the models using **bash scripts on Google Cloud, then writes them to Github, and the Heroku app accesses those updated data files on Github and presents them to clients on a real time basis. **

**What’s next for covidNet**

Our application and neural network still have some refining to go through, even though it works quite well for all 50 states as a prediction device. We wish to make a bigger, deeper, and more powerful LSTM network to detect more subtleties and insights in the coronavirus data, and also bring in more variables, such as the openings of states, different social distancing orders, and other factors that may affect the spread of the virus. We already expanded on this project by going from only 37 states in a static website initially to a realtime, updated daily website with not only more accurate results but new data and extra training every single day. Perhaps with more computational power and a multivariate system, we will be able to not only predict coronavirus cases, but simulate different paths for the virus using different societal and community parameters, such as level of lockdown, average interaction among crowds, and others. 

We hope you all stay safe and have fun :)
