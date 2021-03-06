from subprocess import check_output
from os import pipe,write,close
def cargo(path,args=False):
    def to_string(l):
        s=""
        for i in l:
            s+=i+"\n"
        return s
    to_list=lambda s:s.split("\n")[:-1]
    if args==False:
        data=None
    else:
        data, temp = pipe() 
        write(temp, bytes(to_string(args), "utf-8")); 
        close(temp) 
    s = check_output("cd "+path+";cargo run", stdin = data, shell = True) 
    return to_list(s.decode("utf-8"))

#HOW TO USE:
#the first argument is the path
#the second is the list of arguments
"""
print(cargo("/home/parsa/AAA_RUST/hello_world",["a","b"]))
"""
#arguments can be ignored if there is no
"""
print(cargo("/home/parsa/AAA_RUST/hello_world"))
"""
#returns a list of strings
