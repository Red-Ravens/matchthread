###################################
#    LAST UPDATED: 18 MAR 2018   #
###################################
import sys
import os
import time
import praw_oauth2
from pushbullet import Pushbullet

if __name__ == '__main__':

    if 'pi' in os.getcwd():
        os.chdir('/media/pi/USB20FD/matchthread/')
    else:
        os.chdir('/Users/Alex/Documents/Python3/matchthread/')

    if len(sys.argv) > 2:
        toopen = 'WNT'
    else:
        toopen = 'MNT'

    with open('{}.txt'.format(toopen), 'r') as files:
        opp, place, date, network, kickoff1 = files.read().split('?')

    subject = 'United States vs {}'.format(opp)

    typeOfMatch = '\n'
    avail = '{}, UniMas, Univision'.format(network)
    subjectText = '{} for /r/ussoccer'.format(subject)
    availableOn = '[](/announcement) **Available on**: {}\n\n'.format(avail)

    user_agent = "Match Thread v3.0 modified by /u/RedRavens, using OAuth"

    r = praw_oauth2.redravens()
    r.redditor('MatchThreadder').message('Match Thread', subjectText)

    with open('token.txt') as files:
        token = files.read().strip()
    pb = Pushbullet(token)
    pb.push_note('Requested {}'.format(toopen),
                 '{}'.format(subject), device=pb.get_device('iPhone'))

    time.sleep(4*60)

    # Find the match thread, get its thread id, set its suggested sort to new, and sticky it
    r = praw_oauth2.ussoccer_bot()
    ussoccer = r.subreddit('ussoccer')
    sub_id = '1x1'
    for sub in ussoccer.new(limit=25):
        if 'Match Thread:' in sub.title and sub.author == 'MatchThreadder':
            sub_id = str(sub.id)
            break

    if sub_id != '1x1':
        matchthread = r.submission(id=sub_id).mod
        matchthread.suggested_sort('new')
        matchthread.sticky(bottom=True)
    else:
        pass
