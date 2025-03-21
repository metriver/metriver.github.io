---
title: Title
date: YYYY-MM-DD
tags: [tag1,]
---

# Language C Notes
## c语言基础知识
```c
#include <stdio.h>

int main(){
	strcmp(a,b);//比较a,b 的字典序

	
	int *q[5];//数组指针  
	// 一个指向具有5个整形元素的一维数组的指针
	// 对其初始化时 类似这样={&a[1],&a[2],....}

	int (*q)[5];//指针数组
	// 具有5个指针元素的一维指针数组

	++ 的运算级别低于 ->
	
	}

```

```c
int main(){
	fscanf(FILE *stream/*文件指针*/,""格式化字符串,输入列表);
	
	
	// 一个文件使用前后必须进行打开和关闭
	fopen()
	FILE *fopen(char* filename,*type);
	type=r(只读)w(写)

	fclose()
```

```c
qsort(首地址,num,sizeof(),cmp);
当要对结构体中某一 字符串/数字 排序
eg
	struct a_struct a[n];
	qsort(a,n,sizeof(a_struct),cmp);
	在cmp中类型转换依然转化为数组；
	比较时用 ->访问数组元素
	
```

## 数据结构
### 链表
#### 单向链表
1.定义节点
```c
typedef struct Node {
	int data;
	struct Node* next;
} Node;
```

2.初始化链表
```c
Node *initlist(){
	Node* head = (Node*)malloc(sizeof(Node));
	head -> next = NULL;	
	return head;
}
```

创建了一个头节点head，这个头节点即代表着这个链表的首地址。

其既可以充当链表中的元素，

也可以仅仅作为一个指针引出链表。

3.添加节点
```c
void addNode(Node* head,int data){
	Node* temp = (Node*)malloc(sizeof(Node));
	temp->data = data;
	temp->next = NULL;
	//  find the last node of list
	Node* cur = head;
	while(cur->next != NULL)
	{
		cur = cur->next;
	}
	// add new node to rear
	cur->next = temp;
}
```

4.删除节点

```c
void delNode(Node* head,int data)
{
	if(head == NULL || head->next == NULL)
		return;	//dont delete null or just head

	// speacial:delete head
    if (head->data == data) {
        Node* temp = head;
        head = head->next;  
        free(temp);  
        return;
    }	
	Node* cur = head;
	while(cur->next != NULL && cur ->next->data !=data){
		 cur = cur->next;
	}
	if(cur->next == NULL){
		return;
	}
	Node* temp = cur->next;
	cur->next = temp->next;
	free(temp);
}
```

5.查找节点

```c
Node* findNode(Node* head, int data) {
    Node* cur = head->next; // 从头节点的下一个节点开始遍历
    while (cur != NULL && cur->data != data) {
        cur = cur->next;
    }
    return cur; // 如果找到目标节点，返回该节点；否则返回NULL
}

```