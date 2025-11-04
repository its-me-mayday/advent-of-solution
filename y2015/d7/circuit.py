from wire import Wire

class Circuit:
    def __init__(self, wires:set[Wire] = set()):
        self.wires = wires
    
    def add(self, wire):
        self.wires.add(wire)
    
    def get_wires(self) -> set[Wire]:
        return self.wires
    
    def __str__(self) -> str:
        content = ", ".join(str(w) for w in sorted(self.wires, key=lambda w: w.get_id()))
        return f"Circuit({{{content}}})"