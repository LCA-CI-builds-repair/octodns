#
def filter_public(data):
    public_data = [item for item in data if not item.get('private')]
    return public_data
        self.name = name
        self._type = _type
        self.ttl = ttl
        self.rdata = rdata

    def __repr__(self):
        return f'Rr<{self.name}, {self._type}, {self.ttl}, {self.rdata}'
