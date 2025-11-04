class Circuit:
    def __init__(self, wires:set[Wire] = {}) -> Circuit:
        self.wires = wires
    
    def add_wire(self, wire):
        self.wires.add(wire)
    
    def __str__(self):
        return 
        "Circuit (",
        self.wires,
        ")"
