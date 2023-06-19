def read_data_from_file():
    node_flag = False
    link_flag = False
    demand_flag = False

    node_data = []
    link_data = []
    demand_data = []

    with open("./dataset.txt", mode="r") as file:
        for item in file.readlines():
            if not (node_flag or link_flag or demand_flag):
                if item.startswith("#") or item.startswith("\n") or item.startswith("?"):
                    continue
                elif item.startswith("NODES"):
                    node_flag = True
                elif item.startswith("LINKS"):
                    link_flag = True
                elif item.startswith("DEMANDS"):
                    demand_flag = True
            else:
                if item.startswith(")"):
                    node_flag = False
                    link_flag = False
                    demand_flag = False
                elif node_flag:
                    node_data.append(item.strip())
                elif link_flag:
                    link_data.append(item.strip())
                elif demand_flag:
                    demand_data.append(item.strip())
                
    return node_data, link_data, demand_data

def get_data_dict(node_data, link_data, demand_data):
    data_dict = {}
    data_dict["nodes"] = []
    data_dict["edges"] = []
    data_dict["demands"] = {}
    data_dict["B"] = {}

    for node in node_data:
        node = list(filter(lambda x: x != "", node.replace("(", "").replace(")", "").split(" ")))
        data_dict["nodes"].append(node[0])
        data_dict["B"][node[0]] = 0
    for link in link_data:
        link = list(filter(lambda x: x != "", link.replace("(", "").replace(")", "").split(" ")))
        data_dict["edges"].append((link[1], link[2], float(link[3]), float(link[5])))
    for demand in demand_data:
        demand = list(filter(lambda x: x != "", demand.replace("(", "").replace(")", "").split(" ")))
        data_dict["demands"][(demand[1], demand[2])] = float(demand[4])
    return data_dict

if __name__ == "__main__":
    node_data, link_data, demand_data = read_data_from_file()
    data_dict = get_data_dict(node_data, link_data, demand_data)
    print(data_dict)