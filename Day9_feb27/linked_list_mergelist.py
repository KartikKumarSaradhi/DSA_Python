class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class List:
    def insert(self,head,data):
        newnode=Node(data)
        if(head==None):
            head=newnode
            return head
        else:
            temp=head
            while(temp.next!=None):
                temp=temp.next
            temp.next=newnode
            return head
    def merge(self,head1,head2,head3):
        while(head1!=None  and head2!=None):
            if(head1.data<=head2.data):
                head3=ob.insert(head3,head1.data)
                head1=head1.next
            else:
                head3=ob.insert(head3,head2.data)
                head2=head2.next               
        if(head1!=None):
            while(head1!=None):
                head3=ob.insert(head3,head1.data)
                head1=head1.next
        else:
            while(head2!=None):
                head3=ob.insert(head3,head2.data)
                head2=head2.next
        ob.display(head3)
    def display(self,head):
        while(head!=None):
            print(head.data)
            head=head.next
    def nthnode(self,h,n):
        c=0
        temp=h
        while(temp!=None):
            temp=temp.next
            c+=1
        c=c-n
        while(c>0):
            h=h.next
            c-=1
        print("nth node from last",h.data)
ob=List()
head1=None;head2=None;head3=None
list1=[0,1,2,3,10]
list2=[1,5,6]
for i in list1:
    head1=ob.insert(head1,i)
for i in list2:
    head2=ob.insert(head2,i)
#ob.display(head1)
ob.merge(head1,head2,head3)
n=2
ob.nthnode(head1,n)