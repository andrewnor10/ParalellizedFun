import requests
import bs4
import threading
import time
import random
import queue
sharedMemory = queue.SimpleQueue()
def callOtherFunctions():
   with open ('urls.txt','r') as ifstream:
      for line in ifstream:
        line = line.strip()
        sharedMemory.put(line)
   while not sharedMemory.empty():
        gohere = sharedMemory.get()
        download(gohere, 'output.txt')
        find_paragraphs(gohere, 'output.txt')
        find_links(gohere, 'output.txt')

def download(url, output_filename):
    "*** YOUR CODE HERE ***"
    r = requests.get(url)
    soup_object = bs4.BeautifulSoup(r.content, features="html.parser")

    with open(output_filename, 'w') as ofile:
        ofile.write(soup_object.text)

def make_pretty(url, output_filename):
    "*** YOUR CODE HERE ***"
    r = requests.get(url)
    soup_object = bs4.BeautifulSoup(r.content, features="html.parser")
    with open(output_filename, 'w') as ofile:
       ofile.write(soup_object.prettify())


def find_paragraphs(url, output_filename):
    "*** YOUR CODE HERE ***"
    r = requests.get(url)
    soup_object = bs4.BeautifulSoup(r.content, features="html.parser")
    result = soup_object.find_all('p')
    with open(output_filename, 'w') as ofile:
        for tag in result:
           ofile.write(str(tag)+'\n')

def find_links(url, output_filename):
    "*** YOUR CODE HERE ***"
    r = requests.get(url)
    soup_object = bs4.BeautifulSoup(r.content, features="html.parser")
    links = soup_object.find_all('a')
    
    with open(output_filename, 'w') as ofile:
      for link in links:
       ofile.write(link.get('href')+'\n')
threads = []

for i in range(5):
 threads.append(threading.Thread(target=callOtherFunctions))
start_time = time.time()

for thread in threads:
  thread.start()
for thread in threads:
  thread.join
# callOtherFunctions()
elapsed = time.time() - start_time
print (elapsed)   





