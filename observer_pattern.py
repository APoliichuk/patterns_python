from collections import defaultdict

mailing_list = defaultdict(list)


def subscribe(mailbox, subscriber):
    mailing_list[mailbox].append(subscriber)


def notify_subscribers(mailbox, *args, **kwargs):
    for subscriber in mailing_list[mailbox]:
        subscriber(*args, **kwargs)


def fun(x):
    print('FUN %s' % x)


def bar(x):
    print('BAR %s' % x)


subscribe('FIRST', fun)
subscribe('FIRST', bar)

subscribe('SECOND', fun)


notify_subscribers('FIRST', x='0000000002')
notify_subscribers('SECOND', x='0000000001')
