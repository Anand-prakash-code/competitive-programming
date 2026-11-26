def print_info (**kwargs):
    # You do not put ** in kwargs.items() because ** is only the packing/unpacking operator used in the function header (def print_info(**kwargs):), while the actual dictionary variable created inside the function is named simply kwargs. .do not put put ** in front of kwargs inside the function body, Python tries to unpack the dictionary again instead of reading it, which causes a SyntaxError or TypeError.
    #items() is  inbuilt into Python . kwargs is received as a dict: {'name': 'Alice', 'role': 'Developer'}
   for topic ,info in kwargs.items(): 
     print (f"{topic}: {info}")


print_info( name ="alice", role ="cybersecurity",age =23)

#name: alice
#role: cybersecurity
#age: 23