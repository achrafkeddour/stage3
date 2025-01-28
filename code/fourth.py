# Envoyer un paquet avec routage IP
core_network.send_packet("AMF", "PGW", data="User data over IP")

# Envoyer un paquet avec un label MPLS
core_network.send_packet("SGW", "PGW", label=100, data="User data over MPLS")