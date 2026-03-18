#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define EPS 1e-6

// 递归查找 24 点
// a[]: 当前剩余的数字
// exp[][100]: 对应数字的表达式字符串
// n: 当前数组中的数字个数
int find24(double a[], char exp[][100], int n) {
    if (n == 1) {
        if (fabs(a[0] - 24) < EPS) {
            printf("找到解法: %s = 24\n", exp[0]);
            return 1;
        }
        return 0;
    }

    double next_a[4];
    char next_exp[4][100];

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) continue; // 不能自己和自己算

            // 提取剩余的数字到新数组
            int m = 0;
            for (int k = 0; k < n; k++) {
                if (k != i && k != j) {
                    next_a[m] = a[k];
                    strcpy(next_exp[m], exp[k]);
                    m++;
                }
            }

            // 尝试 4 种运算
            for (int op = 0; op < 4; op++) {
                double res;
                char symbol;
                
                if (op == 0) { res = a[i] + a[j]; symbol = '+'; }
                else if (op == 1) { res = a[i] - a[j]; symbol = '-'; }
                else if (op == 2) { res = a[i] * a[j]; symbol = '*'; }
                else {
                    if (fabs(a[j]) < EPS) continue; // 除数不能为 0
                    res = a[i] / a[j]; symbol = '/';
                }

                // 将新生成的表达式存入新数组的末尾
                next_a[m] = res;
                sprintf(next_exp[m], "(%s%c%s)", exp[i], symbol, exp[j]);

                // 递归进入下一层（数字个数减 1）
                if (find24(next_a, next_exp, n - 1)) return 1;
            }
        }
    }
    return 0;
}

int main() {
    double a[4];
    char exp[4][100];

    printf("请输入4个整数（1-13之间，用空格隔开）：\n");
    for (int i = 0; i < 4; i++) {
        int val;
        if (scanf("%d", &val) != 1) return 1;
        a[i] = (double)val;
        sprintf(exp[i], "%d", val);
    }

    printf("\n计算中...\n");
    if (!find24(a, exp, 4)) {
        printf("抱歉，这四个数字无法通过加减乘除得到 24。\n");
    }

    return 0;
}