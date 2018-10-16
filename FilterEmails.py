#!/usr/bin/python
import re
import sys
def valid_email(email):
    email_parts = [x.strip() for x in email.split('@')]
    #print(email_parts)
    if len(email_parts)<2:
        return False
    user = re.sub("^[0-9#.!%-_]+", "", email_parts[0]).strip() #re.sub("^[0-9#.!%-_]+", " ", "1234!#%rajesh@gmail.com").strip()
    domain = email_parts[1]
    some_list=["googlemail.com","gmail.com","gmail.co.in","yahoo.com","yahoo.co.in","rediffmail.com","rediffmail.co.in","hotmail.com","hotmail.co.in","rocketmail.com","rocketmail.co.in","sify.com","indiatimes.com","timejobs.com","infosys.com","tcs.com","siemens.com","wipro.com","oracle.com","msn.com","vsnl.com","live.com","live.co.in","yahoomail.com","ymail.com"]
    if len(user) < 3 or len(domain) < 3:
        return False
    if any(domain in s for s in some_list):
        return ""+user+'@'+domain
    else:
        return False


def main(filename, targetfile):
    outfile = open(targetfile, 'w')
    with open(filename) as fp:
        for line in fp:
            email = valid_email(line)
            if email:
                outfile.write(email+'\n')
    outfile.close()

if __name__ == '__main__':
    filename = sys.argv[1]
    targetfile = sys.argv[2]
    main(filename, targetfile)

