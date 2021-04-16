import copy

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return repr(self.data)
        
# class LinkedList:
#     def __init__(self, data):
#         self.node = Node(data)
#         self.first = self.node
#         self.last = self.node
#         self.n = 1

#     def append(self, data):
#         newNode = Node(data)
#         self.last.next = newNode
#         self.last = newNode
#         self.n += 1

#     def __iter__(self):
#         self.node = self.first
#         return self

#     def __next__(self):
#         if self.node == None:
#             raise StopIteration
#         node = self.node
#         self.node = self.node.next
#         return node.data

class LinkedList:
    def __init__(self, data):
        self.node = Node(data)
        self.first = self.node
        self.last = self.node
        self.n = 1
        self.__values = [self.node]
        

    def append(self, data):
        newNode = Node(data)
        self.last.next = newNode
        self.last = newNode
        self.n += 1
        self.__values.append(newNode)

    def __str__(self):
        result = "["

        for node in self.__values:
            result = result + str(node) + "->"

        result = result + "]"
        return result

    def __repr__(self):
        result = "["

        for node in self.__values:
            result = result + str(node) + "->"

        result = result + "]"
        return "'" + result + "'"

    def __add__(self, value):
        first_element = self.__values[0]
        copy = LinkedList(first_element)
        for node in self.__values[1:]:
            copy.append(node)
        copy.append(value)
        return  copy

        
    def __len__(self):
         return self.n

    def __iter__(self):
        return self.generator()

    def generator(self):
        self.node = self.first
        for _ in range(0, self.n):  
            yield self.node.data
            self.node = self.node.next

    def __getitem__(self, index):
        if index < 0:
            raise IndexError("list index out of range")
        elif index >= self.n:
            raise IndexError("list index out of range")
        return self.__values[index]

    def __setitem__(self, index, value):
        if index < 0:
            raise IndexError("list index out of range")
        elif index >= self.n:
            raise IndexError("list index out of range")
        self.__values[index] = value
        
        


# a = LinkedList(0)
# a.append(1)
# a.append(2)





# a + 1 

# print(str(a))

# a = a + 1

# print(str(a))



