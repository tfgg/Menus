import time
import datetime
import imaplib
import email
import quopri
import proc

import local_settings

def last_sunday(date):
  while date.weekday() != 6:
    date = date - datetime.timedelta(1)
  return date

M = imaplib.IMAP4_SSL("imap.gmail.com")
M.login("lincoln.internal.web.mcr@gmail.com", local_settings.email_pass)
M.select()
typ, data = M.search(None, '(SUBJECT "Menu")')
for num in data[0].split():
    typ, data = M.fetch(num, '(RFC822)')

    e = email.message_from_string(data[0][1])

    date = datetime.datetime.fromtimestamp(time.mktime(email.utils.parsedate(e.get('date'))))

    if date.timetuple() < (datetime.date.today()- datetime.timedelta(0)).timetuple() :
      continue

    start_date = last_sunday(date.date()) + datetime.timedelta(1)

    if e.is_multipart():
      for msg in e.get_payload():
        if msg['Content-Type'] == 'text/html; charset=ISO-8859-1':
          email_html = msg.get_payload()

          email_html = quopri.decodestring(email_html)
          proc.parse_html(email_html, start_date, False)
    
    print 'Message %s %s %s' % (num, e.get('subject'), start_date)
M.close()
M.logout()
