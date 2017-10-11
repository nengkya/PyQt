class StringList(list):
    def __init__(self):
        self.data = []

    def __repr__(self):
        return str(self.data)

    #override metode append()
    def append(self, objek):
        if not isinstance(objek, str):
            raise TypeError('Objek harus bertipe string')
        self.data.append(objek)

    #override metode insert()
    def insert(self, indeks, objek):
        self.data.insert(indeks, objek)


#membuat objek dari kelas StringList (pewarisan)
slist = StringList()

#menambahkan data menggunakan metode append()
slist.append('Python')

print(slist)
slist.insert( 2, 'Perl')
print(slist)
slist.insert(-2, 'Java')
print(slist)
slist.insert(-2, 100)
print(slist)
