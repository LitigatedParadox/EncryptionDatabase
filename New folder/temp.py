while True:
    from bs4 import BeautifulSoup
    import requests

    ThreadsOfInterest = []
    URL = "https://boards.4chan.org/h/"
    File = open("Site.txt", "w+", encoding='utf-8')

    Source = requests.get(URL)

    Soup = BeautifulSoup(Source.content, 'html.parser')
    Soup = str(Soup)
    Threads = Soup.split('class="thread"')
    def ThreadFinder(tag):
        i = 0
        for thread in Threads:
            if tag in thread:
                i += 1
                ThreadsOfInterest.append(thread)
        if i > 0:
            print(i, "threads found")
            Display = input("Would you like to display these thread names? (Y/N) ")
            if Display == "Y" or "y":
                for thread in ThreadsOfInterest:
                    thread = str(thread)
                    Subjects = thread.split('class="subject"')
                    for subject in Subjects:
                        if tag in subject:
                            print(subject)
            if Display == "N":
                pass

                    

    UserTag = input("Please input the tag you would like to search for: ")
    ThreadFinder(UserTag)