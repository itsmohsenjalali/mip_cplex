from docplex.mp.model import Model
from load_data import get_data_dict, read_data_from_file

node_data, link_data, demand_data = read_data_from_file()
graph = get_data_dict(node_data, link_data, demand_data)
graph['B']['N11'] = 10
graph['B']['N15'] = -10

# Create a docplex model
model = Model('GraphModel')

# Define decision variables for each edge
edge_vars = {}
traffic_vars = {}
U = max(graph['B'].values())
for source, target, fixed_cost, dynamic_cost in graph['edges']:
    edge_vars[(source, target)] = model.binary_var(name=f'edge_{source}_{target}')
    traffic_vars[(source, target)] = model.continuous_var(lb=0, ub= U * 1 ,name=f'traffic_{source}_{target}')

# Define the objective function
objective =model.sum(traffic_vars[edge] * cost[3] for edge, cost in zip(edge_vars.keys(),graph['edges'])) + model.sum(edge_vars[edge] * cost[2] for edge, cost in zip(edge_vars.keys(),graph['edges']))
model.minimize(objective)

# Add constraints (e.g., each node should have exactly one outgoing edge)
for node in graph['nodes']:
    outgoing_node = [traffic_vars[edge] for edge in traffic_vars if edge[0] == node]
    incoming_node = [traffic_vars[edge] for edge in traffic_vars if edge[1] == node]
    model.add_constraint(model.sum(outgoing_node) - model.sum(incoming_node) == graph['B'][node])

model.print_information()
solution = model.solve()

# Print the solution
# print("Optimal Objective Value:", solution.get_objective_value())
solution.display()
