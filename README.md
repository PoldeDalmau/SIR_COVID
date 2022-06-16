# Project 3

Authors: 

Pol de Dalmau Huguet (5414024), Alberto Gori (5391776) and Matteo De Luca (5388783)

How to use the code:

Three notebooks have been made.

-Main.ipynb: 
    
Define initial conditions, parameters (transmission rate beta and recovery rate gamma), time interval and population size, daily vaccines and vaccine effectivity. Then, plots are made of the SIRV model, the effective reproduction number, the newly infected.

-Main_2populations.ipynb: 

Same as the first one but for several populations without vaccine. One must define matrices now for the parameters beta and gamma. The plots made are of the SIR model and actively infected in each population.

-Example_Canada.ipynb:

This notebook first imports the data from a dataframe for Canada found in [this link](https://health-infobase.canada.ca/COVID-19/epidemiological-summary-COVID-19-cases.html). The parameters R_0 and gamma are estimated to make a fit of the SIR model. The population is assumed to be constant. The model is finally compared to the data in several plots. The same analysis can be done for Canada, or only a single province ('Ontario', 'Quebec', 'British Columbia', Alberta', 'Saskatchewan', 'Manitoba') by changing the value of parameter i in the fourth cell. Another parameter that the user can define is the start of the vaccination (t_vaccine).
