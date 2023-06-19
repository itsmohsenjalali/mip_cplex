# Fixed-Charge Network Flow Problem Solver
This project implements a solver for the Fixed-Charge Network Flow Problem (FCNFP) using the IBM CPLEX optimization library in Python. The FCNFP is a mixed integer programming problem that involves finding the optimal flow of commodities through a network while considering fixed charges associated with the arcs. The goal is to minimize the total cost, which includes both flow-related costs and fixed charges.

## Problem Formulation
The FCNFP can be mathematically formulated as follows:

### Minimize:
```
∑(i,j in A) C_ij * X_ij + ∑(i,j in A) F_ij * Y_ij
```
### Subject to:
```
∑(j in Q^+_i) X_ij - ∑(j in Q^-_i) X_ji = B_i   for all i in N
0 <= X_ij <= U_ij * Y_ij                       for all i,j in A
Y_ij ∈ {0,1}                                   for all i,j in A
```

Where:

- A represents the set of arcs in the network.
- C_ij denotes the flow-related cost for each arc (i, j).
- F_ij represents the fixed charge for each arc (i, j).
- Q^+_i and Q^-_i represent the set of arcs entering and leaving node i, respectively.
- B_i represents the commodity balance at node i.
- N represents the set of nodes in the network.
- X_ij represents the flow variable for arc (i, j).
- U_ij represents the upper bound on the flow for arc (i, j).
- Y_ij is a binary variable indicating whether arc (i, j) is selected.

## Dataset (SDNLib)
The SDNLib dataset is used as an example input for the solver. SDNLib is a collection of synthetic directed networks designed for studying network flow problems. You can find more information about the SDNLib dataset at [SDNLib website](http://sndlib.zib.de/home.action).

## Usage
1- Clone the repository:
```
git clone https://github.com/itsmohsenjalali/mip_cplex
```

2- Install the required dependencies:
```
pip install -r requirements.txt
```

3- Run the solver
```
python graph_solver.py
```

or Use Docker for running the solver

1- Build docker image

```
docker build -t mip-cplex .
```

2- Run docker image
```
docker run mip-cplex
```

## Contributing
Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

