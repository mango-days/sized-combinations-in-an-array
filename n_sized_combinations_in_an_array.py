array=[1,2,3,4,5,6,7,8,9,0]
visited=[0,0,0,0,0,0,0,0,0,0]
size=7
ans=[]
def combination():
    if len(ans)==size:
        print (ans)
        return
    for i in range (0, len(array)):
        if visited[i]==0:
            visited[i]=1
            ans.append(array[i])
            combination()
            ans.pop()
            visited[i]=0
combination()