#include <stdio.h>
#define MAXSIZE 100
typedef int ElemType;

typedef struct 
{
    ElemType data[MAXSIZE];   // 顺序表存储数组
    int length;           // 当前长度
} SqList;

// 初始化
void InitList(SqList *L)
{
    L->length = 0;
}

// 尾部插入
int ListAppend(SqList *L, ElemType e)
{
    if (L->length >= MAXSIZE)
    {
        printf("顺序表已满\n");
        return 0;
    }
    L->data[L->length] = e;
    L->length++;
    return 1;
}

// 指定位置插入
int ListInsert(SqList *L, int pos, ElemType e)
{
    if (pos < 1 || pos > L->length + 1)
        return 0;

    for (int i = L->length - 1; i >= pos - 1; i--)
    {
        L->data[i + 1] = L->data[i];
    }
    L->data[pos - 1] = e;
    L->length++;
    return 1;
}
//delete
int deleteElem(SqList* L, int pos, ElemType* e){
    *e = L->data[pos-1];
    if(pos < L->length){
        for(int i = pos; i < L->length;i++){
            L->data[i-1] = L->data[i];
        }
    }
    L->length--;
    return 1;
}

int findElem(SqList* L, ElemType e){
    for(int i = 0;i<L->length;i++){
        if(L->data[i] == e){
            return i+1;
        }
    }
    return 0;
}

int main()
{
    SqList L;
    ElemType delData;
    InitList(&L);

    ListAppend(&L, 5);
    ListAppend(&L, 67);
    ListAppend(&L, 28);
    ListAppend(&L, 50);
    ListAppend(&L, 53);
    for (int i = 0; i < L.length; i++)
    {
        printf("%d\n", L.data[i]);
    
    }
    printf("\n");
    ListInsert(&L, 2, 28);
    for (int i = 0; i < L.length; i++)
    {
        printf("%d\n", L.data[i]);
    }
    printf("\n");
    deleteElem(&L,2,&delData);
    for (int i = 0; i < L.length; i++)
    {
        printf("%d\n", L.data[i]);
    }
    return 0;
}
//初始化也可以用malloc写