## ���ݽṹ

### ��������
#### 1. ����ڵ�
```c
typedef struct Node
{
    int data;
    struct Node *next;
} Node;
```

#### 2. ��ʼ������
```c
Node *initList()
{
    Node *head = (Node *)malloc(sizeof(Node));
    head->next = NULL;
    return head;
}
```

#### 3. ��ӽڵ�
```c
void addNode(Node *head, int data)
{
    Node *temp = (Node *)malloc(sizeof(Node));
    temp->data = data;
    temp->next = NULL;

    // �������һ���ڵ�
    Node *cur = head;
    while (cur->next != NULL)
    {
        cur = cur->next;
    }

    // ����½ڵ㵽ĩβ
    cur->next = temp;
}
```

#### 4. ɾ���ڵ�
```c
void delNode(Node *head, int data)
{
    if (head == NULL || head->next == NULL)
        return; // �������ֻ��ͷ�ڵ�

    // ���������ɾ��ͷ�ڵ�
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
        return; // δ�ҵ�
    }

    Node *temp = cur->next;
    cur->next = temp->next;
    free(temp);
}
```

#### 5. ���ҽڵ�
```c
Node *findNode(Node *head, int data)
{
    Node *cur = head->next; // ���׽ڵ��һ���ڵ㿪ʼ
    while (cur != NULL && cur->data != data)
    {
        cur = cur->next;
    }
    return cur; // �ҵ����ظýڵ㣬���򷵻� NULL
}
```

---

### ջ

#### ˳��ջ����ջ��
```c
#define MAXSIZE 100
typedef struct Stack
{
    int data[MAXSIZE];
    int top;
} Stack;

// ��ʼ��ջ
void initStack(Stack *s) { s->top = -1; }

// �ж�ջ�Ƿ�Ϊ��
int isEmpty(Stack *s) { return s->top == -1; }

// �ж�ջ�Ƿ���
int isFull(Stack *s) { return s->top == MAXSIZE - 1; }

// ��ջ
void push(Stack *s, int value)
{
    if (isFull(s)) return;
    s->data[++s->top] = value;
}

// ��ջ
int pop(Stack *s)
{
    return isEmpty(s) ? -1 : s->data[s->top--];
}

// ��ȡջ��Ԫ��
int peek(Stack *s)
{
    return isEmpty(s) ? -1 : s->data[s->top];
}
```

#### ��ջʵ��
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

### ����

#### ѭ������
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

### ��

#### 0.����&����

- �ǿն�����(NEDT) ��n���ڵ� ����n-1����֧
- NEDT ��i������� $ 2^{i-1} $�����
- NEDT ���h �����$2^h-1$�����
- NEDT��n��Ҷ���,��N����Ϊ2�Ľ��,�� n=N+1
> ��չ:$ n_0 = \sum_{i=1}^m(m-1)n_m   \\m��bt�Ķ� $
- NEDT n����� h=$[log_2^n]+1$(����ȡ��)
- ��ת���������ֵܽڵ����ߣ�ɾ��������������н������
- ����ת���������Ȱ������е���ת��Ϊ���������ٴ����Ķ�������ʼ������Ϊǰһ������������
- �����������ص㣺û�ж�Ϊ1�Ľ��  ������С��Ȩ·: ��Ȩ�������֣�ÿ�ΰ�Ȩ��С���������ϳ�һ����������Ȩ��ӷŻ����֣��ظ�����
- ǰ��/������� �����ڵ� ������������ҵ��ý�� ���ҷֱ�Ϊ�����������ظ�����
#### 1. ����ڵ�
```c
typedef struct TreeNode
{
    int data;
    struct TreeNode *left;
    struct TreeNode *right;
} TreeNode;
```

#### 2. �����ڵ�
��ʱ����Բ������г� ֱ�ӷ��ڲ��뺯���й���newnode
```c
TreeNode *createNode(int data)
{
    TreeNode *newNode = (TreeNode *)malloc(sizeof(TreeNode));
    newNode->data = data;
    newNode->left = newNode->right = NULL;
    return newNode;
}
```

#### 3. ����ڵ㣨������������
```c
TreeNode *insertBST(TreeNode *root, int data)
{
    if (!root) return createNode(data);
    if (root->data > data) root->left = insert(root->left, data);
    else root->right = insert(root->right, data);
    return root;
}
```

#### 4. ���ҽڵ�(BST)
```c
TreeNode *searchBST(TreeNode *root, int data)
{
    if (!root || root->data == data) return root;
    return search(data < root->data ? root->left : root->right, data);
}
```

