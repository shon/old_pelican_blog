# -*- coding: utf-8 -*-
"""Settings for pelican."""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


AUTHOR = 'Shekhar Tiwatne'
SITENAME = 'ɹ ɐ ɥ ʞ ǝ ɥ s '
SITEURL = 'http://shon.github.com'

# This can also be the absolute path to a theme that you downloaded
# i.e. './themes/anothertheme/'
THEME = 'notmyidea'

# The folder ``images`` should be copied into the folder ``static`` when
# generating the output.
STATIC_PATHS = ['images']

# See http://pelican.notmyidea.org/en/latest/settings.html#timezone
TIMEZONE = 'Asia/Calcutta'

# Pelican will take the ``Date`` metadata and put the articles into folders
# like ``/posts/2012/02/`` when generating the output.
ARTICLE_PERMALINK_STRUCTURE = '/%Y/%m/'

# I like to put everything into the category ``Blog``, which also appears on
# the main menu. Tags will not appear on the menu.
DEFAULT_CATEGORY = 'Blog'

# I like to have ``Archives`` in the main menu.
MENUITEMS = (
    ('Archives', '{0}/archives.html'.format(SITEURL)),
)


WITH_PAGINATION = True
DEFAULT_PAGINATION = 4
REVERSE_ARCHIVE_ORDER = True
DISPLAY_PAGES_ON_MENU = ['About me.html']
DISPLAY_PAGES_ON_MENU = True
#MENUITEMS = (('About me', 'http://flavors.me/shon'),)

SOCIAL = (('twitter', 'http://twitter.com/shon_'), ('github', 'http://github.com/shon'), ('facebook', 'http://facebook.com/shon0'))

TYPOGRIFY = True

# Uncomment what ever you want to use
#GOOGLE_ANALYTICS = 'XX-XXXXXXX-XX'
DISQUS_SITENAME = 'shon-blog'
#GITHUB_URL = 'http://github.com/username/username.github.com'
TWITTER_USERNAME = 'shon_'
