
maxa=5
maxb=4
visited=[]
queue=[]
start=(0,0)
final=(2,0)
tree={}
def filla(a,b):
    return (maxa,b)
def fillb(a,b):
    return (a,maxb)
def emptya(a,b):
    return (0,b)
def emptyb(a,b):
    return (a,0)
def pourab(a,b):
    if a+b<=maxb:
        return (0,a+b)
    else:
        return (a-(maxb-b),maxb)
def pourba(a,b):
    if a+b<=maxa:
        return (a+b,0)
    else:
        return (maxa,b-(maxa-a))

def getchildren(a,b):
    children=[]
    if filla(a,b)!=(a,b) and filla(a,b) not in children:
        children.append(filla(a,b))
    if fillb(a,b)!=(a,b) and fillb(a,b) not in children:
        children.append(fillb(a,b))
    if  emptya(a,b)!=(a,b) and emptya(a,b) not in children:
        children.append(emptya(a,b))
    if  emptyb(a,b)!=(a,b) and emptyb(a,b) not in children:
        children.append(emptyb(a,b))
    if  pourab(a,b)!=(a,b) and pourab(a,b) not in children:
        children.append(pourab(a,b))
    if  pourba(a,b)!=(a,b) and pourba(a,b) not in children:
        children.append(pourba(a,b))
    return children

while start!=final:
    if start not in visited:
        visited.append(start)
        children=getchildren(start[0],start[1])
        tree[start]=children
        queue.extend(children)
    start=queue[0]
    queue.pop(0)
path=[]
print(visited)
start=(0,0)
temp=final
visited.reverse()
for i in visited:
    if temp==start:
        visited.append(start)
        break
    if temp in tree[i]:
        path.append(i)
        temp=i
path.insert(0,final)
print("Path ",path[::-1])

