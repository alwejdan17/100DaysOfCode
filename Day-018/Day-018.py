

#------------Create List---------
Books=["Python Programming","Introduction to Machine Learning","Introduction to Deep Learning"]
print("The list of Books\n",Books)
#------------1.Add items----------
Books.append("Introduction to Data Science")
Books.append("Introduction to Data Analysis")
print("\nNEW List after add items:\n",Books)
#------------2.Copy list----------
Books2=Books.copy()
print("\nList #2 :\n",Books2)
#------------3.Sort list----------
Books.sort()
print("\nBooks list#1 after sort:\n",Books)
#------------4.Pop last item from list#2----------
print("\nremoved item from List#2: \n",Books2.pop())
print("\nBooks list#2 after pop last item:\n",Books2)


