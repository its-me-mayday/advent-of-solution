from circuit import Circuit
from wire import Wire

def init_circuit(booklet, log) -> Circuit:
    log.info("init_circuit START")
    circuit = Circuit()
    valuable_wires = set()
    
    for instruction in booklet:
        log.info("init_circuit: instruction", instruction)
        log.info("circuit", extra = {"circuit": circuit})
        log.info("valuable_wires", extra = {"valuable_wires": valuable_wires})
        
        wire_id, wire_source = _parse_instruction(instruction)

        log.debug("init_circuit", extra = {"wire_id": wire_id, "wire_source": wire_source})
        wire = Wire(wire_id, wire_source)
        log.info("init_circuit", extra = {"wire": wire})
        
        is_numeric_wire_source = wire_source.isnumeric()
        log.info("init_circuit", extra = {"is_numeric_wire_source": is_numeric_wire_source})
        if(is_numeric_wire_source): 
            wire.set_signal(int(wire_source))
            log.debug("init_circuit (is_numeric_wire_source case)", extra = {"wire": wire})
            circuit.add(wire)
            log.debug("init_circuit (circuit.add(wire))", extra = {"circuit": circuit})
        else:
            log.debug("init_circuit (NOT is_numeric_wire_source)", extra = {"wire": wire})
            valuable_wires.add(wire)
            log.debug("init_circuit (NOT is_numeric_wire_source)", extra = {"valuable_wires": valuable_wires})

    
    log.debug("init_circuit END", extra = {"circuit": circuit})
    log.debug("init_circuit END", extra = {"valuable_wires": valuable_wires})
    return _evaluate_wires(circuit, valuable_wires, log) 

def _evaluate_wires(circuit: Circuit, valuable_wires: set[Wire], log) -> Circuit:
    log.debug("_evaluate_wires START", extra = {"valuable_wires": valuable_wires})
    log.debug("_evaluate_wires START", extra = {"circuit": circuit})
    
    wires = circuit.get_wires()
    log.debug("_evaluate_wires", extra = {"wires from circuit": wires})
    
    while(bool(valuable_wires)):
        log.debug("_evaluate_wires (in loop)", extra = {"bool(valuable_wires)": bool(valuable_wires)})
        evaluated_wires = set()
        log.debug("_evaluate_wires", extra = {"evaluated_wires": evaluated_wires})

        for valuable_wire in valuable_wires:
            log.debug("_evaluate_wires (in second loop)", extra = {"valuable_wire": valuable_wire})
            valuable_wire_signal = valuable_wire.get_signal()
            log.debug("_evaluate_wires (in second loop)", extra = {"valuable_wire_signal": valuable_wire_signal})
            if(valuable_wire_signal is None):
                wire_signal = _parse_source(valuable_wire.get_source(), circuit)
                log.debug("_evaluate_wires (in second loop)", extra = {"wire_signal": wire_signal})

                if(wire_signal is not None):
                    valuable_id_wire = valuable_wire.get_id()
                    log.debug("_evaluate_wires (in second loop) in not None wire_signal", extra = {"valuable_id_wire": valuable_id_wire})
                    wire = Wire(valuable_wire.get_id(), valuable_wire.get_source(), wire_signal)
                    log.debug("_evaluate_wires (in second loop) in not None wire_signal", extra = {"create wire": wire})
                    circuit.add(wire)
                    log.debug("_evaluate_wires (in second loop) in not None wire_signal", extra = {"circuit": circuit})
                    evaluated_wires.add(wire)
                    log.debug("_evaluate_wires (in second loop) in not None wire_signal", extra = {"evaluated_wires": evaluated_wires})

        new_valuable_wires = set() 
        for evaluated_wire in evaluated_wires:
            log.debug("_evaluate_wires in reconciliation loop", extra = {"evaluated_wire": evaluated_wire})
            revaluation_condition = not valuable_wires.__contains__(evaluated_wire.get_id())
            log.debug("_evaluate_wires in reconciliation loop", extra = {"revaluation_condition": revaluation_condition})

            if(revaluation_condition):
                new_valuable_wires.add(evaluated_wire)
                log.debug("_evaluate_wires in reconciliation loop in revaluation_condition", extra = {"new_valuable_wires": new_valuable_wires})
        
        valuable_wires = new_valuable_wires
        log.debug("_evaluate_wires in reconciliation loop (resetting)", extra = {"valuable_wires": valuable_wires})

    log.debug("evaluate_wires END", extra = {"valuable_wires": valuable_wires})
    log.debug("evaluate_wires END", extra = {"circuit": circuit})
    return circuit

def _parse_source(source, circuit: Circuit) -> int:
    split_source = source.split(" ")

    if(len(split_source) == 1): # equal another source
        source_id = split_source[0]
        wire = circuit.get_wire(source_id)
        if(wire is None): return None
        return wire.get_signal()

    if(len(split_source) == 2): # NOT operator
        wire_id = split_source[1]
        wire_signal = circuit.get_wire(wire_id)
        if(wire_signal is None): 
            return None
        else:
            return abs(~wire_signal.get_signal()+1) 
    else:
        wire_id_left = split_source[0]
        wire_id_right = split_source[2]
        wire_operator = split_source[1]
        
        wire_left = circuit.get_wire(wire_id_left)
        if(wire_left is None): return None
        
        wire_signal_left = wire_left.get_signal()
        
        if(wire_id_right.isnumeric()):
            match (wire_operator):
                case "LSHIFT":
                    return int(wire_signal_left)<<int(wire_id_right)
                case "RSHIFT":
                    return int(wire_signal_left)>>int(wire_id_right)
                case _:
                    print("Operator", wire_operator ,"not recognized!")
                    exit(-1)        
        else:

            wire_right = circuit.get_wire(wire_id_right)
            if(wire_right is None): return None

            wire_signal_right = wire_right.get_signal()

            match (wire_operator):
                case "AND":
                    return int(wire_signal_left)&int(wire_signal_right)
                case "OR": 
                    return int(wire_signal_left)|int(wire_signal_right)
                case _:
                    print("Operator", wire_operator ,"not recognized!")
                    exit(-1)        

def _parse_instruction(instruction):
    instruction_arr = instruction.split("->")
    return instruction_arr[1].strip(), instruction_arr[0].strip()