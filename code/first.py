class CoreNode:
    def __init__(self, name, node_type):
        self.name = name
        self.node_type = node_type  # AMF, UPF, SGW, PGW, etc.
        self.routing_table = {}  # Table de routage IP/MPLS
        self.label_table = {}    # Table de labels MPLS

    def add_route(self, destination, next_hop):
        self.routing_table[destination] = next_hop

    def add_label(self, label, destination):
        self.label_table[label] = destination

    def forward_packet(self, packet):
        if packet.label:
            # MPLS Forwarding
            if packet.label in self.label_table:
                next_hop = self.label_table[packet.label]
                print(f"{self.name} ({self.node_type}): MPLS Forwarding packet to {next_hop}")
            else:
                print(f"{self.name} ({self.node_type}): Label {packet.label} not found!")
        else:
            # IP Forwarding
            if packet.destination in self.routing_table:
                next_hop = self.routing_table[packet.destination]
                print(f"{self.name} ({self.node_type}): IP Forwarding packet to {next_hop}")
            else:
                print(f"{self.name} ({self.node_type}): Destination {packet.destination} not reachable!")

class Link:
    def __init__(self, node1, node2, cost=1):
        self.node1 = node1
        self.node2 = node2
        self.cost = cost

class Packet:
    def __init__(self, source, destination, label=None, data=""):
        self.source = source
        self.destination = destination
        self.label = label
        self.data = data