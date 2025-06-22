# DataStruct🙌
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
    
    拓展:$ n_0 = \sum_{i=1}^m(m-1)n_m $  其中m是bt的度

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
### 图
#### 基础操作
```C
//  邻接矩阵
#include <stdio.h>
#include <stdlib.h>

#define MAX_VERTICES 100

typedef struct
{
    int adjMatrix[MAX_VERTICES][MAX_VERTICES];
    int numVertices;
} Graph;

// 初始化图
void initGraph(Graph *g, int numVertices)
{
    g->numVertices = numVertices;
    for (int i = 0; i < numVertices; i++)
    {
        for (int j = 0; j < numVertices; j++)
        {
            g->adjMatrix[i][j] = 0;
        }
    }
}

// 添加边
void addEdge(Graph *g, int src, int dest)
{
    g->adjMatrix[src][dest] = 1;
    // 如果是无向图，还需要添加反向边
    // g->adjMatrix[dest][src] = 1;
}

// 打印邻接矩阵
void printGraph(Graph *g)
{
    for (int i = 0; i < g->numVertices; i++)
    {
        for (int j = 0; j < g->numVertices; j++)
        {
            printf("%d ", g->adjMatrix[i][j]);
        }
        printf("\n");
    }
}

// 邻接表
typedef struct Edge
{
    int dest;
    struct Edge *next;
} Edge;

typedef struct Vertex
{
    int id;
    Edge *edges;
} Vertex;

typedef struct
{
    Vertex vertices[MAX_VERTICES];
    int numVertices;
} GraphAdjList;

// 初始化图
void initGraphAdjList(GraphAdjList *g, int numVertices)
{
    g->numVertices = numVertices;
    for (int i = 0; i < numVertices; i++)
    {
        g->vertices[i].id = i;
        g->vertices[i].edges = NULL;
    }
}

// 添加边
void addEdgeAdjList(GraphAdjList *g, int src, int dest)
{
    // 创建新边
    Edge *newEdge = (Edge *)malloc(sizeof(Edge));
    newEdge->dest = dest;
    newEdge->next = g->vertices[src].edges;
    g->vertices[src].edges = newEdge;

    // 如果是无向图，还需要添加反向边
    newEdge = (Edge *)malloc(sizeof(Edge));
    newEdge->dest = src;
    newEdge->next = g->vertices[dest].edges;
    g->vertices[dest].edges = newEdge;
}

// 打印邻接表
void printGraphAdjList(GraphAdjList *g)
{
    for (int i = 0; i < g->numVertices; i++)
    {
        printf("%d: ", g->vertices[i].id);
        Edge *current = g->vertices[i].edges;
        while (current != NULL)
        {
            printf("%d -> ", current->dest);
            current = current->next;
        }
        printf("NULL\n");
    }
}
// 删除边
void deleteEdgeAdjList(GraphAdjList *g, int src, int dest)
{
    Edge *current = g->vertices[src].edges;
    Edge *prev = NULL;

    // 查找源顶点的边
    while (current != NULL && current->dest != dest)
    {
        prev = current;
        current = current->next;
    }

    // 如果找到，删除该边
    if (current != NULL)
    {
        if (prev == NULL)
        {
            g->vertices[src].edges = current->next; // 删除头节点
        }
        else
        {
            prev->next = current->next; // 删除中间或尾节点
        }
        free(current);
    }

    // 删除反向边（如果是无向图）
    current = g->vertices[dest].edges;
    prev = NULL;

    while (current != NULL && current->dest != src)
    {
        prev = current;
        current = current->next;
    }

    if (current != NULL)
    {
        if (prev == NULL)
        {
            g->vertices[dest].edges = current->next; // 删除头节点
        }
        else
        {
            prev->next = current->next; // 删除中间或尾节点
        }
        free(current);
    }
}

// 删除顶点
void deleteVertexAdjList(GraphAdjList *g, int vertexId)
{
    if (vertexId < 0 || vertexId >= g->numVertices)
    {
        return;
    }

    // 删除所有与该顶点相关的边
    for (int i = 0; i < g->numVertices; i++)
    {
        if (i != vertexId)
        {
            deleteEdgeAdjList(g, i, vertexId);
        }
    }

    // 删除顶点本身
    for (int i = vertexId; i < g->numVertices - 1; i++)
    {
        g->vertices[i] = g->vertices[i + 1];
    }
    g->numVertices--;
}

// 深度优先搜索（DFS）
void dfs(GraphAdjList *g, int vertexId, int *visited)
{
    visited[vertexId] = 1; // 标记为已访问
    printf("%d ", vertexId);

    Edge *current = g->vertices[vertexId].edges;
    while (current != NULL)
    {
        if (!visited[current->dest])
        {
            dfs(g, current->dest, visited);
        }
        current = current->next;
    }
}
// 广度优先搜索（BFS）
void bfs(GraphAdjList *g, int startVertex)
{
    int visited[MAX_VERTICES] = {0}; // 访问标记数组
    int queue[MAX_VERTICES];         // 队列
    int front = 0, rear = -1;        // 队列指针

    visited[startVertex] = 1;    // 标记起始顶点为已访问
    queue[++rear] = startVertex; // 入队

    while (front <= rear)
    {
        int currentVertex = queue[front++]; // 出队
        printf("%d ", currentVertex);

        Edge *current = g->vertices[currentVertex].edges;
        while (current != NULL)
        {
            if (!visited[current->dest])
            {
                visited[current->dest] = 1;    // 标记为已访问
                queue[++rear] = current->dest; // 入队
            }
            current = current->next;
        }
    }
}
```
#### prim-mst
```C
#include <stdio.h>
#include <stdlib.h>

// 邻接矩阵
#define MAX_VERTEX_NUM 50
#define INFINITY 999999 // 无穷大
typedef struct edge
{
    int id;
    int weight;
} edge;

edge graph[MAX_VERTEX_NUM][MAX_VERTEX_NUM];
int vertex_count = 0;
int edge_count = 0;
typedef struct mst
{
    int u;
    int v;
    int weight;
    int id; // 边的唯一标识符
} mst;
mst minst[MAX_VERTEX_NUM]; // 存储最小生成树的边
int mstcount = 0;          // 记录最小生成树的边数

void cmp(int *a, int *b)
{
    return (*a - *b);
}
// 最小生成树 Prim 算法
void prim(int start)
{
    int lowcost[MAX_VERTEX_NUM];       // 存储当前最小权值
    int closest[MAX_VERTEX_NUM];       // 存储最小生成树中最近的顶点
    int visited[MAX_VERTEX_NUM] = {0}; // 记录顶点是否已加入最小生成树

    // 初始化数组
    for (int i = 0; i < vertex_count; i++)
    {
        lowcost[i] = INFINITY;
        closest[i] = start;
    }

    // 起始点加入最小生成树
    visited[start] = 1;
    lowcost[start] = 0;
    mstcount = 0; // 重置最小生成树边数

    // 更新起始点邻接边的权值
    for (int i = 0; i < vertex_count; i++)
    {
        if (graph[start][i].weight > 0)
        {
            lowcost[i] = graph[start][i].weight;
            closest[i] = start;
        }
    }

    // 逐步构建最小生成树
    for (int i = 1; i < vertex_count; i++)
    {
        int min_cost = INFINITY;
        int min_index = -1;

        // 找出未加入顶点中权值最小的边
        for (int j = 0; j < vertex_count; j++)
        {
            if (!visited[j] && lowcost[j] < min_cost)
            {
                min_cost = lowcost[j];
                min_index = j;
            }
        }

        // 将找到的顶点加入最小生成树
        if (min_index != -1)
        {
            visited[min_index] = 1;

            minst[mstcount].u = closest[min_index];
            minst[mstcount].v = min_index;
            minst[mstcount].weight = lowcost[min_index];
            minst[mstcount].id = graph[closest[min_index]][min_index].id;
            mstcount++;

            lowcost[min_index] = 0; // 已加入顶点权值设为0

            // 更新新加入顶点的邻接边
            for (int k = 0; k < vertex_count; k++)
            {
                if (!visited[k] && graph[min_index][k].weight > 0 &&
                    graph[min_index][k].weight < lowcost[k])
                {
                    lowcost[k] = graph[min_index][k].weight;
                    closest[k] = min_index;
                }
            }
        }
    }
}

int main()
{
    int i, j, weight, id;
    int vertex1, vertex2;

    scanf("%d%d", &vertex_count, &edge_count);
    for (i = 1; i <= edge_count; i++)
    {
        scanf("%d%d%d%d", &id, &vertex1, &vertex2, &weight);
        graph[vertex1][vertex2].id = id;
        graph[vertex1][vertex2].weight = weight;
        graph[vertex2][vertex1].id = id;
        graph[vertex2][vertex1].weight = weight;
    }
    prim(0); // 从顶点0开始构建最小生成树
    return 0;
}
```
#### 北京地铁查询（dijkstra）
```C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXNUM 512      // 地铁最大站数
#define MAXLEN 16       // 地铁站名的最大长度
#define INFINITY 999999 // 无穷大

struct station
{                       // 车站信息
    char sname[MAXLEN]; // 车站名
    int ischange;       // 是否为换乘站，0-否，1-换乘
};
struct weight
{
    int weight;  // 两个站间的权重，即相差站数，缺省为1
    int line_id; // 两个顶点所在的线号
};
struct station BGvertex[MAXNUM];         // 地铁网络图顶点数组
struct weight BGweights[MAXNUM][MAXNUM]; // 网络图权重数组，邻接矩阵
int station_num = 0;                     // 实际地铁总站数

char start_station[MAXLEN]; // 起点站名
char end_station[MAXLEN];   // 终点站名

int addVertex(struct station st)
{
    int i;
    for (i = 0; i < station_num; i++)
    {
        if (strcmp(BGvertex[i].sname, st.sname) == 0)
        {
            return i; // 已存在该站，返回其下标
        }
    }
    BGvertex[station_num] = st;                   // 添加新站
    BGvertex[station_num].ischange = st.ischange; // 设置换乘站标志
    return station_num++;                         // 返回新站的下标并增加总站数
}

void initMap()
{
    FILE *fp;
    int i, j, snum, line_id, lnum, v1, v2; // v1为上一个站的下标，v2为当前站的下标
    struct station st;

    fp = fopen("bgstations.txt", "r");

    fscanf(fp, "%d", &snum);

    for (i = 0; i < snum; i++)
    {
        fscanf(fp, "%d %d", &line_id, &lnum);
        v1 = v2 = -1;
        for (j = 0; j < lnum; j++)
        {
            fscanf(fp, "%s %d", st.sname, &st.ischange);
            v2 = addVertex(st); // 将该站加到站信息数组中，返回其下标
            if (v1 != -1)
            {
                BGweights[v1][v2].weight = BGweights[v2][v1].weight = 1;
                BGweights[v1][v2].line_id = BGweights[v2][v1].line_id = line_id;
            }
            v1 = v2;
        }
    }
    fclose(fp);
    return;
}

int stationIndex(const char *sname)
{
    int i;
    for (i = 0; i < station_num; i++)
    {
        if (strcmp(BGvertex[i].sname, sname) == 0)
        {
            return i; // 返回站名对应的下标
        }
    }
    return -1; // 未找到该站名
}

void dijistra(int start, int end)
{
    int i, j, k, min, v;
    int dist[MAXNUM];          // 存储起点到各个顶点的最短距离，例如 dist[i] = 5 表示起点到顶点i的最短距离为5
    int path[MAXNUM];          // 存储前驱顶点,                例如 path[i] = j 表示顶点i的前驱顶点是j
    int visited[MAXNUM] = {0}; // 记录顶点是否已访问

    for (i = 0; i < station_num; i++)
    {
        dist[i] = INFINITY; // 初始化距离为无穷大
        path[i] = -1;       // 初始化前驱顶点为-1
    }
    dist[start] = 0; // 起点到自身的距离为0

    for (i = 0; i < station_num; i++)
    {
        min = INFINITY;
        v = -1;
        for (j = 0; j < station_num; j++)
        {
            if (!visited[j] && dist[j] < min)
            {
                min = dist[j];
                v = j; // 找到未访问的最小距离顶点
            }
        }
        if (v == -1)
            break; // 如果没有可访问的顶点，退出循环

        visited[v] = 1; // 标记该顶点已访问

        for (j = 0; j < station_num; j++)
        {
            if (!visited[j] && BGweights[v][j].weight > 0) // 有边且未访问
            {
                if (dist[v] + BGweights[v][j].weight < dist[j])
                {
                    dist[j] = dist[v] + BGweights[v][j].weight;
                    path[j] = v; // 更新前驱顶点
                }
            }
        }
    }
    // 算法结束，下面按照要求输出

    //  // 打印path数组，也就是每一站的前驱站
    //  for (i = 0; i < station_num; i++)
    //  {
    //      printf("path[%d] = %d\n", i, path[i]);
    //  }

    // 输出最短路径和距离
    // printf("从 %s 到 %s 的最短路径为：", BGvertex[start].sname, BGvertex[end].sname);
    if (dist[end] == INFINITY)
    {
        printf("FAIL!\n");
        return;
    }
    int route[MAXNUM]; // 存储最短路径的顶点下标，记录顺序为从终点到起点（因为path记录的是前驱顶点）
    int count = 0;     // 路径顶点计数,包括起点的总站数 即=dist[end]+1

    // 从终点开始回溯到起点，构建最短路径 end->path[end]->path[path[end]]->...->start
    for (k = end; k != -1; k = path[k])
    {
        route[count++] = k;
    }
    // 逆序输出路径，因为我们是从终点回溯到起点的
    // 输出格式：start-line_id(num)-change-line_id(num)-...-end
    for (i = count - 1; i >= 0; i--)
    {
        if (i == count - 1)
        {
            printf("%s", BGvertex[route[i]].sname); // 输出起点站名
        }
        else if (i == 0)
        {
            printf("-%s", BGvertex[route[i]].sname); // 输出终点站名
        }
        else
        {
            int line_id = BGweights[route[i]][route[i + 1]].line_id;
            int num = 1;
            while (i > 0 && BGweights[route[i]][route[i - 1]].line_id == line_id) // 下一个站和当前站在同一条线路上
            {
                num++;
                i--;
            }
            // 循环结束后，i指向换乘站
            // num=当前线路站数
            printf("-%d(%d)-%s", line_id, num, BGvertex[route[i]].sname); // 输出线路信息和换乘站名
            if (i - 1 == 0)
            {
                printf("-%d(%d)-%s", BGweights[route[i]][route[i - 1]].line_id, 1, BGvertex[route[i - 1]].sname); // 如果是换乘站且前面没有其他站，则输出前一个站名
                break;
            }
        }
    }

    // printf("\n最短距离为：%d\n", dist[end]);

    // 输出换乘站信息
    // printf("\n换乘站信息：\n");
    // for (i = 0; i < count; i++)
    // {
    //     if (BGvertex[route[i]].ischange)
    //     {
    //         printf("%s ", BGvertex[route[i]].sname);
    //     }
    // }
    // printf("\n");
    // // 输出线路信息
    // printf("线路信息：\n");
    // for (i = 0; i < count - 1; i++)
    // {
    //     int line_id = BGweights[route[i]][route[i + 1]].line_id;
    //     if (line_id > 0)
    //     {
    //         printf("%s -> %s: 线路 %d\n", BGvertex[route[i]].sname, BGvertex[route[i + 1]].sname, line_id);
    //     }
    // }
    // printf("\n");
}
int main()
{
    struct station st;
    int i, j;

    initMap(); // 初始化地铁网络图

    // printf("地铁站信息：\n");
    // for (i = 0; i < station_num; i++)
    // {
    //     printf("%s %d\n", BGvertex[i].sname, BGvertex[i].ischange);
    // }
    int v1, v2;
    scanf("%s %s", start_station, end_station);

    v1 = stationIndex(start_station);
    v2 = stationIndex(end_station);

    dijistra(v1, v2);

    return 0;
}
```

