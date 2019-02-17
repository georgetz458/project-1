# -*- coding: utf-8 -*-
#python 3.v
#Άσκηση 11
#εισαγωγη βιβλιοθήκης
import random
#άνοιγμα αρχείου
fin = open("text.txt","r")
#διάβασμα κάθε γραμμής και μετατροπη από list σε string
data = fin.readlines()
d = str(data)
#αντικατάσταση του \\n με κενό ώστε να εξαφανιστεί
b= d.replace("\\n","")
a = b.split()
fin.close()
# Δημιουργεία συνάρτησης που δημιουργηται ενα generator απο 0εωτ το μήκος της λίστας ώστε να απωθηκευτούν οι τριλαδες λέξεων με επικάλιψη
def chunks(l):
 for i in range(0, len(l)):
     yield a[i:i+3]
#μετατροπη τou chunks από generator σε string
x = list(chunks(a))
#ανακάτεμα των τριάδων
random.shuffle(x)
#μετατροπή του χ σε string
l = str(x)
#απομάκρυνση συμβόλων
l = l.replace("[","")
l = l.replace("]","")
l = l.replace(",","")
l = l.replace('''"''',"")
l = l.replace("'","")
#προσθήκη τελείας στο τέλος της πρότασης
l = l + "."
#εκτ΄ύποση τυχαίου κειμένου
print(l)
