AltCodeBot v0.9
===============

A Reddit bot that replies to comments with the alt key code of special characters.

Reply Commands:
    !ignore me (User) - bot will no longer reply to user
	!ignore sub (Mod) - bot will no longer post in subreddit

Initialization:
In the same working directory as the altcodebot.py file...

Create a user and password config file with:
    >>> import shelve
	>>> c = shelve.open('credentials.db', writeback=True)
	>>> c['user'] = 'botusername'
	>>> c['password'] = 'botpassword'
	>>> c.close()

Create your initial ignore_user list (and ignore your bot) with:
    >>> import shelve
	>>> u = shelve.open('ignore_users.db', writeback=True)
	>>> u['botusername'] = 1
	>>> u.close()
	

To-Do List:
- Test more
- Possibly add per-sub rules