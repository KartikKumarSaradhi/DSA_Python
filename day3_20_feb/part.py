def fun(a):
    if(a==0):
        return
    fun(a-1)
    print(a)
    fun(a-1)
fun(3)