## 排序
```C
#include <stdio.h>
#include <stdlib.h>

int buf[105];
int t[105];
int n;
int num = 0; // comparison count
void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}
void xuanze()
{
    for (int i = 0; i < n - 1; i++)
    {
        int min = i;
        for (int j = i + 1; j < n; j++)
        {
            num++;
            if (buf[j] < buf[min])
                min = j;
        }
        if (min != i)
        {
            int temp = buf[i];
            buf[i] = buf[min];
            buf[min] = temp;
        }
    }
}
void bubble()
{
    for (int i = 0; i < n - 1; i++)
    {
        int flag = 0;
        for (int j = 0; j < n - 1 - i; j++)
        {

            num++;
            if (buf[j] > buf[j + 1])
            {
                flag = 1;
                int temp = buf[j];
                buf[j] = buf[j + 1];
                buf[j + 1] = temp;
            }
        }
        if (!flag)
            break;
    }
}
// 堆排序
void adjust(int k[], int i, int n) // 构建堆
{
    int j, temp;
    temp = k[i];
    j = 2 * i + 1;
    while (j < n)
    {
        if (j < n - 1 && k[j] < k[j + 1])
            j++;
        num++;
        if (temp >= k[j])
            break;
        k[(j - 1) / 2] = k[j];
        j = 2 * j + 1;
    }
    k[(j - 1) / 2] = temp;
}
void heap(int k[], int n)
{
    int i;
    int temp;
    for (i = n / 2 - 1; i >= 0; i--)
        adjust(k, i, n);
    for (i = n - 1; i >= 1; i--)
    {
        temp = k[i];
        k[i] = k[0];
        k[0] = temp;
        adjust(k, 0, i);
    }
}

// 二路归并排序

void merge(int l1, int r1, int l2, int r2)
{
    int i = l1, j = l2, q = l1;
    while (i <= r1 && j <= r2)
    {
        num++;
        if (buf[i] <= buf[j])
            t[q++] = buf[i++];
        else
            t[q++] = buf[j++];
    }
    while (i <= r1)
        t[q++] = buf[i++];
    while (j <= r2)
        t[q++] = buf[j++];
    for (int p = l1; p <= r2; p++)
        buf[p] = t[p];
}
void mergesort(int l, int r)
{
    int m = (l + r) / 2;
    if (l < r)
    {
        mergesort(l, m);
        mergesort(m + 1, r);
        merge(l, m, m + 1, r);
    }
}

// 快排
void quick(int left, int right)

{
    int i, last;
    if (left < right)
    {
        last = left;
        for (i = left + 1; i <= right; i++)
        {
            num++;
            if (buf[i] < buf[left])
                swap(&buf[++last], &buf[i]);
        }
        swap(&buf[left], &buf[last]);
        quick(left, last - 1);
        quick(last + 1, right);
    }
}

int main()
{
    int op;
    scanf("%d%d", &n, &op);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &buf[i]);
    }
    if (op == 1)
        xuanze();
    else if (op == 2)
        bubble();
    else if (op == 3)
        heap(buf, n);
    else if (op == 4)
        mergesort(0, n - 1);
    else if (op == 5)
        quick(0, n - 1);

    for (int i = 0; i < n; i++)
    {
        if (i == n - 1)
            printf("%d\n", buf[i]);
        else
            printf("%d ", buf[i]);
    }

    printf("%d", num);
    return 0;
}
```
## 算法模块
### 回溯
```c

#include <stdio.h>
#include <stdbool.h>

// 问题规模限制
#define MAX_SIZE 100

// 全局变量
int solution[MAX_SIZE]; // 当前解
bool used[MAX_SIZE];    // 资源使用状态（可选）
int depth = 0;          // 当前解长度

// 回溯核心函数
void backtrack(int step)
{
    // 1. 终止条件：检查当前解是否完整
    if (isComplete(step))
    {
        processSolution(step); // 处理有效解
        return;
    }

    // 2. 生成候选集（当前步可用的选项）
    int candidates[MAX_SIZE];
    int count = generateCandidates(step, candidates);

    // 3. 遍历所有候选选项
    for (int i = 0; i < count; i++)
    {
        int candidate = candidates[i];

        // 4. 验证候选选项的可行性
        if (isValid(step, candidate))
        {
            // 5. 做出选择
            makeChoice(step, candidate);

            // 6. 递归深入
            backtrack(step + 1);

            // 7. 回溯：撤销选择
            undoChoice(step, candidate);
        }
    }
}

// ===== 需要根据问题实现的函数 =====
bool isComplete(int step)
{
    // 实现1：检查当前解是否完整（终止条件）
}

void processSolution(int step)
{
    // 实现2：处理找到的完整解（打印/存储）
}

int generateCandidates(int step, int candidates[])
{
    // 实现3：生成当前步的候选选项集合
    // 返回候选数量
}

bool isValid(int step, int candidate)
{
    // 实现4：验证候选选项的可行性
}

void makeChoice(int step, int candidate)
{
    // 实现5：将候选选项加入当前解
}

void undoChoice(int step, int candidate)
{
    // 实现6：将候选选项从当前解移除
}
// =================================

int main()
{
    // 初始化所有状态
    for (int i = 0; i < MAX_SIZE; i++)
    {
        solution[i] = 0;
        used[i] = false;
    }

    // 启动回溯
    backtrack(0);

    return 0;
}
```