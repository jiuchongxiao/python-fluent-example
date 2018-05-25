from fluent import event, asyncsender as sender

# for local fluent
# sender.setup('app')

# for remote fluent
sender.setup('fluent-python-asyn-sender', host='192.168.181.99', port=30224)
# do your work
event.Event('follow-asyn-event-base', {
    'from': 'userA',
    'to':   'userB'
})

# IMPORTANT: before program termination, close the sender
sender.close()