class Twitter:
    def __init__(self, name):
        self.followers = set()
        self.name = name

    def tweet(self, message):
        print("{} says: ".format(self.name)+message)
        for follower in self.followers:
            follower.notify(message)

    def follow(self, who):
        who.followers.add(self)
        return self

    def notify(self, message):
        print("{} got the message: {}".format(self.name, message))


a = Twitter('Alice')
k = Twitter('King')
q = Twitter('Queen')
h = Twitter('Mad Hatter')
c = Twitter('Cheshire Cat')
a.follow(c).follow(h).follow(q)
k.follow(q)
q.follow(q).follow(h)
h.follow(a).follow(q).follow(c)

print(f'==== {q.name} tweets ====')
q.tweet('Off with their heads!')
print(f'\n==== {a.name} tweets ====')
a.tweet('What a strange world we live in.')
print(f'\n==== {k.name} tweets ====')
k.tweet('Begin at the beginning, and go on till you come to the end: then stop.')
print(f'\n==== {c.name} tweets ====')
c.tweet("We're all mad here.")
print(f'\n==== {h.name} tweets ====')
h.tweet('Why is a raven like a writing-desk?')


