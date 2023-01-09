def newOrder(**kwargs):
    for key, value in kwargs.items():
        print('{} is equal to {}'.format(key, value))


newOrder(tea='Green', price=400, size='medium', sugar=True)

