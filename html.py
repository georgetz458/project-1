# -*- coding: utf-8 -*-
#Άσκηση 10
#εισαγωγη βιβλιοθήκης
import urllib.request
#αίτηση απόκτησης πηγαίου κώδικα
x = input("Give a site: ")
html_file = urllib.request.urlopen(x)
a = html_file.readlines()
link = 0
lines = 0
for line in a:
    #σε κάθε γραμμή to string αποκωδικοποιήται σε utf-8
    line = line.decode("UTF-8")
        #σε κάθε γραμμή ελένχει εαν εχει σύνδεσμο και αποθηκεύει το σύνολο του πλήθους αυτού
    if '</a>' in line:
        link += 1
    #σε κάθε γραμμή ελένχει εαν εχει αλλαγή γραμμής και αποθηκεύει το σύνολο του πλήθους αυτού
    if '<br>' or '</div>' or '</p>' in line:
        lines += 1
#εκτθπώνει το πλήθος των συνδέσμων και αλλαγών γραμμών
print("The number of links are: ", link)
print("The number of lines are: ", lines)
