def create_division (x):
    def division (n):
        return x/n 
    return division

w = create_division (2)
print (w(2))