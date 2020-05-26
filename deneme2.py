import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


books = pd.read_csv('BX-Books.csv', sep=';', error_bad_lines=False, encoding="latin-1")
books.columns = ['ISBN', 'bookTitle', 'bookAuthor', 'yearOfPublication', 'publisher', 'imageUrlS', 'imageUrlM', 'imageUrlL']
users = pd.read_csv('BX-Users.csv', sep=';', error_bad_lines=False, encoding="latin-1")
users.columns = ['userID', 'Location', 'Age']
ratings = pd.read_csv('BX-Book-Ratings.csv', sep=';', error_bad_lines=False, encoding="latin-1")
ratings.columns = ['userID', 'ISBN', 'bookRating']


#rating dağılım grafiği 
plt.rc("font", size=15)
ratings.bookRating.value_counts(sort=False).plot(kind='bar')
plt.title('rating dağılımı\n')
plt.xlabel('rating')
plt.ylabel('count')
plt.savefig('system2.png', bbox_inches='')
plt.tight_layout()
plt.show()

#yaş dağılım grafiği
users.Age.hist(bins=[0,10,20,30,40,50,100])
plt.title('yaş dağılımı\n')
plt.xlabel('age')
plt.ylabel('count')
plt.savefig('system2.png',bbox_inches='tight')
plt.tight_layout()
plt.show()

#books ve rating dosyalarını birleştirdik
combine_book_rating=pd.merge(ratings,books,on='ISBN')
columns = ['ISBN','bookAuthor', 'yearOfPublication', 'publisher', 'imageUrlS', 'imageUrlM', 'imageUrlL']
combine_book_rating['bookTitle']=books.bookTitle
combine_book_rating['rating'] = ratings.bookRating
combine_book_rating = combine_book_rating.drop((columns),axis=1)
print(combine_book_rating.rating.head())


#k-nn en yakın komşu algoritmasından yola çıkarak çok daha basit mantıkla öneri oluşturur.

x= input('istediğiz kitap önerilerinin hangi ratingi barındırması gerektigini belirtiniz: ')
print(x)



# öneri kitapları veriyor
newRate = combine_book_rating[(combine_book_rating['rating']>int(x))&(combine_book_rating['rating']<=int(x)+1)][['bookTitle','rating']].head()
print(newRate)


