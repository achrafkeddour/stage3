# Initialiser le réseau
core_network = CoreNetwork()

# Ajouter des nœuds
core_network.add_node("AMF", "AMF")
core_network.add_node("UPF1", "UPF")
core_network.add_node("UPF2", "UPF")
core_network.add_node("SGW", "SGW")
core_network.add_node("PGW", "PGW")

# Ajouter des liens
core_network.add_link("AMF", "SGW")
core_network.add_link("SGW", "UPF1")
core_network.add_link("SGW", "UPF2")
core_network.add_link("UPF1", "PGW")
core_network.add_link("UPF2", "PGW")

# Configurer les routes et labels
core_network.nodes["AMF"].add_route("PGW", "SGW")
core_network.nodes["SGW"].add_route("PGW", "UPF1")
core_network.nodes["SGW"].add_label(100, "UPF1")
core_network.nodes["UPF1"].add_route("PGW", "PGW")
core_network.nodes["UPF2"].add_route("PGW", "PGW")