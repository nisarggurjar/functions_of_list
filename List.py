class List:
    def Append(self,item):
        self.li = self.li + [item]

    def __init__(self, *argv):
        self.li  = list()
        for i in argv:
            self.li = self.li + [i]

    def Index(self, item):
        c = 0
        for i in self.li:
            if i == item:
                return c
            c +=1

    def Clear(self):
        self.li = []

    def Count(self,item):
        c = 0
        for i in self.li:
            if i == item:
                c +=1
        return c

    def Show(self):
        print(self.li)

    def Extend(self, list2):
        self.li = self.li + list2
        return self.li

    def Insert(self, index, item):
        nlist = []
        i = 0
        for e in self.li:
            if i < index:
                nlist =  nlist + [e]
                i += 1
            elif i == index:
                nlist =  nlist + [item]
                nlist =  nlist + [e]
                i += 1
            elif i > index:
                nlist =  nlist + [e]
                i += 1
        self.li = nlist

    def Copy(self):
        l = []
        for i in self.li:
            l = l + [i]
        return l

    def Remove(self, item):
        l = list()
        for i in self.li:
            if i == item:
                pass
            else:
                l = l + [i]
        self.li = l

    def Pop(self,*argv):
        if argv is ():
            t = self.li[-1]
            self.li = self.li[0:-1]
        else:
            t = self.li[argv[0]]
            ele = self.li[argv[0]]
            self.Remove(ele)
        return t

    def Sort(self):
        for i in range(1,len(self.li)):
            j = i - 1
            nxt_ele = self.li[i]
            while (self.li[j] > nxt_ele) and (j>=0):
                self.li[j+1] = self.li[j]
                j = j-1
            self.li[j+1] = nxt_ele

    def Reverse(self):
        start = 0
        end = len(self.li)-1
        while start < end:
            self.li[start], self.li[end] = self.li[end], self.li[start]
            start = start + 1
            end = end - 1