#### 5.��������
```c
// ǰ�����
void preOrder(TreeNode *root)
{
    if (root) {
        printf("%d ", root->data);
        preOrder(root->left);
        preOrder(root->right);
    }
}

// �������
void inOrder(TreeNode *root)
{
    if (root) {
        inOrder(root->left);
        printf("%d ", root->data);
        inOrder(root->right);
    }
}

// �������
void postOrder(TreeNode *root)
{
    if (root) {
        postOrder(root->left);
        postOrder(root->right);
        printf("%d ", root->data);
    }
}
```
#### 6.����ֵΪx���йش��� 
```C
int op_x(btree *root, datatype x)
{
    // null ���Ϊ�� ��û���ҵ�x
    if (root == NULL)
    {
        return 1;
    }
    // �ҵ�x 
    if (root->data == x&&hight!=1)
    {
        // ����
    }

// �����BST�������²��� 
//    else if (x < root->data)
//    {
//        return heightofx(root->lchild, x, hight + 1);
//    }
//    else
//    {
//        return heightofx(root->rchild, x, hight + 1);
//    }

    // ������Ѱ��
        int left = op_x(root->lchild, x);
        if (leftDepth != 1)//�˴�˵���ҵ��� Ҳ���ǲ��� != data when case null
        {
         //    ����
         return //something
        }
    
    //  ������Ѱ�� ������û�ҵ�ҲҪ����
        int right = op_x(root->rchild, x);
        return //something 
}
```

#### 7.Ҷ�ڵ㴦��
```C
void findleaf(btree *root)
{
    if (root == NULL)
    {
        return;
    }
    if (root->lchild == NULL && root->rchild == NULL)
    {
        // ����Ҷ�ڵ�
    }
    else
    {
        findleaf(root->lchild);
        findleaf(root->rchild);
    }
}
```


### ͼ
---
```C
//�ڽӾ���

#include <stdio.h>
#include <stdlib.h>

#define MAX_VERTICES 100

typedef struct
{
    int adjMatrix[MAX_VERTICES][MAX_VERTICES];
    int numVertices;
} Graph;

// ��ʼ��ͼ
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

// ��ӱ�
void addEdge(Graph *g, int src, int dest)
{
    g->adjMatrix[src][dest] = 1;
    // ���������ͼ������Ҫ��ӷ����
    // g->adjMatrix[dest][src] = 1;
}

// ��ӡ�ڽӾ���
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

// �ڽӱ�
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

// ��ʼ��ͼ
void initGraphAdjList(GraphAdjList *g, int numVertices)
{
    g->numVertices = numVertices;
    for (int i = 0; i < numVertices; i++)
    {
        g->vertices[i].id = i;
        g->vertices[i].edges = NULL;
    }
}

// ��ӱ�
void addEdgeAdjList(GraphAdjList *g, int src, int dest)
{
    // �����±�
    Edge *newEdge = (Edge *)malloc(sizeof(Edge));
    newEdge->dest = dest;
    newEdge->next = g->vertices[src].edges;
    g->vertices[src].edges = newEdge;

    // ���������ͼ������Ҫ��ӷ����
    newEdge = (Edge *)malloc(sizeof(Edge));
    newEdge->dest = src;
    newEdge->next = g->vertices[dest].edges;
    g->vertices[dest].edges = newEdge;
}

// ��ӡ�ڽӱ�
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
// ɾ����
void deleteEdgeAdjList(GraphAdjList *g, int src, int dest)
{
    Edge *current = g->vertices[src].edges;
    Edge *prev = NULL;

    // ����Դ����ı�
    while (current != NULL && current->dest != dest)
    {
        prev = current;
        current = current->next;
    }

    // ����ҵ���ɾ���ñ�
    if (current != NULL)
    {
        if (prev == NULL)
        {
            g->vertices[src].edges = current->next; // ɾ��ͷ�ڵ�
        }
        else
        {
            prev->next = current->next; // ɾ���м��β�ڵ�
        }
        free(current);
    }

    // ɾ������ߣ����������ͼ��
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
            g->vertices[dest].edges = current->next; // ɾ��ͷ�ڵ�
        }
        else
        {
            prev->next = current->next; // ɾ���м��β�ڵ�
        }
        free(current);
    }
}

// ɾ������
void deleteVertexAdjList(GraphAdjList *g, int vertexId)
{
    if (vertexId < 0 || vertexId >= g->numVertices)
    {
        return;
    }

    // ɾ��������ö�����صı�
    for (int i = 0; i < g->numVertices; i++)
    {
        if (i != vertexId)
        {
            deleteEdgeAdjList(g, i, vertexId);
        }
    }

    // ɾ�����㱾��
    for (int i = vertexId; i < g->numVertices - 1; i++)
    {
        g->vertices[i] = g->vertices[i + 1];
    }
    g->numVertices--;
}

// �������������DFS��
void dfs(GraphAdjList *g, int vertexId, int *visited)
{
    visited[vertexId] = 1; // ���Ϊ�ѷ���
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
// �������������BFS��
void bfs(GraphAdjList *g, int startVertex)
{
    int visited[MAX_VERTICES] = {0}; // ���ʱ������
    int queue[MAX_VERTICES];         // ����
    int front = 0, rear = -1;        // ����ָ��

    visited[startVertex] = 1;    // �����ʼ����Ϊ�ѷ���
    queue[++rear] = startVertex; // ���

    while (front <= rear)
    {
        int currentVertex = queue[front++]; // ����
        printf("%d ", currentVertex);

        Edge *current = g->vertices[currentVertex].edges;
        while (current != NULL)
        {
            if (!visited[current->dest])
            {
                visited[current->dest] = 1;    // ���Ϊ�ѷ���
                queue[++rear] = current->dest; // ���
            }
            current = current->next;
        }
    }
}

// prim-mst
//   ------------------------
#include <stdio.h>
#include <stdlib.h>

// �ڽӾ���
#define MAX_VERTEX_NUM 50
#define INFINITY 999999 // �����
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
    int id; // �ߵ�Ψһ��ʶ��
} mst;
mst minst[MAX_VERTEX_NUM]; // �洢��С�������ı�
int mstcount = 0;          // ��¼��С�������ı���

void cmp(int *a, int *b)
{
    return (*a - *b);
}
// ��С������ Prim �㷨
void prim(int start)
{
    int lowcost[MAX_VERTEX_NUM];       // �洢��ǰ��СȨֵ
    int closest[MAX_VERTEX_NUM];       // �洢��С������������Ķ���
    int visited[MAX_VERTEX_NUM] = {0}; // ��¼�����Ƿ��Ѽ�����С������

    // ��ʼ������
    for (int i = 0; i < vertex_count; i++)
    {
        lowcost[i] = INFINITY;
        closest[i] = start;
    }

    // ��ʼ�������С������
    visited[start] = 1;
    lowcost[start] = 0;
    mstcount = 0; // ������С����������

    // ������ʼ���ڽӱߵ�Ȩֵ
    for (int i = 0; i < vertex_count; i++)
    {
        if (graph[start][i].weight > 0)
        {
            lowcost[i] = graph[start][i].weight;
            closest[i] = start;
        }
    }

    // �𲽹�����С������
    for (int i = 1; i < vertex_count; i++)
    {
        int min_cost = INFINITY;
        int min_index = -1;

        // �ҳ�δ���붥����Ȩֵ��С�ı�
        for (int j = 0; j < vertex_count; j++)
        {
            if (!visited[j] && lowcost[j] < min_cost)
            {
                min_cost = lowcost[j];
                min_index = j;
            }
        }

        // ���ҵ��Ķ��������С������
        if (min_index != -1)
        {
            visited[min_index] = 1;

            minst[mstcount].u = closest[min_index];
            minst[mstcount].v = min_index;
            minst[mstcount].weight = lowcost[min_index];
            minst[mstcount].id = graph[closest[min_index]][min_index].id;
            mstcount++;

            lowcost[min_index] = 0; // �Ѽ��붥��Ȩֵ��Ϊ0

            // �����¼��붥����ڽӱ�
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
    prim(0); // �Ӷ���0��ʼ������С������
    return 0;
}
```
## �㷨ģ��

