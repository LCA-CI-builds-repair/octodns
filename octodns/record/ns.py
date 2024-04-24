#
#
#

frclass NsRecord(ValuesMixin, Record):
    _type = 'NS'
    _value_type = NsValue

    def __init__(self, *args, **kwargs):
        super(NsRecord, self).__init__(*args, **kwargs)
        # Add any specific initialization code here for NsRecordse import Record, ValuesMixin
from .target import _TargetsValue


class NsValue(_TargetsValue):
    pass


class NsRecord(ValuesMixin, Record):
    _type = 'NS'
    _value_type = NsValue


Record.register_type(NsRecord)
