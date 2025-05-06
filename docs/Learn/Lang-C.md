
# C 语言笔记

## 零碎知识点

### 字符串赋值
```c
{
    char str1[] = "China"; // 正确
    // char str2[10]; strcpy(str2, "abcdefghijklmn"); // 错误：长度不匹配
    // char str3[10] = "abcdefghigklmn"; // 错误：长度不匹配
}

```
### 数组指针 / 指针数组
```c
{
    int *q1[5]; // 指针数组，q1 是一个数组，数组里是指向 int 的指针
    // 初始化示例：{ &a[1], &a[2], ... }
    // 等价写法：
    int *(q1_equiv[5]);

    int (*q2)[5]; // 数组指针，q2 是一个指针，指向含有 5 个 int 元素的一维数组
}
```

### 运算符优先级
```c
{
    ++的运算级别低于->;
}
```

---

### 文件处理
```c
// 使用文件前后必须进行打开和关闭
{
    FILE *fopen(char *filename, char *type);
    type = "r"(只读), "w"(写)

    FILE *in = fopen("xxx.txt", "r");

    // 常用的读取字符方式
    int ch;
    while ((ch = getchar()) != EOF)
    {
        // 处理字符
    }

    fclose(in);
}
```

---

### qsort 排序
```c
// qsort(首地址, 元素数量, 每个元素大小, 比较函数);

struct a_struct
{
    char name[20];
    int value;
} a[10];

// 示例调用
// qsort(a, 10, sizeof(struct a_struct), cmp);
// cmp 函数内需要进行类型转换为数组并使用 -> 访问字段
```

---

### 输入/输出总结
```c
{
    gets(arr); // 读入字符串 直至读到 回车
    puts(arr); //=printf("%s\n",arr)  //注意\n

    fgets(arr, 1005, stdin);
    fputs(arr, 1005, stdout);

    getchar();   // 读入一个字符  直至回车 但只有第一个 读入
    putchar(ch); // 输出一个字符 = printf("%c",ch)

    fscanf(FILE * stream, const char *format, [argument...]);
    fscanf(stdin, "%s", str); // 与fgets不同 这个读到空格就结束了 而不是回车

    printf("%9.2d", n); // 9-->场宽  .2-->小数点    -9 -->向左对齐
    // 超出场宽 以实际为主
    % 8s 同理 % 04d // 场宽前置 0 -->输出值前+0
}
```

---

### sscanf/sprintf
```c
{
    fgets(str, 1005, stdin);
    fgets(format, 1005, stdin);

    sscanf(str, format, s);
    // 将s以format的格式读入str
    // 按照format给出的格式 从str里面读取需要的东西 如字符串 数字...
    // eg:
    {
        strcpy(dtm, "Saturday March 25 1989");
        sscanf(dtm, "%s %s %d  %d", weekday, month, &day, &year);
    }

    sprintf
        // sprintf（format，"格式"，传入的数据）
        // 以某种形式将数据传入 多用于 转换为 字符串
        /*
        int a=123;
        sprintf(str,%d,a);
        puts(str);// 123
        */
        sprintf(format_p, "%%%d.%ds", k, x);
    printf(format_p, s); // 将format_p作为输出格式
    // 注意%%%d拆解为 %% (转义%) %d读入k；
}
```

---

### 处理重复元素
```c
// 排序后去重

// 先把数据排序
qsort(arr, n, sizeof(int), cmp); // cmp为比较函数
// 然后遍历数组，找到重复的元素并删除
int new_len = 0;
for (int i = 0; i < n; i++)
{
    if (i == 0 || arr[i] != arr[i - 1])
    {
        arr[new_len++] = arr[i]; // 保留不重复的元素
    }
}
```

---

