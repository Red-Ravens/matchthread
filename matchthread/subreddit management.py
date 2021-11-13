#!/usr/bin/env python3
#####################################
#    LAST UPDATED     11 NOV 2021   #
#####################################
"""
Restricts /r/ussoccer subreddit during time periods
"""
import sys
import praw
import praw_oauth2


def restrict_subreddit(r: praw.Reddit) -> None:
    """
    Restrict the /r/ussoccer subreddit
    :param r: praw.Reddit object that has privileges to restrict subreddit
    :return: None
    """
    r.subreddit("ussoccer").mod.update(content_options='link')


def unrestrict_subreddit(r: praw.Reddit) -> None:
    """
    Un-restrict the /r/ussoccer subreddit
    :param r: praw.Reddit object that has privileges to unrestrict subreddit
    :return: None
    """
    r.subreddit("ussoccer").mod.update(content_options='any')


if __name__ == '__main__':
    ussoccer = praw_oauth2.ussoccer_bot()
    arg = sys.argv[1]
    if arg in ('-r', '--restrict'):
        print('Restricting')
        restrict_subreddit(ussoccer)
    elif arg in ('-u', '--unrestrict'):
        print('Unrestricting')
        unrestrict_subreddit(ussoccer)
    else:
        print("Found {} at sys.argv[1]".format(arg))
