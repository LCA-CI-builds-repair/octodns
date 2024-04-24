#
#
#

frclass TxtRecord(_ChunkedValuesMixin, Record):
    _type = 'TXT'
    _value_type = TxtValue

    def __init__(self, *args, **kwargs):
        super(TxtRecord, self).__init__(*args, **kwargs)
        # Add any specific initialization code here for TxtRecordse import Record
from .chunked import _ChunkedValue, _ChunkedValuesMixin


class TxtValue(_ChunkedValue):
    pass


class TxtRecord(_ChunkedValuesMixin, Record):
    _type = 'TXT'
    _value_type = TxtValue


Record.register_type(TxtRecord)
