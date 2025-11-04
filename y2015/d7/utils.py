from circuit import Circuit
from wire import Wire

def init_circuit(booklet) -> Circuit:
    print("booklet:", booklet)
    circuit = Circuit()
    for instruction in booklet:
        wire_id, wire_source = _parse_instructions(instruction)
        wire = Wire(wire_id, wire_source)
        
        if(wire_source.isnumeric()): wire.set_signal(int(wire_source))
        circuit.add(wire)

    return circuit 

def _parse_instructions(instruction):
    instruction_arr = instruction.split("->")
    return instruction_arr[1].strip(), instruction_arr[0].strip()