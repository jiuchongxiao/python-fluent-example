import msgpack
from io import BytesIO

import logging
from fluent import asynchandler as handler

def overflow_handler(pendings):
    unpacker = msgpack.Unpacker(BytesIO(pendings))
    for unpacked in unpacker:
        print(unpacked)


custom_format = {
  'host': '%(hostname)s',
  'where': '%(module)s.%(funcName)s',
  'type': '%(levelname)s',
  'stack_trace': '%(exc_text)s'
}


logging.basicConfig(level=logging.INFO)
l = logging.getLogger('fluent.test')
h = handler.FluentHandler('fluent-python.asyn-log', host='192.168.181.99', port=30224, buffer_overflow_handler=overflow_handler)
formatter = handler.FluentRecordFormatter(custom_format)
h.setFormatter(formatter)
l.addHandler(h)


# ---  具体log日志
l.info({
  'from': 'userA',
  'to': 'userB'
})
l.info('{"from": "userC", "to": "userD"}')
l.info("This log entry will be logged with the additional key: 'message'.")
l.error({'erro':"erro info message"})