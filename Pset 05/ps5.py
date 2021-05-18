# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz
import re


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory
class NewsStory(object):
    def __init__(self,guid,title,description,link,pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
        
    def get_guid(self):
        return self.guid
    
    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def get_link(self):
        return self.link
    
    def get_pubdate(self):
        return self.pubdate
    
    
        

#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self,phrase):
        self.phrase = phrase
        
    def is_phrase_in(self,text):
        story_lower = text.lower()
        temp = re.findall('[\w]+',story_lower)
        phrase_pieces = self.phrase.lower().split()
        index_lst = []
         
        for word in phrase_pieces:
            if word in temp: continue
            else:
                return False
            
        for i in range(len(phrase_pieces)):
            for j in range(len(temp)):
                if temp[j] == phrase_pieces[i]:
                    ind = temp.index(temp[j])
                    index_lst.append(ind)
                    break
                
        for i in range(1,len(index_lst)):
            if index_lst[i] - index_lst[i-1] != 1:
                return False
        return True    
          
                
# story1 = 'The purple cow is soft and cuddly.'
# test1 = PhraseTrigger('Purple Cow')
# print('Should return True.')
# print(test1.is_phrase_in(story1))           
# print('==========================================')            
# print('==========================================')                
# story2 = 'Cow!!! Purple!!!'
# test2 = PhraseTrigger('PURPLE COW')        
# print('Should return False.')
# print(test2.is_phrase_in(story2))        
# print('==========================================')            
# print('==========================================')            
        

# Problem 3
# TODO: TitleTrigger
class TitleTrigger(PhraseTrigger):
    def __init():
        PhraseTrigger.__init__()
        
    def evaluate(self,news):
        if self.is_phrase_in(news.get_title()):
            return True
        else:
            return False

# Problem 4
# TODO: DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
    def __init():
        PhraseTrigger.__init__()
        
    def evaluate(self,news):
        if self.is_phrase_in(news.get_description()):
            return True
        else:
            return False
# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    def __init__(self,date):
        date_time_naive = datetime.strptime(date,'%d %b %Y %H:%M:%S')
        date_time_aware = date_time_naive.replace(tzinfo = pytz.timezone('EST'))
        self.date_time_naive = date_time_naive
        self.date_time_aware = date_time_aware
        

# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def __init__(self,date):
        TimeTrigger.__init__(self,date)
        
    def evaluate(self,news):
        try:
            if self.date_time_naive > news.get_pubdate():
                return True
            else:
                return False
        except:
            if self.date_time_aware > news.get_pubdate():
                return True
            else:
                return False

class AfterTrigger(TimeTrigger):
    def __init__(self,date):
        TimeTrigger.__init__(self,date)
        
    def evaluate(self,news):
        try:
            if self.date_time_naive < news.get_pubdate():
                return True
            else:
                return False
        except:
            if self.date_time_aware < news.get_pubdate():
                return True
            else:
                return False
                

# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self,trigger):
        self.trigger = trigger
        
    def evaluate(self,news):
        if self.trigger.evaluate(news):
            return False
        else:
            return True
            
# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self,trigger1,trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
        
    def evaluate(self,news):
        if self.trigger1.evaluate(news) and self.trigger2.evaluate(news):
            return True
        else:
            return False
# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self,trigger1,trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
        
    def evaluate(self,news):
        if self.trigger1.evaluate(news) or self.trigger2.evaluate(news):
            return True
        else:
            return False

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    
    # iterate every story in list
    # check if each trigger in triggerlist fires
    
    triggerstories = []
    for story in stories:
        for trigger in triggerlist:
            if not trigger.evaluate(story):
                continue
            else:
                triggerstories.append(story)
                
    return triggerstories



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    trglist = []
    trgdict = {}
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            #lines.append(line)
            line = line.split(',')
            lines.append(line)
            
    trgdict = {'TITLE' : TitleTrigger,
               'DESCRIPTION' : DescriptionTrigger,
               'BEFORE' : BeforeTrigger,
               'AFTER' : AfterTrigger,
               'AND' : AndTrigger,
               'OR' : OrTrigger,
               'NOT' : NotTrigger
        } 
       
    t_dict = {}        
    for line in lines:
        if 'TITLE' in line:
            t_dict[line[0]] = trgdict['TITLE'](line[2])
        elif 'DESCRIPTION' in line:
            t_dict[line[0]] = trgdict['DESCRIPTION'](line[2])
        elif 'BEFORE' in line:
            t_dict[line[0]] = trgdict['BEFORE'](line[2])
        elif 'AFTER' in line:
            t_dict[line[0]] = trgdict['AFTER'](line[2])
        elif 'AND' in line:
            t_dict[line[0]] = trgdict['AND'](t_dict[line[2]],t_dict[line[3]])
        elif 'OR' in line:
            t_dict[line[0]] = trgdict['OR'](t_dict[line[2]],t_dict[line[3]])
        elif 'NOT' in line:
            t_dict[line[0]] = trgdict['NOT'](t_dict[line[2]])
        else:
            for item in line[1:]:
                trglist.append(t_dict[item])
            
    
    return trglist

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    # print(trgdict)
    # print(lines) # for now, print it so you see what it contains!
    
print(read_trigger_config('triggers.txt'))    



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        # t1 = TitleTrigger("election")
        # t2 = DescriptionTrigger("Trump")
        # t3 = DescriptionTrigger("Biden")
        # t4 = AndTrigger(t2, t3)
        # triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            # stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

