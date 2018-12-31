# Options Portfolio Management

**Structure of project**:-
 - model - This directory contains the ReferenceModel
 - data - This directory contains the ScenarioStructure.dat and the .dat files for each Scenario

**Reference Model**
This file contains the model containing the constants, parameters, variables, constraints and the objective of the optimization problem. I have laid out the layout for solving the options portfolio management problem as a two-stage process.
 - **constants** - I have defined constants like commission for each trade, current option position, reserve coefficient, starting balance, initial margin and the span matrix. For now, I have used some default values which can be changed depending on actual formulation of problem. The span matrix can be obtained using the Black-Scholes formula in a separate program by calling a function(Let's say getSpanMatrix() ).
 - **parameters** - The list of options in our problem as well as its price in each scenario are the parameters. These need to be specified in the .dat files for each scenario as the price will be different for different scenarios
 - **variables** - There are two variables. Two vectors denoting the quantity of options to be bought as well as sold in the next step.
 - **computations** - Total cost for this step, estimated liquidation value as well as the option position after buying/selling are computed.
 - **constraints** - Applied constraints on total cost, margin as well as to prevent margin call.
 - **objective** - The portfolio valuation is to be optimized.

**Scenario Structure**
The structure of the scenario tree is outlined in the ScenarioStructure.dat file. The number of stages, nodes, scenarios as well as the conditional probability of each node arec specified in this file. For now, I have assumed four scenarios with equal probability. This can be changed depending on the number of possible values of the valuation of each option as well as its corresponding probability(According to an appropriate probability distribution). 

**ScenarioName.dat**
For each scenario one such file is required. Since, I have taken four scenarios in the structure I have four files corresponding to each scenario. Each scenario represents different valuations of the options. It contains a list of all options as well as its price in the current scenario. The probability of each scenario has to be mentioned in ScenarioStructure.dat file. For the four scenarios I have assumed the price of each option to be w,x,y and z in the respective scenarios which can be changed.