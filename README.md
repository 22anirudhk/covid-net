### covidNet by Anirudh Kotamraju and Kailash Ranganathan - A Deep Learning Powered Coronavirus Visualization and Prediction Software


**Inspiration**

Coronavirus is obviously a major problem in our current times, but it seems that quarantine and the effects it is having on the global market and on people’s lives are influencing a new wave of openings, and with it, an even stronger and more potent virus. People are not adhering to social distancing as much, and while we understand their perspectives to want to quickly resume their normal lives, we wanted to deliver an objective and informative way to show people that coronavirus is more potent and spreading faster than ever. To do this, we built covidNet, a web app that uses a backend neural networks model to not only display data of total cases in over 35 US states but also use deep learning to give predictions and insights into how coronavirus will grow over the next 30 days. This will be able to give a better insight into how coronavirus could grow over standard regression and curve-fitting models in place. 

**What it does**

covidNet delivers a neat and clean UI straight to your home laptop that gives visual data for 37 US states on total cases and how they have grown since the start of the coronavirus outbreak. But the main attraction is the prediction curves, where we trained individual “recurrent neural network” models for each of the 37 states to analyze how the virus has grown over the past few months and continue the curve to predict the virus’s cases over the next 30 days. This will give deep learning-assisted insights into what coronavirus could potentially become in a clean, easy to understand UI. 

**How we built it**

Rather than use standard HTML and Javascript to create a reactive website, we used Dash and Plotly, specially designed for visualizing data science results. With this, we are able to efficiently and effectively integrate our neural network prediction backend with a clean frontend all in Python with some CSS formatting. The backend features a LSTM recurrent neural network written in Tensorflow, with all the data processing (matrix manipulation and normalization algorithms) written by us in Python for our custom project. The network was run entirely on Google Colab’s GPUs and its best results were exported via PANDAS, where they are stored in an internal table as a database for our Heroku web app. The website is live and anyone can access it at predict-19.herokuapp.com 

**Challenges we ran into**

Because LSTM’s are more complicated structurally (and time-dependent as opposed to normal ANNs)than normal feed-forward neural networks, our analysis of coronavirus time series from raw data was quite difficult. We spent a long time devising algorithms to convert the data from raw text to properly formatted and normalized tensors to run through our LSTM. With this data, we were able to quickly create interactive graphs with it to display on our website. 

**Accomplishments that we're proud of**

We are proud that we were able to write the neural network, train 37 individual models on 37 individual datasets (one for each state), and deliver it in a functioning and visually pleasing UI in the timeframe of the Hackathon. We were able to elegantly link the backend neural network Tensorflow model with the frontend Dash and Plotly web app. 

**What’s next for covidNet**

Obviously, our quickly written application and neural network have a lot of refining to go through, even though it works quite well for all 37 states as a prediction device. We wish to make a bigger, deeper, and more powerful LSTM network to detect more subtleties and insights in the coronavirus data, and also bring in more variables, such as the openings of states, different social distancing orders, and other factors that may affect the spread of the virus. With more visuals, we will be able to display more accurate predictions using higher-level deep learning software and help give people an insight into the possibilities of the future of coronavirus. 

We hope you all stay safe and have fun :)
