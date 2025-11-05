from wire import Wire

class Circuit:
    def __init__(self):
        self._wires_by_id: dict[str, Wire] = {}
    
    def add(self, wire: Wire) -> None:
        self._wires_by_id[wire.id] = wire
    
    def get_wire(self, wire_id: str) -> Wire | None:
        return self._wires_by_id.get(wire_id)

    def get_wires(self) -> set[Wire]:
        return set(self._wires_by_id.values()) 

    def __len__(self) -> int:
        return len(self._wires_by_id)

    def __iter__(self):
        return iter(self._wires_by_id.values())

    def __str__(self) -> str:
        parts = []
        for w in self._wires_by_id.values():
            try:
                s = str(w)
            except Exception:
                s = f"Wire(id={getattr(w, 'id', '?')})"
            parts.append(s)
        wires_str = ", ".join(parts) if parts else "∅"
        return f"Circuit[{len(self)}]: {{ {wires_str} }}"