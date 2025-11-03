from passport import Passport

def scan(datas): 
    return make_passport(datas)
    
def make_passport(pairs: list[str]) -> Passport:
    d = dict(s.split(":", 1) for s in pairs)
    return Passport(**{k: d.get(k) for k in Passport.__dataclass_fields__})