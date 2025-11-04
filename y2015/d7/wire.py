class Wire:
    def __init__(self, id: str, source: str, signal: int = None):
        self.id = id
        self.source = source
        self.signal = signal
    
    def get_id(self) -> str:
        return self.id 
    
    def set_signal(self, signal):
        self.signal = signal
    
    def get_signal(self) -> int:
        return signal

    def get_source(self) -> str:
        return self.source 
    
    def __str__(self) -> str:
        return f"Wire {self.get_id()} src({self.get_source()}) -> signal ({self.get_signal()})"

    def __repr__(self) -> str:
        return f"Wire(id={self.id!r}, source={self.source!r}, signal={self.signal!r})" 