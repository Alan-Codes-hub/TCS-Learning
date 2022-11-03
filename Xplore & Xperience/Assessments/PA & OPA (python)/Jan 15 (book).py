class Book():
    def __init__(self,book_id,book_name):
        self.book_id=book_id
        self.book_name=book_name

class Library():
    def __init__(self,Library_id,Address,book_list):
        self.Library_id=Library_id
        self.Address=Address
        self.book_list=book_list

    def books_count(self,chara):
        occ=0
        self.chara=chara
        for i in book_list:
            if i.book_name.startswith(chara):
                occ+=1
        return occ


    def delete_books(self,del_list):
        temp=[]
        self.del_list=del_list
        for j in book_list:
            if j.book_name in del_list:
                book_list.remove(j)
        return book_list




if __name__=='__main__':
    book_list=[]
    del_list=[]
    count=int(input())
    for c in range(count):
        book_id=int(input())
        book_name=input()
        obj=Book(book_id,book_name)
        book_list.append(obj)
    chara=input()
    del_count=int(input())
    for d in range(del_count):
        del_name=input()
        del_list.append(del_name)
    print("output:")
    demo_obj=Library(500023,"vasanth_Vihar",book_list)
    result=demo_obj.books_count(chara)
    print(result)
    result_list=demo_obj.delete_books(del_list)
    for b in result_list:
        print(b.book_name)
