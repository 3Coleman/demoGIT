# # # class employee:
# # #     def __init__(self,name,salary):
# # #         self.name=name
# # #         self.salary=salary
# # #     def __eq__(self, other):
# # #         return self.salary==other.salary
# # #     def __gt__(self, other):
# # #         return self.salary>other.salary
# # #
# # #     def __lt__(self, other):
# # #         return self.salary<other.salary
# # #
# # # emp1=employee("Nikhil","10000")
# # # emp2=employee("Abel","12000")
# # # print(emp1==emp2)
# # # print(emp1>emp2)
# # # print(emp1<emp2)
# #
# #
# # # class School:
# # #     def __init__(self,m1,m2,m3):
# # #         self.m1=m1
# # #         self.m2=m2
# # #         self.m3=m3
# # #     def avg(self):
# # #         return((self.m1+self.m2+self.m3)/3)
# # #
# # #     def get_m1(self):
# # #         return self.m1
# # #
# # #     def set_m2(self,value):
# # #         self.m2=value
# # #
# # # s1=School(10,12,13)
# # # s2=School(20,17,20)
# # # s2.set(50)
# # # print(s1.get_m1())
# # # print(s2.avg())
# #
# # # class Students:
# # #     school="Telusko"
# # #     def __init__(self,m1,m2,m3):
# # #         self.m1=m1
# # #         self.m2=m2
# # #         self.m3=m3
# # #
# # #     def avg_mark(self):
# # #         return (self.m1+self.m2+self.m3)/3
# # #
# # #
# # #     @classmethod
# # #     def getschool(cls):
# # #         return cls.school
# # #
# # #     @staticmethod
# # #     def info():
# # #         print("this is 'Student' class ")
# # #         print(12%5)
# # #
# # # s1=Students(12,13,14)
# # # s2=Students(11,14,17)
# # #
# # # print(s2.avg_mark())
# # # print(Students.getschool())
# # # Students.info()
# # #
# # # class student:
# # #     def __init__(self,name,rollno):
# # #         self.name=name
# # #         self.rollno=rollno
# # #
# # #     def show(self):
# # #         print(self.name,self.rollno)
# # #     class laptop:
# # #         def __init__(self):
# # #             self.brand="lenova"
# # #             self.cpu="intel"
# # #             self.ram=16
# # # s1=student("Akhil",6)
# # # s2=student("Amal",7)
# # # s1.show()
# # # s2.show()
# # # lap1=s1.laptop()
# # # lap1.ram()
# #
# #
# # # class collage:
# # #     def __init__(self):
# # #         print("outer class constructor")
# # #     class student:
# # #         def __init__(self):
# # #             print("inner class constructor")
# # #         def id(self):
# # #             print("inner class student id ")
# # #     def adress(self):
# # #         print("outer class collage adress")
# # # c=collage()
# # # c.adress()
# # # s=collage.student()
# # # s.id()
# # class A:
# #     def f1(self):
# #         print("feature1 of A")
# #     def f2(self):
# #         print("feature2 of A")
# # class B(A):
# #     def f3(self):
# #         print("feature3 of B")
# #     def f4(self):
# #         print("feature4 of B")
# # object1=A()
# # object2=B()
# # object1.f1()
# # object1.f2()
# # object2.f1()
# # object2.f2()
# # object2.f3()
# # object2.f4()
# #
# # class A:
# #     def f1(self):
# #         print("feature1 of A")
# #     def f2(self):
# #         print("feature2 of A")
# # class B(A):
# #     def f3(self):
# #         print("feature3 of B")
# #     def f4(self):
# #         print("feature4 of B")
# # class C(B):
# #     def f5(self):
# #         print("feature3 of B")
# # object1=A()
# # object2=B()
# # object3=C()
# # object3.f1()
# # object3.f3()
# # class A :
# #     def __init__(self):
# #         print("init classA")
# #     def f1(self):
# #         print("f1 of classA")
# # class B():
# #     def __init__(self):
# #         print("init classB")
# #     def f1(self):
# #         print("f1 of B")
# # class C(A,B):
# #     def __init__(self):
# #         super().__init__()
# #         print("init of C")
# # object1=C()
# # object1.f1()
# #
# #
# #
# # class DUCK:
# #     def sound(self):
# #         print("quack quack")
# # class DOG:
# #     def sound(self):
# #         print("woah woah ")
# # class CAT:
# #     def sound(self):
# #         print("MEOW MEOW")
# # def all_sound(obj):
# #     obj.sound()
# # x=DUCK()
# # all_sound(x)
# #
# #
# # x=5
# # x="abel"
# # print(type(x))
# #
# # class DOG:
# #     def sound(self):
# #         print("bark")
# # class COW:
# #     def sound(self):
# #         print("maa mama")
# # def ob(obj):
# #     obj.sound()
# #
# # x=COW()
# # y=
# # ob(x)
# #
# #
# #
# #
# #
# #
# # class student:
# #     def __init__(self,m1,m2):
# #         self.m1=m1
# #         self.m2=m2
# #     def __add__(self, other):
# #         m1=self.m1+other.m1
# #         m2=self.m2+other.m2
# #         s3=student(m1,m2)
# #         return s3
# # s1=student(12,14)
# # s2=student(13,16)
# # s3=s1+s2
# # print(s3.m2)
# #
# # class student:
# #     def __init__(self,m1,m2):
# #         self.m1=m1
# #         self.m2=m2
# #     def __gt__(self, other):
# #         s1mark=self.m1+self.m2
# #         s2mark=other.m1+other.m2
# #         if s1mark>s2mark:
# #             True
# #         else:
# #             False
# #
# # s1=student(40,44)
# # s2=student(41,39)
# # if s1>s2:
# #     print("s1 wins")
# # else :
# #     print("s2 wins")
# #
# #
# #
# # method overloading
# # #
# # class A :
# #     def phone(self):
# #         print("i owns nokia 11 phone")
# # class B(A):
# #     def phone(self):
# #         print("i owns i phone")
# # p1=B()
# # p1.phone()
# #
# # from abc import ABC,abstractmethod
# #
# # class computer(ABC):
# #     @abstractmethod
# #     def process(self):
# #         pass
# # class laptop(computer):
# #     def process(self):
# #         print("lenova laptop")
# # class mobile(computer)
# #     def process(self):
# #         print("motorola")
# # com1=computer()
# # com1.process()
# # from abc import ABC,abstractmethod
# # class animal(ABC):
# #     @abstractmethod
# #     def move(self):
# #         pass
# #     def print1(self):
# #         print("im an animal")
# # class snake(animal):
# #     def move(self):
# #         print("i can crawl...")
# #     def walk(self):
# #         print("i can walk")
# # class human(animal):
# #     def move(self):
# #         print("i can walk and run..")
# #
# # s1=snake()
# # s1.move()
# # s1.walk()
# # s1.print1()
# # h1=human()
# # h1.move()
# # a1=animal()
# # a1.print1()
# # list=[1,2,3,4,5]
# # for i in list:
# #     print(i)
# # my_object=["edureka","python","iterator"]# my_object  is the iterable object
# # my_object_iterator=iter(my_object)
# # print(next(my_object_iterator))
# # print(next(my_object_iterator))
# # print(next(my_object_iterator))
# # list=[1,2,3,4,5]
# # list_itera=iter(list)
# # print(next(list_itera))
# # class top10:
# #     def __init__(self):
# #         self.count=1
# #     def __iter__(self):
# #         return self
# #     def __next__(self):
# #         if self.count<=10:
# #             val=self.count
# #             self.count+=1
# #             return val
# #         else:
# #             raise StopIteration
# #
# # values=top10()
# # for i in values:
# #     print(i)
# #
# # class top10:
# #     def __init__(self):
# #         self.value=1
# #     def __iter__(self):
# #         return self
# #     def __next__(self):
# #         if value1 <= 10:
# #             value1=self.value
# #             self.value+=1
# #             return value1
# #         else:
# #             raise StopIteration
# # value2=top10()
# # for i in value2:
# #     print(i)
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # class top10:
# #     def __init__(self):
# #         self.counter=1
# #     def __iter__(self):
# #         return self
# #     def __next__(self):
# #         if self.counter<=10:
# #             variable=self.counter
# #             self.counter+=1
# #             return variable
# #         else :
# #             raise StopIteration
# # OB1=top10()
# # for i in OB1:
# #     print(i)
# #
# #
# # def top10():
# #     yield 1
# #     yield 2
# #     yield 3
# #     yield 4
# #
# # for i in top10():
# #     print(i)
# # import sys
# # x=[1,2,3,4]
# # y=map(lambda i:i**2,x)
# # print(y)
# # for k in y:
# #     print(k)
# # print(sys.getsizeof(list(y)))
# #
# # def top10():
# #     k=1
# #     while k<=10:
# #         s=k*k
# #         return s
# #         k+=1
# # for i in top10():
# #     print(i)
# #
# # class top10:
# #     def __init__(self):
# #         self.counter=1
# #     def __iter__(self):
# #         return self
# #     def __next__(self):
# #         if self.counter<=10:
# #             k=self.counter
# #             return k
# #             self.counter+=1
# #         else:
# #            raise StopIteration
# # ob=top10()
# # for a in ob:
# #     print(a)
# #
# # class top10:
# #     def __init__(self):
# #         self.counter=1
# #     def __iter__(self):
# #         return self
# #     def __next__(self):
# #         if self.counter<=10:
# #             variable=self.counter**2
# #             self.counter+=1
# #             return variable
# #         else :
# #              raise StopIteration
# # OB1=top10()
# # for i in OB1:
# #     print(i)
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # class top10:
# #     def __init__(self):
# #         self.counter=1
# #     def __iter__(self):
# #         return self
# #     def __next__(self):
# #         if self.counter<=10:
# #             x=self.counter*2
# #             self.counter += 1
# #             return x
# #
# #         else :
# #             raise StopIteration
# # ob=top10()
# # for i in ob:
# #     print(i)
# #
# #
# # def generator():
# #     count=1
# #     while count<=10:
# #         k=count**2
# #         count+=1
# #         yield k
# # for i in generator():
# #     print(i)
# #
# #
# #
# #
# #
# #
# # from threading import*
# # from time import sleep
# # class Hello(Thread):
# #     def run(self):
# #         for i in range(5):
# #             print("Hello")
# #             sleep(1)
# # class Hi(Thread):
# #     def run(self):
# #         for i in range(5):
# #             print("Hi")
# #             sleep(1)
# # ob1=Hello()
# # ob2=Hi()
# # ob1.start()
# # sleep(0.2)
# # ob2.start()
# # ob1.join()
# # ob2.join()
# # print("the end ")
# #
# #
# #
# #
# #
# #
# # from threading import*
# # from time import sleep
# # class A(Thread):
# #     def run(self):
# #         for i in range (5):
# #             print("RunA")
# #             sleep(1)
# # class B(Thread):
# #     def run(self):
# #         for i in range(5):
# #             print("RunB")
# #             sleep(1)
# #
# # obA=A()
# # obB=B()
# # obA.start()
# # sleep(0.5)
# # obB.start()
# # obA.join()
# # obB.join()
# # print("the end")
# #
# #
# # f=open('file_handle1','r')
# #
# # print(f.readline(),end="")
# # print(f.readline(),end="")
# # print(f.readline())
# #
# # f1=open("abc","a")
# # f1.write("PC")
# #
# # f=open("leave1.jpg","rb")
# # f1=open("angel.png","wb")
# # for i in f:
# #     f1.write(i)
# #
# # f=open("file_handle1","r")
# # print(f.readline(),end="")
# # print(f.readline())
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # a=open("leave1.jpg","rb")
# # b=open("abell.jpg","wb")
# # for i in a:
# #     print(b.write(i))
#
# # def search(list,n):
# #     list = [1, 2, 3, 4, 5]
# #     n = 5
# #     i=0
# #     while i <len(list):
# #         if list(i)==n:
# #             return True
# #         i=i+1
# #     return False
# #
# #
# # if search(list,n=5):
# #     print("found")
# # else :
# #     print("not found")
#
# #linear search
# # def search (list,key):
# #     flag=False
# #     list1=[]
# #     for i in range(len(list)):
# #         if key==list[i]:
# #             flag=True
# #             list1.append(i)
# #     if flag==True:
# #         print("key element is found in index no's:")
# #         for i in list1:
# #             print(i)
# #     else:
# #         print("element is not found")
# # list=[34,23,5,6,7,1,23,8,34]
# # key=int(input("Enter the key element :"))
# # search(list,key)
#
#
#
#
#
#
#
#
#
#
# # def search(list,key):
# #     flag=False
# #     list2=[]
# #     for i in range (len(list)):
# #         if list[i]==key:
# #             flag=True
# #             list2.append(i)
# #     if flag==True:
# #         print("Found the name  in list at index no: ")
# #         for i in list2:
# #             print(i)
# #
# #     else:
# #         print("Not found the name ")
# # list=["abel","akhil","ajmal","aswanth","abel"]
# # key=input("enter a name you want :")
# # search(list,key)
#
#
#
#
#
#
#
#
#
#
# # def binary_search (list,key):
# #     low=0
# #     high=len(list)-1
# #     found=False
# #
# #     while low<=high and  not found:
# #         mid = (low + high) // 2
# #         if key==list[mid]:
# #             found=True
# #         elif key>list[mid]:
# #             low=mid+1
# #         else:
# #             high=mid-1
# #     if found==True:
# #         print("key is found ")
# #     else:
# #         print("key isnt found ")
# #
# #
# #
# # # list=[23,1,4,2,3]
# # num=int(input("enter the list length : "))
# # list=[int(input()) for i in range(num)]
# # list.sort()
# # print(list)
# # key =int(input("enter the key : "))
# # binary_search(list,key)
#
#
#
#
#
# def search(list,key):
#     low=0
#     high=len(list)-1
#
#     found=False
#     while low<=high and not found:
#         mid = (low + high) // 2
#         if key==list[mid]:
#             found=True
#         elif key>list[mid]:
#             low=mid+1
#         else:
#             high=mid-1
#     if found==True:
#         print("the key is found")
#     else:
#         print("key isnt there ")
#
#
#
#
# length=int(input("enter the length of the list :"))
# list=[int(input())for i in range(length)]
# list.sort()
# print(list)
# key=int(input("enter the key: "))
# search(list,key)
#
#
#
#
#
#
#
#
#
#
# import mysql_test.connector
# mydb = connect()
import mysql.connector

my_db= mysql.connector.connect(host='localhost' ,user='root' ,password='Intel@3105')

