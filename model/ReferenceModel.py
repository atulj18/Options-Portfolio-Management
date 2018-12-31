from pyomo.core import *



# Model

model = AbstractModel()



# Constants

c = 0.01  # Commission for each trade

span_matrix = getSpanMatrix()  # Function to get SPAN Matrix - 16 rows and 4 columns

x = [0, 0, 0, 0]  # Current option position

b = 5  # Reserve coefficient

A = 1000  # Starting balance

M = 100  # Initial Margin



# Parameters

model.OPTIONS = Set()

model.Option_Price = Param(model.OPTIONS, within=PositiveReals)



# Variables

model.x_buy = Var(model.OPTIONS, bounds=(0.0, None))

model.x_sell = Var(model.OPTIONS, bounds=(0.0, None))



# Computations

Cost = 0

Liquidation_value = 0

for i in model.OPTIONS:
    x[i] = x[i] + model.x_buy[i] + model.x_sell[i]
    Cost += model.Option_Price[i] * (model.x_buy[i] - model.x_sell[i]) + c * (model.x_buy[i] + model.x_sell[i])
    Liquidation_value -= model.Option_Price[i] * x[i]



# Constraints

model.BudgetConstraint = Constraint(Cost <= A)

arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(16):
    for j in x:
        arr[i] += span_matrix[i][j] * x[j]


model.MarginConstraints = Constraint(arr[i] <= M for i in range(16))

model.MarginCallConstraint = Constraint((A-Cost) >= (Liquidation_value + b*M))



# Optimization Objective

def Portfolio_Value(model):
    return A-Cost-Liquidation_value

model.Total_Cost_Objective = Objective(rule=Portfolio_Value, sense=maximize)
