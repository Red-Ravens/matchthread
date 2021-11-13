###################################
#    LAST UPDATED: 12 NOV 2021   #
###################################
import sys
import os
import praw_oauth2

if __name__ == '__main__':

    if 'pi' in os.getcwd():
        os.chdir('/media/pi/USB20FD/matchthread/')
    else:
        os.chdir('/Users/RedRavens/Documents/Python3/matchthread/')

    if len(sys.argv) > 1:
        toopen = 'wnt'
    else:
        toopen = 'mnt'

    with open('{}.txt'.format(toopen), 'r') as files:
        opp = files.read().split('?')[0]

    subject = 'United States vs {} for /r/ussoccer'.format(opp)

    user_agent = "Match Thread v4.0 modified by /u/RedRavens, using OAuth"

    r = praw_oauth2.redravens()
    r.redditor('MatchThreadder').message('Match Thread', subject)
