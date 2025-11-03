from dataclasses import dataclass
import re

@dataclass(slots=True)
class Passport:
    byr: str|None=None; iyr: str|None=None; eyr: str|None=None
    hgt: str|None=None; hcl: str|None=None; ecl: str|None=None
    pid: str|None=None; cid: str|None=None
    
    colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
      
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
    
    def is_valid_byr(self) -> bool:
        if(self.byr is None): return False

        return all([
            len(self.byr) == 4,
            1920 <= int(self.byr) <= 2002
        ]) 
    
    def is_valid_iyr(self) -> bool:
        if(self.iyr is None): return False

        return all([
            len(self.iyr) == 4,
            2010 <= int(self.iyr) <= 2020
        ]) 
    
    def is_valid_eyr(self) -> bool:
        if(self.eyr is None): return False

        return all([
            len(self.eyr) == 4,
            2020 <= int(self.eyr) <= 2030
        ]) 
    
    def is_valid_hgt(self) -> bool:
        if(self.hgt is None): return False
        
        height = self._split_hgt()
        if(not height): return False
        
        value, unit = height
        return all([
            self._get_range_by_unit(unit, value)
        ]) 
    
    def is_valid_hcl(self) -> bool:
        if(self.hcl is None): return False 
        pat = re.compile(r'^#[a-z0-9]{6}$') 
         
        return bool(pat.match(self.hcl)) 
    
    def is_valid_ecl(self) -> bool:
        if(self.ecl is None): return False
        
        return self.ecl in self.colors
    
    def is_valid_pid(self) -> bool:
        if(self.pid is None): return False 
        pat = re.compile(r'^[0-9]{9}$') 
         
        return bool(pat.match(self.pid)) 
    
    def is_valid(self) -> bool:
        return all([
            self.has_required_fields(),
            self.is_valid_byr(),
            self.is_valid_iyr(),
            self.is_valid_eyr(),
            self.is_valid_hgt(),
            self.is_valid_hcl(),
            self.is_valid_ecl(),
            self.is_valid_pid(),
            ])
    
    def _get_range_by_unit(self, unit, value) -> bool:
        if(unit=="cm"):
            return 150 <= value <= 193
        if(unit=="in"):
            return 59 <= value <= 76
        return False
        
    
    def _split_hgt(self):
        i = 0
        n = len(self.hgt)

        while i < n and self.hgt[i].isdigit():
            i += 1

        if i == 0 or i == n:
            return None

        value = int(self.hgt[:i])
        unit = self.hgt[i:].lower()
        return value, unit