from dataclasses import dataclass

@dataclass(slots=True)
class Passport:
    byr: str|None=None; iyr: str|None=None; eyr: str|None=None
    hgt: str|None=None; hcl: str|None=None; ecl: str|None=None
    pid: str|None=None; cid: str|None=None
      
    def has_required_fields(self) -> bool:
        return all([
            self.byr is not None,
            self.iyr is not None,
            self.eyr is not None,
            self.hgt is not None,
            self.hcl is not None,
            self.ecl is not None,
            self.pid is not None,
        ])
    
    def is_valid(self) -> bool:
        return (
            self.has_required_fields()
        )