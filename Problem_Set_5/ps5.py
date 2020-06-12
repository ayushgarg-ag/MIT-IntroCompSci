# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: Ayush Garg

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz
utc = pytz.UTC


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
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

# # NewsStory
class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
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
        raise NotImplementedError

# # PHRASE TRIGGERS
# Problem 2: PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase

    def is_phrase_in(self, title):
        title = title.lower()
        for punc in string.punctuation:
            title = title.replace(punc, ' ')
        list_of_words = title.split(" ")
        temp_list = []
        for word in list_of_words:
            if (word != ''):
                for punc in string.punctuation:
                    word = word.replace(punc, '')
                temp_list.append(word)
        for word in self.phrase.lower().split(' '):
            if (word not in temp_list):
                return False
        if(self.phrase.lower() in " ".join(temp_list)):
            return True
        return False

# Problem 3: TitleTrigger
class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)

    def evaluate(self, NewsStory):
        return self.is_phrase_in(NewsStory.get_title())

# Problem 4: DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)

    def evaluate(self, NewsStory):
        return self.is_phrase_in(NewsStory.get_description())

# # TIME TRIGGERS
# Problem 5: TimeTrigger
class TimeTrigger(Trigger):
    def __init__(self, input_time):
        # Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
        # Convert time from string to a datetime before saving it as an attribute.
        self.input_time = datetime.strptime(
            input_time, "%d %b %Y %H:%M:%S").replace(tzinfo=utc)

# Problem 6: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def evaluate(self, NewsStory):
        story_time = NewsStory.get_pubdate().replace(tzinfo=utc)
        return self.input_time > story_time

class AfterTrigger(TimeTrigger):
    def evaluate(self, NewsStory):
        story_time = NewsStory.get_pubdate().replace(tzinfo=utc)
        return self.input_time < story_time

# # COMPOSITE TRIGGERS
# Problem 7: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, Trigger):
        self.trigger = Trigger

    def evaluate(self, story):
        return not self.trigger.evaluate(story)

# Problem 8: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, Trigger1, Trigger2):
        self.trigger1 = Trigger1
        self.trigger2 = Trigger2

    def evaluate(self, story):
        return self.trigger1.evaluate(story) and self.trigger2.evaluate(story)

# Problem 9: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, Trigger1, Trigger2):
        self.trigger1 = Trigger1
        self.trigger2 = Trigger2

    def evaluate(self, story):
        return self.trigger1.evaluate(story) or self.trigger2.evaluate(story)

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    filtered_list = []
    for story in stories:
        for trigger in triggerlist:
            if (trigger.evaluate(story)):
                filtered_list.append(story)
    return filtered_list

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
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    trigger_dict = {}
    returned_triggers = []
    SPECIFICATION_KEYWORDS = ['TITLE', 'DESCRIPTION', 'AFTER', 'BEFORE']
    COMBINATION_KEYWORDS = ['NOT', 'AND', 'OR']
    for line in lines:
        elements = line.split(',')
        if elements[0] != 'ADD':
            keyword = elements[1]
            if (keyword in SPECIFICATION_KEYWORDS):
                if (keyword == 'TITLE'):
                    trigger_dict[elements[0]] = TitleTrigger(elements[2])
                elif (keyword == 'DESCRIPTION'):
                    trigger_dict[elements[0]] = DescriptionTrigger(elements[2])
                elif (keyword == 'AFTER'):
                    trigger_dict[elements[0]] = AfterTrigger(elements[2])
                else:
                    trigger_dict[elements[0]] = BeforeTrigger(elements[2])
            else:
                if (keyword == 'AND'):
                    trigger_dict[elements[0]] = AndTrigger(
                        elements[2], elements[3])
                elif (keyword == 'OR'):
                    trigger_dict[elements[0]] = OrTrigger(
                        elements[2], elements[3])
                else:
                    trigger_dict[elements[0]] = NotTrigger(elements[2])
        else:
            for i in range(1, len[elements]):
                returned_triggers.append(trigger_dict[elements[i]])
    return returned_triggers


SLEEPTIME = 120  # seconds -- how often we poll

def main_thread(master):
    try:
        t1 = TitleTrigger("Coronavirus")
        t2 = DescriptionTrigger("Covid")
        t3 = DescriptionTrigger("19")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        triggerlist = read_trigger_config('triggers.txt')

        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT, fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica", 14),
                    yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []

        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(
                    END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(
                    END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:
            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

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