### ����
```C
#include <stdio.h>
#include <stdbool.h>

// �����ģ����
#define MAX_SIZE 100

// ȫ�ֱ���
int solution[MAX_SIZE]; // ��ǰ��
bool used[MAX_SIZE];    // ��Դʹ��״̬����ѡ��
int depth = 0;          // ��ǰ�ⳤ��

// ���ݺ��ĺ���
void backtrack(int step)
{
    // 1. ��ֹ��������鵱ǰ���Ƿ�����
    if (isComplete(step))
    {
        processSolution(step); // ������Ч��
        return;
    }

    // 2. ���ɺ�ѡ������ǰ�����õ�ѡ�
    int candidates[MAX_SIZE];
    int count = generateCandidates(step, candidates);

    // 3. �������к�ѡѡ��
    for (int i = 0; i < count; i++)
    {
        int candidate = candidates[i];

        // 4. ��֤��ѡѡ��Ŀ�����
        if (isValid(step, candidate))
        {
            // 5. ����ѡ��
            makeChoice(step, candidate);

            // 6. �ݹ�����
            backtrack(step + 1);

            // 7. ���ݣ�����ѡ��
            undoChoice(step, candidate);
        }
    }
}

// ===== ��Ҫ��������ʵ�ֵĺ��� =====
bool isComplete(int step)
{
    // ʵ��1����鵱ǰ���Ƿ���������ֹ������
}

void processSolution(int step)
{
    // ʵ��2�������ҵ��������⣨��ӡ/�洢��
}

int generateCandidates(int step, int candidates[])
{
    // ʵ��3�����ɵ�ǰ���ĺ�ѡѡ���
    // ���غ�ѡ����
}

bool isValid(int step, int candidate)
{
    // ʵ��4����֤��ѡѡ��Ŀ�����
}

void makeChoice(int step, int candidate)
{
    // ʵ��5������ѡѡ����뵱ǰ��
}

void undoChoice(int step, int candidate)
{
    // ʵ��6������ѡѡ��ӵ�ǰ���Ƴ�
}
// =================================

int main()
{
    // ��ʼ������״̬
    for (int i = 0; i < MAX_SIZE; i++)
    {
        solution[i] = 0;
        used[i] = false;
    }

    // ��������
    backtrack(0);

    return 0;
}
```