from fluent import sender

import msgpack
from io import BytesIO


def overflow_handler(pendings):
    unpacker = msgpack.Unpacker(BytesIO(pendings))
    for unpacked in unpacker:
        print(unpacked)


# for local fluent
# logger = sender.FluentSender('app')

# for remote fluent
# logger = sender.FluentSender("service-a.ServiceController","fluentd-es.logging",24224)
# logger = sender.FluentSender('fluent-python', host='192.168.181.99', port=30224)
logger = sender.FluentSender('fluent-python', host='192.168.181.99', port=30224,
                             buffer_overflow_handler=overflow_handler)
# Use current time
# logger.emit('test', {'from': 'userA', 'to': 'userB','face':'smile'})

if not logger.emit('testtt', {'from': 'userA', 'to': 'userB'}):
    print(logger.last_error)
    logger.clear_last_error()  # clear stored error after handled errors