### 读字符串将其中的数字字符转化为数字
```c
char str[100];
int num = 0;
for (int i = 0; str[i] != '\0'; i++)
{
    if (str[i] >= '0' && str[i] <= '9')
    {
        num = num * 10 + (str[i] - '0'); // 将字符转化为数字
    }
}
printf("%d\n", num); // 输出转换后的数字

// 如果是从stdin中读 ch是一个一个读的
// 比如 aaa 123 bbb 456
// 下面的代码可以处理  在for中会多读一个字符 用ungetc放回去
if (ch >= '0' && ch <= '9')
{
    for (data = 0; ch >= '0' && ch <= '9'; ch = getchar())
        data = data * 10 + (ch - '0');

    ungetc(ch, stdin);
}
```

### 表达式

中缀表达式 最常用

前缀表达式 从右往左 遇到数字压栈 遇到运算符 弹栈

后缀表达式 从左往右...

---

## 数据结构

### 单向链表
#### 1. 定义节点
```c
typedef struct Node
{
    int data;
    struct Node *next;
} Node;
```

#### 2. 初始化链表
```c
Node *initList()
{
    Node *head = (Node *)malloc(sizeof(Node));
    head->next = NULL;
    return head;
}
```

#### 3. 添加节点
```c
void addNode(Node *head, int data)
{
    Node *temp = (Node *)malloc(sizeof(Node));
    temp->data = data;
    temp->next = NULL;

    // 查找最后一个节点
    Node *cur = head;
    while (cur->next != NULL)
    {
        cur = cur->next;
    }

    // 添加新节点到末尾
    cur->next = temp;
}
```

#### 4. 删除节点
```c
void delNode(Node *head, int data)
{
    if (head == NULL || head->next == NULL)
        return; // 空链表或只有头节点

    // 特殊情况：删除头节点
    if (head->data == data)
    {
        Node *temp = head;
        head = head->next;
        free(temp);
        return;
    }

    Node *cur = head;
    while (cur->next != NULL && cur->next->data != data)
    {
        cur = cur->next;
    }

    if (cur->next == NULL)
    {
        return; // 未找到
    }

    Node *temp = cur->next;
    cur->next = temp->next;
    free(temp);
}
```

#### 5. 查找节点
```c
Node *findNode(Node *head, int data)
{
    Node *cur = head->next; // 从首节点后一个节点开始
    while (cur != NULL && cur->data != data)
    {
        cur = cur->next;
    }
    return cur; // 找到返回该节点，否则返回 NULL
}
```

---

### 栈

#### 顺序栈（多栈）
```c
#define MAXSIZE 100
typedef struct Stack
{
    int data[MAXSIZE];
    int top;
} Stack;

// 初始化栈
void initStack(Stack *s) { s->top = -1; }

// 判断栈是否为空
int isEmpty(Stack *s) { return s->top == -1; }

// 判断栈是否满
int isFull(Stack *s) { return s->top == MAXSIZE - 1; }

// 入栈
void push(Stack *s, int value)
{
    if (isFull(s)) return;
    s->data[++s->top] = value;
}

// 出栈
int pop(Stack *s)
{
    return isEmpty(s) ? -1 : s->data[s->top--];
}

// 获取栈顶元素
int peek(Stack *s)
{
    return isEmpty(s) ? -1 : s->data[s->top];
}
```

#### 单栈实现
```c
int stack[MAXSIZE];
int top = -1;

void push(int value) { stack[++top] = value; }
int pop() { return stack[top--]; }
int peek() { return stack[top]; }
int isEmpty() { return top == -1; }
int isFull() { return top == MAXSIZE - 1; }
```

---

### 队列

#### 循环队列
```c
int queue[MAXSIZE];
int front = 0;
int rear = MAXSIZE - 1;

void enqueue(int value)
{
    rear = (rear + 1) % MAXSIZE;
    queue[rear] = value;
}

int dequeue()
{
    front = (front + 1) % MAXSIZE;
    return queue[front];
}

int peekQueue() { return queue[(front + 1) % MAXSIZE]; }
int isQueueEmpty() { return front == rear; }
int isQueueFull() { return (rear + 1) % MAXSIZE == front; }
```

