class CoreNetwork:
    def __init__(self):
        self.nodes = {}
        self.links = []

    def add_node(self, name, node_type):
        self.nodes[name] = CoreNode(name, node_type)

    def add_link(self, node1_name, node2_name, cost=1):
        if node1_name in self.nodes and node2_name in self.nodes:
            link = Link(self.nodes[node1_name], self.nodes[node2_name], cost)
            self.links.append(link)
        else:
            print("One or both nodes not found!")

    def send_packet(self, source, destination, label=None, data=""):
        if source in self.nodes:
            packet = Packet(source, destination, label, data)
            self.nodes[source].forward_packet(packet)
        else:
            print(f"Source node {source} not found!")