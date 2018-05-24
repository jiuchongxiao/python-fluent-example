1.目的：将python日志记录到fluent
2.文件说明
    1)fluent-python-fluentsender.py               -> FluentSender Interface 发送fluent日志
    2)fluent-python-event-base.py                 -> Event-Based Interface 发送fluent日志 是对FluentSender的包装
    3)fluent-python-hander-buffer-overflow.py     -> Handler for buffer overflow 对缓存溢出的处理
    4)fluent-python-logging.py                    -> Python logging.Handler interface   定义日志格式 发送fluent日志
    5)fluent-python-logging-Asynchronous .py      -> Asynchronous Communication  定义日志格式异步发送fluent日志
3.python运行各个文件查看fluent记录
http://192.168.181.99:30601
