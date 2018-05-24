
from fluent import sender, event


# for local fluent
# logger = sender.FluentSender('app')

# for remote fluent
# logger = sender.FluentSender("service-a.ServiceController","fluentd-es.logging",24224)
logger = sender.FluentSender('fluent-python', host='192.168.181.99', port=30224)

# send event to fluentd, with 'app.follow' tag
event.Event('follow-event-base', {
  'from': 'userA',
  'to':   'userB'
})