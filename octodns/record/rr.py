from .exception import RecordException

class RrParseError(RecordException):
    def __init__(self, message='failed to parse string value as RR text'):
        super().__init__(message)

class Rr(object):
    '''
    Simple object intended to be used with Record.from_rrs to allow providers
    that work with RFC formatted rdata to share centralized parsing/encoding
    code
    '''
    
    def from_rrs(self, rrs):
        # Method definition for handling rrs (resource records)
        pass
    
    def to_rdata(self):
        # Method definition for converting to rdata
        pass
    def __init__(self, name, _type, ttl, rdata):
        self.name = name
        self._type = _type
        self.ttl = ttl
        self.rdata = rdata

    def __repr__(self):
        return f'Rr<{self.name}, {self._type}, {self.ttl}, {self.rdata}'
