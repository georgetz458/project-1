# -*- coding: utf-8 -*-
#Άσκηση 9
def sub_lists(my_list):
	subs = []
    #λουπα από 0 εωτ το μηκος της λιστας
	for i in range(len(my_list)):
		n = i+1
        #αλλη λουπα μεχρι το μηκος της λιστας
		while n <= len(my_list):
            #δημιουργεία λίστας απο το ι μεχρι το ν δηλ σημιουργούνται όλες οι πιθανές υπολίστες
			sub = my_list[i:n]
            #προσθέτω τις υπολίστες σε μια λίστα
			subs.append(sub)
			n += 1
	return subs
list = [-2, 1,-3, 4,-1,2,1,-5,4]
l=sub_lists(list)
def maxSequence(l):
    max1 = 0
    # λούπα  (όπου χ η υπολίστα) μεσα στη λιστα για την εύρεση αθροισμάτων
    for x in l:
        sum = 0
        # συγκριση των αθροισμάτων
        for y in x:
            sum+= y
        max1 = max(sum, max1)
    return max1
print (maxSequence(l))
