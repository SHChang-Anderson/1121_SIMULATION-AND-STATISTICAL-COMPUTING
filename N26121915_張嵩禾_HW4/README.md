# 1121_SIMULATION-AND-STATISTICAL-COMPUTING-HW4

This project provides a method for generating Poisson Random Discrete Variables (R.D.V) using the approach described in the textbook section 5.1. Additionally, it includes a file named `Restaurant_Orders_Simulate.py` for simulating daily order quantities. This allows for the simulation of order quantities for different numbers of days.

## Requirements

- Python 3.10.10
- matplotlib 3.7.1

## Usage

### Poisson R.D.V Generator: Method1.py

method1.py allows you to generate Poisson R.D.V with varying mean values. You can adjust the mean by passing different parameters to the `generate_poisson` function. Follow these steps:

1. Run Method1.py
2. Modify the parameters in `generate_poisson` to generate Poisson R.D.V 

### Poisson R.D.V Generator: Method2.py

`PoissonGenerator.py` allows you to generate Poisson R.D.V with varying mean values using the method described in section 5.1 of the textbook. You can adjust the mean by modifying the `lambda_param` variable in the script. Follow these steps:

1. Run `PoissonGenerator.py`.
2. Modify the `lambda_param` variable to set the desired mean for generating Poisson R.D.V.

### Restaurant Orders Simulation: Restaurant_Orders_Simulate.py

`Restaurant_Orders_Simulate.py` is a file for simulating daily order quantities for a restaurant. You can modify this file to simulate order quantities for different numbers of days. This can be used for assessing order patterns over varying time frames. Follow these steps:

1. Run `Restaurant_Orders_Simulate.py`.
2. Adjust the parameters in the script to simulate order quantities for the desired number of days.

