class node:

    def __init__(self,x,y)
        self.x = x
        self.y = y

    class depot(node):
        def __init__(self,x,y):
            node.__init__(x,y)


    class customer(node):
        def __init__(self,x,y):
            node.__init__(x,y)