---

### 树

#### 0.性质&概念

- 非空二叉树(NEDT) 有n个节点 则有n-1个分支
- NEDT 第i层最多有 $ 2^{i-1} $个结点
- NEDT 深度h 最多有$2^h-1$个结点
- NEDT有n个叶结点,有N个度为2的结点,则 n=N+1
> 拓展:$ n_0 = \sum_{i=1}^m(m-1)n_m   \\m是bt的度 $
- NEDT n个结点 h=$[log_2^n]+1$(向下取整)
- 树转二叉树：兄弟节点连线；删除除左孩子外的所有结点连线
- 树林转二叉树：先把数量中的树转化为二叉树；再从最后的二叉树开始依次作为前一个树的右子树
- 哈夫曼树：特点：没有度为1的结点  构造最小带权路: 把权看作树林，每次把权最小的两棵树合成一个二叉树，权相加放回树林，重复操作
- 前序/后序遍历 定根节点 在中序遍历中找到该结点 左右分别为左右子树，重复操作
#### 1. 定义节点
```c
typedef struct TreeNode
{
    int data;
    struct TreeNode *left;
    struct TreeNode *right;
} TreeNode;
```

#### 2. 创建节点
有时候可以不单独列出 直接放在插入函数中构造newnode
```c
TreeNode *createNode(int data)
{
    TreeNode *newNode = (TreeNode *)malloc(sizeof(TreeNode));
    newNode->data = data;
    newNode->left = newNode->right = NULL;
    return newNode;
}
```

#### 3. 插入节点（二叉搜索树）
```c
TreeNode *insertBST(TreeNode *root, int data)
{
    if (!root) return createNode(data);
    if (root->data > data) root->left = insert(root->left, data);
    else root->right = insert(root->right, data);
    return root;
}
```

#### 4. 查找节点(BST)
```c
TreeNode *searchBST(TreeNode *root, int data)
{
    if (!root || root->data == data) return root;
    return search(data < root->data ? root->left : root->right, data);
}
```

#### 5.遍历方法
```c
// 前序遍历
void preOrder(TreeNode *root)
{
    if (root) {
        printf("%d ", root->data);
        preOrder(root->left);
        preOrder(root->right);
    }
}

// 中序遍历
void inOrder(TreeNode *root)
{
    if (root) {
        inOrder(root->left);
        printf("%d ", root->data);
        inOrder(root->right);
    }
}

// 后序遍历
void postOrder(TreeNode *root)
{
    if (root) {
        postOrder(root->left);
        postOrder(root->right);
        printf("%d ", root->data);
    }
}
```
#### 6.对于值为x的有关处理 
```C
int op_x(btree *root, datatype x)
{
    // null 理解为假 即没有找到x
    if (root == NULL)
    {
        return 1;
    }
    // 找到x 
    if (root->data == x&&hight!=1)
    {
        // 处理
    }

// 如果是BST可以如下操作 
//    else if (x < root->data)
//    {
//        return heightofx(root->lchild, x, hight + 1);
//    }
//    else
//    {
//        return heightofx(root->rchild, x, hight + 1);
//    }

    // 左子树寻找
        int left = op_x(root->lchild, x);
        if (leftDepth != 1)//此处说明找到了 也就是不假 != data when case null
        {
         //    操作
         return //something
        }
    
    //  右子树寻找 无论找没找到也要返回
        int right = op_x(root->rchild, x);
        return //something 
}
```

#### 7.叶节点处理
```C
void findleaf(btree *root)
{
    if (root == NULL)
    {
        return;
    }
    if (root->lchild == NULL && root->rchild == NULL)
    {
        // 处理叶节点
    }
    else
    {
        findleaf(root->lchild);
        findleaf(root->rchild);
    }
}
```