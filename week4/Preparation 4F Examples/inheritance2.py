class ClassA:
    static_var = 1;
    
    def __init__(self):
        print "Initializing A"
        self.instance_var = 2;        
        




class ClassB(ClassA):
    def __init__(self):
        print "Initializing B"
        # This is new --
        try:
            super(ClassB,self).__init__()
        except:
            print "This is an old style class. Can't use super."
        # -- this was new
        





def main():
    
    b = ClassB()
    print "b.static_var =",b.static_var
    try: 
        print "b.instance_var =",b.instance_var
    except:
        print "b has no instance variable instance_var"      

if __name__ == "__main__":
    main()