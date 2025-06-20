
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
    int *q1[5]; // 数组指针，q1 是一个数组，数组里是指向 int 的指针
    // 初始化示例：{ &a[1], &a[2], ... }
    // 等价写法：
    int *(q1_equiv[5]);

    int (*q2)[5]; // 指针数组，q2 是一个指针，指向含有 [5 个 int 元素]的一维数组
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
    while ((c = fgetc(in)) != EOF)
    {
        // 处理字符
    }
    //一行一行读取
    while(fgets(str,100,in))
    {
        //...
	}

    fclose(in);
    //把标准输入输出直接重定向到文件，这时候可以直接scanf读in  printf写out
    freopen("filein.txt", "r", stdin);
	freopen("fileout.txt", "w", stdout);
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

### 约瑟夫问题

递推公式

$ f(n,m)=(f(n - 1, m) + m - 1) % n + 1;$

---