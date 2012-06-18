Redis patterns | search
#######################
:date: 2010-11-26 02:55
:tags: python, autocomplete, redis

Problem
~~~~~~~

You want to implement search against user objects stored in redis using
Python. Something like querying for all user ids whose username begins
with "an".

Solution
~~~~~~~~

Here we have user objects stored in as hashes with "user:obj:" as
prefix.

For example

::

    user:obj:3955 {id: 3955, username: 'John', ..}

We need some extra data structures to support our search i.e. (search
user objects where username begins with given phrase. So search for
``jo`` should match John, Joe and so on. We will use sorted sets of all
usernames and will assign every element a score. This score is a float
and helps us in finding the matching words.

Some scores for eg.

::

    a -> 0.097ab -> 0.097098ac -> 0.097099bc -> 0.098099

So for above four string if we find strings that has score that is =>
0.097 and < 0.098, we find all strings that begins with 'a'

Code


.. code:: python

    # Search usernames that begins with given phrase
    #
    # usernames: (username1, username2, ..)
    # userscore:<username>: float
    # user:obj: { id: int, username: string }
    
    usernames_zset = "usernames"
    
    def my_ord(c):
        return "%03d" % ord(c)
    
    def get_score(s):
        return '0.' + ''.join(map(str, map(my_ord,s)))
    
    def get_next_score(s):
        s_score = get_score(s)
        part0 = s_score[:4]
        c = s_score[4]
        next_c = str(int(c)+1)
        part1 = s_score[5:]
        return part0 + next_c + part1
    
    def add_user(conn, username, score):
        # The User Object
        uid = conn.incr('user:idgen')
        conn.hset('user:obj:%d' % uid, 'id', username)
        # datastructures necessary to implement search
        conn.zadd(usernames_zset, username, score)
    
    def add_test_data(conn):
        test_data = ('abc', 'ab', 'a', 'shekhar', 'shon', 'sh', \
            'zxcvbnmasdfghjklqwertyuiop0', 'zxcvbnmasdfghjklqwertyuiop00')
    
        for username in test_data:
            score = get_score(username)
            add_user(conn, username, score)
    
    import redis
    conn = redis.Redis()
    
    add_test_data(conn)
    
    # conn.zrange(usernames_zset, 0, -1) # Whole set
    a_score = get_score('a')
    b_score = get_next_score('a')
    
    print 'Find all users starting with "a" -> INF'
    print conn.zrangebyscore(usernames_zset, a_score, 'INF')
    print 'Find all users starting with "a"'
    print conn.zrangebyscore(usernames_zset, a_score, b_score)
    print 'Find all users starting with "a" limit 2'
    print conn.zrangebyscore(usernames_zset, a_score, 'INF', 0, 2)


.. <script src="https://gist.github.com/716212.js"> </script>

Discussion
~~~~~~~~~~

This to demonstrate simple redis pattern and using it in Python.

See Also
~~~~~~~~

-  `ZrangebyscoreCommand`_

There are already some good writeups on related topics.

-  `playnicely`_
-  `autocomplete`_

.. _ZrangebyscoreCommand: http://code.google.com/p/redis/wiki/ZrangebyscoreCommand
.. _playnicely: http://playnice.ly/blog/2010/05/24/redis-multi-field-searching-and-filtering/
.. _autocomplete: http://antirez.com/post/autocomplete-with-redis.html
