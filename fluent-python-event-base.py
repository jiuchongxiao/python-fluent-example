
from fluent import sender, event


# for local fluent
# logger = sender.FluentSender('app')

# for remote fluent
sender.setup('fluent-python-asyn-sender', host='192.168.181.99', port=30224)
# send event to fluentd, with 'app.follow' tag
event.Event('follow-event-base', {
  'from': 'userA',
  'to':   'userB'
})