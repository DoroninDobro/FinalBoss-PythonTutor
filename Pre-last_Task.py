def height(man):
    if man not in p_tree:
        return 0
    else:
        return 1 + height(p_tree[man])

p_tree = {}
n = int(input())
for i in range(n - 1):
    child, parent = input().split()
    p_tree[child] = parent

heights = {}
for man in set(p_tree.keys()).union(set(p_tree.values())):
    heights[man] = height(man)

# for key, value in sorted(heights.items()):
#     print(key, value)
#It is delete from first task
def is_it_parent(nam1,nam2):
    val1=int(heights[nam1]) #1
    val2=int(heights[nam2]) #4
    parents = set()
    for key in p_tree:
        if p_tree[key]==nam1:
            parents.add(key)
    if val2-val1 == 1:
        massiv = {nam2}
        if massiv <= parents:
            return True
        else:
            return False
    else:
        for Name in parents:
            if is_it_parent(Name, nam2) == True:
                return True
            
            





def otvet(name1, name2):
    val1=int(heights[name1])
    val2=int(heights[name2])
    if val1==0:
        return 1
    if val2==0:
        return 2
    if val1<val2:
        x=1
        if is_it_parent(name1,name2)==True:
            return x
        else:
            return 0
    elif val2<val1:
        x=2
        if is_it_parent(name2,name1)==True:
            return x
        else:
            return 0
    else:
        x=0
        return x
    


m=int(input())
for _ in range(m):
    s=input().split()
    x=otvet(s[0],s[1])
    print(x,end=' ')

# OHCMZSSM OVBOHOGAWQ
# OHCMZSSM RRJHDOUTF  gives 0, but must 1




'''Условие
Даны два элемента в дереве. Определите, является ли один из них потомком другого.

Во входных данных записано дерево в том же формате, что и в предыдущей задаче Далее идет число запросов K. В каждой из следующих K строк, содержатся имена двух элементов дерева.

Для каждого такого запроса выведите одно из трех чисел: 1, если первый элемент является предком второго, 2, если второй является предком первого или 0, если ни один из них не является предком другого.

Условие предыдущей задачи:
Условие
В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель.

Каждом элементу дерева сопоставляется целое неотрицательное число, называемое высотой. У родоначальника высота равна 0, у любого другого элемента высота на 1 больше, чем у его родителя.

Вам дано генеалогическое древо, определите высоту всех его элементов.

Программа получает на вход число элементов в генеалогическом древе N. Далее следует N−1 строка, задающие родителя для каждого элемента древа, кроме родоначальника. Каждая строка имеет вид имя_потомка имя_родителя.

Программа должна вывести список всех элементов древа в лексикографическом порядке. После вывода имени каждого элемента необходимо вывести его высоту.

Примечание

Эта задача имеет решение сложности O(n), но вам достаточно написать решение сложности O(n2) (не считая сложности обращения к элементам словаря).
'''

