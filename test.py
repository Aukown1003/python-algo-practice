import math

num = 1
name = '1'

print(num)
print(name)

new_num = int(name)
print(new_num, type(new_num))
# sep= 単語の間に入れるワード　end=最後の入れる文字や処理 option + ¥でバックスラッシュ
print('hi', 'mike', 'yu', sep=',', end='.\n')

result = math.sqrt(25)
print(result)

print('hello.\nhou wow you')
# \nを文字列で使いたい場合は戦闘にrをおいておく
print(r'c:\name\name')
# 複数行書くときは""""""を入れる
print("""
line1
line2
line3
""")

# 繰り返し処理
print('hi' * 3 + 'mike')

# 長い文字列は改行で
s = ('aaaaaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbbbb')
print(s)

word = 'python'
# ワードの[n]番目を表示
print(word[0])
# 最後は-1で指定
print(word[-1])
# 1番目から2文字など指定もできる
print(word[0:2])
print(word[:2])
print(word[2:])
# 部分的に入れ替えたい場合
word = 'j' + word[1:]
print(word)

s = 'my name is yu'
print(s)
is_start = s.startswith('my')
print(is_start)

print(s.find('yu'))
print(s.count('my'))

x = str('test')
print(type(x))
print("#################")
# 以下勉強
# practice1-2
# 標準出力を用いて、1 行目に 1 を、 2 行目に 2 を、 3 行目に 3 を表示するプログラムを作成してください。
print("1-2の答えは")
print(1)
print(2)
print(3)
# もしくは
print("""
1
2
3
""")
print("#################")
# practice1-3
# 27182 を 818 で割った余りを表示するプログラムを作成してください。
numerator = 27182 # 分子
denominator = 818 # 分母
remainder = numerator % denominator
print("1-3の答えは" + str(remainder))
print("#################")
# practice1-4
# 314×(159+265)−358 の計算結果を出力するプログラムを作成してください。
ans = 314*(159+265)-358
print("1-4の答えは" + str(ans))
print("#################")
# practice1-5
# 1 日は 24 時間、 1 時間は 60 分、1 分は 60 秒です。
# 1 日は何秒かを計算し、整数で出力するプログラムを作成してください。
day = 24
hour = 60
second = 60
total_second = second * hour * day
print("1-5の答えは" + str(total_second))

print("#################")
# practice2 1-1
# 1 以上 100 以下の整数 N が標準入力から与えられます。
# N を 2 倍した値を標準出力するプログラムを作ってください。
# 入力を整数型として受け取る
print("practice2 1-1")
N = int(input())
print(N*2)

print("#################")
# practice2 1-2
# 1 以上 100 以下の整数 N が標準入力から与えられます。
# N を 5 で割ったあまりを標準出力するプログラムを作成してください。
print("practice2 1-2")
N = int(input())
print(N%5)

print("#################")
# practice2 1-3
# 文字列 S が標準入力から与えられます。
# S を 3 回繰り返してできる文字列を標準出力するプログラムを作成してください。
print("practice2 1-3")
S = str(input())
print(str(S*3))

print("#################")
# practice2 1-4
# 長さ 5 の文字列 S が標準入力から与えられます。文字列 S の中央の文字を出力してください。
# たとえば入出力例 1 に示す通り、S= power に対しては、文字 w を出力します。
print("practice2 1-4 文字列の入力")
S = str(input())
print(S[2])

print("#################")
# practice2 1-5
# 0 以上 23 以下の整数 X が標準入力から与えられます。
# 現在の時刻が X 時のとき、日が変わる ( 24 時になる) まであと何時間かかるかを計算してください。
print("practice2 1-5")
X = int(input())
print(24 - X)

print("#################")
# 標準入力を 1 行受け取り、空白で区切り、一括で整数型に変換し、 A, B という変数に代入する
print("practice3 ２つの値を入力")
A, B = map(int, input().split())
# 変数 A と B の和を表示する
print(A+B)

print("#################")
# practice2 2-1
# 2 つの正の整数 A,B が空白区切りで入力されます。
# A+B の値を出力してください。
A, B = map(int, input().split())
print(A+B)

print("#################")
# practice2 2-2
# 2 つの正の整数 A,B が空白区切りで入力されます。 A と B のうち大きい方の値を出力してください。
# ただし、A と B の値は異なることが保証されています。
A, B = map(int, input().split())
print(max(A, B))

print("#################")
# practice2 2-3
# 2 つの正の整数 A,B が空白区切りで入力されます。 A と B のうち一の位が小さい方の値を出力してください。
# ただし、A と B の一の位は異なることが保証されています。
# 補足
# 整数の一の位はその数を 10 で割った余りと等しいです。
# たとえば 17 の一の位は 7 ですが、これは 17 を 10 で割った余りと一致します。
A, B = map(int, input().split())
if A%10 < B%10:
     print(A)
else:
     print(B)

print("#################")
# practice2 2-4
# 2 つの正の整数 A,B が空白区切りで入力されます。A が B の倍数かどうかを判定してください。
# 補足
# 「A が B の倍数である」ことは、「A が B で割りきれる」ことと等しいです。
A, B = map(int, input().split())
if A%B == 0:
     print("Yes")
else:
     print("No")

print("#################")
# practice2 2-5
# 3 つの整数 A,B,C が空白区切りで入力されます。3 つの整数の平均値を整数で出力してください。
# ただし、答えは整数になることが保証されています。
A, B, C = map(int, input().split())
# 演算子 / を使うと、計算結果が小数型 (float 型) 整数値を出力したい場合は、演算子 //
print((A + B + C) // 3)

print("#################")
# practice2 2-6
# 4 つの正の整数 A,B,C,D が空白区切りで入力されます。4 つの整数の最大値を出力してください。
A, B, C, D = map(int, input().split())
print(max(A, B, C, D))

print("#################")
# practice2 2-7
# 2 つの文字列 S,T が改行区切りで入力されます。S と T が等しい文字列であるかを判定してください。
S = input()
T = input()
if S == T:
     print("Yes")
else:
     print("No")

print("#################")
# practice2 2-8
S = input()
T = input()
U = input()
print(U + T + S)

print("#################")
# practice2 2-9
# 文字列 S と正の整数 N が改行区切りで入力されます。S の前から N 番目の文字を出力してください。
# ただしここでは、文字列 S の先頭の文字は 1 文字目であるとします。
S = str(input())
N = int(input())
print(S[N - 1])

print("#################")
# practice2 2-10
# 文字列 S が 1 行目に、2 つの正の整数 N,M が空白区切りで 2 行目に入力されます。 S の前から N 番目の文字と、前から M 番目の文字を入れ替えた文字列を出力してください。
# ただしここでは、文字列 S の先頭の文字は 1 文字目であるとします。
S = input()
N, M = map(int, input().split())
s_list = list(S)
print(s_list) #['s', 'a', 'f', 'a']のような感じ
s_list[N-1], s_list[M-1] = s_list[M-1], s_list[N-1] #文字の代入n番目とm番目を=の右側の値で代入
result = ''.join(s_list) #['s', 'a', 'f', 'a']を合体
print(result)

print("#################")
# practice3
# 入力を整数型として受け取る
N = int(input())
# 入力を整数型配列として受け取る
A = list(map(int, input().split()))

print("#################")
# practice3 3-1
N = int(input())
A = list(map(int, input().split()))
ans = 0
for item in A:
     ans += item
print(ans)

print("#################")
# practice3 3-2
N = int(input())
A = list(map(int, input().split()))
ans = 1
for item in A:
    ans *= item
print(ans)

print("#################")
# practice3 3-3
N = int(input())
A = list(map(int, input().split()))
for item in A:
     print(item%10)

print("#################")
# practice3 3-4
N = int(input())
A = list(map(int, input().split()))
for item in A:
     if item % 3 == 0:
          print(item)

print("#################")
# practice3 3-5
N = int(input())
A = list(map(int, input().split()))
A.reverse()
for item in A:
     print(item)

N = int(input())
A = list(map(int, input().split()))
for item in reversed(A): #reverseで反転できる
    print(item)

print("#################")
# practice3 3-6
N = int(input())
A = list(map(int, input().split()))
print(int(sum(A)/N))
print(sum(A) // N)

# intで整数型に、sumで合計を、/Nで平均を

N = int(input()) # 入力を整数型として受け取る
A = list(map(int, input().split())) # 入力を整数型配列として受け取る
sum = 0 # 総和を格納する変数
for item in A: # A の各要素に対して処理を行う
    sum += item
ans = sum // N # 配列の平均値を求める
print(ans)

print("#################")
# practice3 3-7
N = int(input())
A = list(map(int, input().split()))
print(min(A))

print("#################")
# practice3 3-8
N = int(input())  # 入力を整数型として受け取る
A = [""] * N  # 空の配列をN個作る。N = 3 ["","",""]
for i in range(N):  # range(N) は 0 から N-1 までの整数を生成する
    A[i] = input()  # 入力を文字列型配列として受け取る
ans = 0 # 答え
for item in A: # A の各要素の長さを足し合わせる
    ans += len(item)
print(ans)

print("#################")
# practice3 3-9
N = int(input())
A = [""] * N
for i in range(N):
     A[i] = input()
ans = ""
for item in A:
     ans += item[0]
print(ans)

print("#################")
# practice3 3-10
N = int(input())
# A = [input() for i in range(N)] とも書ける
A = [""] * N
for i in range(N):
     A[i] = input()

left_count = 0
for word in A:
     if word == "left":
          left_count += 1

right_count = N - left_count
if left_count > right_count:
     print("left")
elif left_count < right_count:
     print("right")
else:
     print("same")

print("#################")
# 配列の全探索 1
# 整数 N, V と、N 個の整数 Aが与えられます。
# N 個の整数の中に、整数 V があるかどうかを判定するプログラムを作成してください。
# N V
# A0~An-1
# 入力例 1
# 5 1
# 3 5 1 9 2
# Yes
N, V = map(int, input().split()) # 分割するときはmap+split
A = list(map(int, input().split())) # 複数は更にlist化
flag = False  # flagの初期設定
for num in A:
    if V == num:
        flag = True  # 存在すればtrueで設定する

if flag:  # flagが存在する時
    print("Yes")
else:
    print("No")

print("#################")
# 配列の全探索 2
# 整数 N, V と、N 個の整数 Aが与えられます。
# N 個の整数の中に整数 V が何個あるかを数えるプログラムを作成してください。

N, V = map(int, input().split())
A = list(map(int, input().split()))

size = 0
for i in A:
    if i == V:
        size += 1
print(size)

print("#################")
# 配列の全探索 3
# N 個の整数 Aが与えられます。
# N 個の整数のうち、正の整数が何個あるかを数えるプログラムを作成してください。
N = int(input())
A = list(map(int, input().split()))
count = 0
for i in A:
    if i > 0:
        count += 1
print(count)

print("#################")
# 配列の全探索 4
# N 個の整数 A
# N 個の整数の中で 最も右にある V は前から何番目にあるかを調べるプログラムを作成してください。
# ただし、V が存在しない場合はそのことを報告してください。
N, V = map(int, input().split())
A = list(map(int, input().split()))
ans = -1
# (0..4).each do のpython版
for num in range(N):
    if A[num] == V:
        ans = num
print(ans)

print("#################")
# 配列の全探索 5
# N 個の整数 A
# 次の条件を満たす i の個数を調べるプログラムを作成してください。
# i は1以上n-1以下
# AiはAi-1よりも大きい

N = int(input())
A = list(map(int, input().split()))
count = 0
for i in range(1,N):
    if A[i-1] < A[i]:
        count += 1

print(count)

print("#################")
# 配列の全探索 6
# N 個の整数 A
# N 個の整数の最大値を求めるプログラムを作成してください。
N = int(input())
A = list(map(int, input().split()))
max(A)
# 線形探索

maxnum = A[0]
for x in A:
    if x > maxnum:
        maxnum = x

# 答えを出力する
print(maxnum)

print("#################")
# 配列の全探索 7
# N 個の互いに相異なる整数 A0 ~ AN-1
# N 個の整数の中で一番大きいものは前から何番目にあるかを調べるプログラムを作成してください。
# ただし、N 個の整数のうちの先頭の整数 A 0は、前から 0 番目であると考えることとします。

N = int(input())
A = list(map(int, input().split()))

# 線形探索
index = 0
for i in range(N):
    if A[i] > A[index]:
        index = i

# 答えを出力する
print(index)

print("#################")
# 配列の全探索 8
N = int(input())
A = list(map(int, input().split()))

index = 0
for i in A:
    if i < index:
        index = i
print(index)
# もしくは
print(min(A))

print("#################")
# 配列の全探索 9
N = int(input())
A = list(map(int, input().split()))

count = [0] * 9
for x in A:
    count[x-1] += 1

for x in count:
    print(x)

print("#################")
# 配列の全探索 10
N = int(input())
A = list(map(int, input().split()))

count = [0] * 9
for x in A:
    count[x-1] += 1

index = 0
for i in range(9):
    if count[i] > count[index]:
        index = i

ans = index + 1
print(ans)

print("#################")
# 例題
# x以上y未満の整数iを順に調べる処理は次のように書きます。
# 入力を受け取る
N = int(input())

# count に 0 を代入する
count = 0

# i に 1 から N までの数を順番に代入する
for i in range(1,N+1):
    # i が 2 で割り切れるなら count に 1 を足す
    if i%2==0:
        count += 1

# count の値を出力する
print(count)

print("#################")
# 数値の全探索 1
# 1 以上 N 以下の整数のうち、 2 でも 3 でも 5 でも割り切れない数の個数を数えるプログラムを作成してください。
N = int(input())
count = 0
for i in range(1, N+1):
    if i%2 != 0 and i%3 != 0 and i%5 != 0:
        count += 1
print(count)

print("#################")
# 数値の全探索 2
# N の約数の個数を数えるプログラムを作成してください。
# ただし N の約数とは「 N を割り切ることのできる 1 以上の整数」のことです。
N = int(input())
count = 0
for i in range(1,N+1):
    if N % i == 0:
        count += 1
print(count)

print("#################")
# 数値の全探索 3
# 整数 N が素数かどうかを判定するプログラムを作成してください。
# ただし次の条件を満たすとき「 N は素数である」と言います。
# N は 2 以上の整数である
# N を割り切ることのできる 1 より大きい整数は N のみである

N = int(input())
ans = "Yes"
if N <= 1:
    ans = "No"
else:
    for i in range(2,N):
        if N % i == 0:
            ans = "No"
print(ans)

print("#################")
# 数値の全探索 4
# 整数 A と B の最大公約数を出力するプログラムを作成してください。
# ただし次の条件を満たすとき「 X は A と B の最大公約数である」と言います。
# 条件：X は A も B も割り切る 1 以上の整数の中で最大のものである

A, B = map(int, input().split())
num = []
for i in range(1, min(A,B)+1):
    if A % i == 0 and B % i == 0:
        num.append(i)
print(max(num))

print("#################")
# 数値の全探索 5
# 正の整数 N が与えられます。 1 以上 N 以下の整数 i について、次の問題に答えてください。
# i が 3 でも 5 でも割り切れるならば FizzBuzz を出力し、
# それ以外で i が 3 で割り切れるならば Fizz を出力し、
# それ以外で i が 5 で割り切れるならば Buzz を出力し、
# i がどちらでも割り切れないならば i 自身を出力してください

N = int(input())
for i in range(1, N+1):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)

print("#################")
# 文字列の全探索 1
# S という文字列に文字cが含まれているかどうかを判定してください。

S = str(input())
c = str(input())
# 文字数の取得
size = len(S)
flag = False
for i in range(size):
    if S[i] == c:
        flag = True
if flag:
    print("Yes")
else:
    print("No")

print("#################")
# 文字列の全探索 2
# 英小文字からなる文字列 S が与えられます。
# 文字列 S が回文かどうかを判定するプログラムを作成してください。 なお文字列 S が回文であるとは、S を逆から読んでも S になることを言います。
S = input()
size = len(S)
flag = "Yes"
for i in range(size):
    if S[i] != S[(size - 1) - i]:
        flag = "No"
        break

print(flag)

print("#################")
# 文字列の全探索 3
# 英小文字からなる文字列 S が与えられます。
# 文字列 S 中に「連続する 2 文字が同じ文字である箇所」が何個あるかを答えるプログラムを作成してください。
S = input()
size = len(S)
count = 0
# sizeのままだと最後の参照先が存在しないので-1してif内で+1して整合性を保つ
for i in range(size - 1):
    if S[i] == S[i + 1]:
        count += 1
print(count)

print("#################")
# 文字列の全探索 4
# 英小文字からなる長さ N の文字列 S, T が与えられます。
# 文字列 S の何文字かを書き換えることで、文字列 T に一致させたいものとします。 置き換える必要のある文字数を答えるプログラムを作成してください。
N = int(input())
S = input()
T = input()
count = 0
for i in range(N):
    if S[i] != T[i]:
        count += 1
print(count)

print("#################")
# 文字列の全探索 5
# 英小文字からなる文字列 S (長い) と T (短い) が与えられます。
# 文字列 S の中に、文字列 T が含まれるかどうかを判定してください。 たとえば、次の通りです。
# algomethod は go を含みます
# algomethod は met を含みます
# algomethod は ago を含みません (l が挟まっています)
S = input()
T = input()
if T in S:
    print("Yes")
else:
    print("No")

# 以下正解例
# データを受け取る
S = input()
T = input()

# S, T の長さを取得する
N = len(S)
M = len(T)

# 線形探索 (0 から N-M まで)
flag = False
for i in range(N-M+1):
    if S[i:i+M] == T:
        flag = True

# 答えを出力する
if flag: print("Yes")
else: print("No")

print("#################")
# 二重ループの全探索 1
# N 個の整数A0 ~ An-1
# N 個の整数の中に素数がいくつあるか調べるプログラムを作成してください。

N = int(input())
A = list(map(int, input().split()))
count = 0
for x in A:
    flag = True
    if x == 1:
        flag = False
    else:
        for i in range(2,x):
            if x % i == 0:
                flag = False
        if flag:
            count += 1
print(count)

print("#################")
# 二重ループの全探索 2
# 1 以上の整数 N, K が与えられます。
# 1 以上 N 以下の整数の中で約数をちょうど K 個持つ数の個数を調べるプログラムを作成してください。
N, K = map(int, input().split())
count = 0 #回答用の個数の変数
for x in range(1,N+1):
    print(str(x)+"の探索")
    yaku = 0 #1とその値自身の約数分
    for i in range(1,x+1):
        if x % i == 0:
            yaku += 1
            print(str(x) + "÷"+ str(i) + "は約数！")
        else:
            print(str(x) + "÷"+ str(i))
    print(str(i) + "の約数は" + str(yaku) + "個")
    if yaku == K:
        count += 1
print(count)

print("#################")
# 二重ループの全探索 3
# 整数 X を文字列としてみると回文になっているとき、「X は回文数である」と呼ぶことにします。
# 整数 L, R が与えられるので、L 以上 R 以下の整数の中に回文数がいくつあるか数えるプログラムを作成してください。
L, R = map(int, input().split())
count = 0
for i in range(L,R+1):
    print("探査している値 = " + str(i))
    S = str(i)
    flag = True
    N = len(S)
    for i in range(N):
        if S[i] != S[(N-1)-i]:
            flag = False
    if flag:
        count += 1

print(count)

print("#################")
# 二重ループの全探索 4
# 英小文字からなる文字列 S が与えられます。
# 文字列 S に使われている英小文字の種類数を答えるプログラムを作成してください。
S = input()
length = len(S)
count = 0
for i in range(length):
    if S[i] in S[i+1:]:
        f = 1
    else:
        count += 1
print(count)

# データを受け取る
S = input()
N = len(S)

# 文字の全探索
count = 0
for x in range(ord('a'), ord('z')+1):
    c = chr(x)
    # S に c が含まれるかを調べる
    flag = False
    for i in range(N):
        if S[i] == c:
            flag = True
    # S に c が含まれるならば 1 を足す
    if flag:
        count += 1

# 答えを出力する
print(count)

print("#################")
# 二重ループの全探索 5
# 英小文字からなる N個の文字列S0 ~ Sn-1
# N 個の文字列のうち回文の個数を数えるプログラムを作成してください。
N = int(input())
S = [input() for _ in range(N)] # 縦に受け取る場合はこう書く
count = 0
for x in S:
    flag = True
    N = len(x)
    for i in range(N):
        if x[i] != x[(N-1)-i]:
            flag = False
    if flag:
        count += 1

print(count)

print("#################")
# 複数の配列の全探索 1
# N 個の整数 A0~ An-1 と M 個の整数 B0 ~ Bn-1
# 次の条件を満たす組 (i,j) の個数を答えるプログラムを作成してください。
# i は 0 以上 N−1 以下の整数
# j は 0 以上 M−1 以下の整数
# A i>B j

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

count = 0
for x in A:
    for y in B:
       if x > y:
           count += 1

print(count)

print("#################")
# 複数の配列の全探索 2
# N 個の整数 A0~ An-1 と K 個の整数 B0 ~ Bn-1
# 次の条件を満たす組 (i,j) の個数を答えるプログラムを作成してください。
# i は 0 以上 N−1 以下の整数
# j は 0 以上 M−1 以下の整数
# Ai + Bj = K

# データを受け取る
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

count = 0
for a in A:
    for b in B:
       if a + b == K:
           count += 1

print(count)

print("#################")
# 複数の配列の全探索 3
# X 個の整数 A0~ An-1 と Y 個の整数 B0 ~ Bn-1 と　Z 個の整数 C0 ~ Cn-1
# 次の条件を満たす組 (i,j,k) の個数を答えるプログラムを作成してください。
# i は 0 以上 X−1 以下の整数
# j は 0 以上 Y−1 以下の整数
# k は 0 以上 Z−1 以下の整数
# Ai +Bj =Ck

X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

count = 0
for x in A:
    for y in B:
        for z in C:
            if x + y == z:
                count += 1

print(count)

print("#################")
# ペアの全探索 1
# N 個の整数 A0~An-1,と整数 K が与えられます。
# これらの N 個の整数から、和が K 以下となるように 2 つの数を選ぶ方法は何通りあるか求めるプログラムを作成してください。
# ただし選んだ 2 つの整数の添字 (Ai の i) が等しくなってはいけないものとします。

N, K = map(int, input().split())
A = list(map(int, input().split()))

count = 0
for i in range(N):
    for j in range(i+1,N):
        if A[i] + A[j] <= K:
            count += 1

print(count)


print("#################")
# ペアの全探索 2
# 2 つの整数 L,R が与えられます。
# L 以上 R 以下の整数の中から、 一の位が等しくなるように相異なる 2 つの整数を選ぶ方法は何通りあるか求めるプログラムを作成してください。

L, R = map(int, input().split())

count = 0
for i in range(L,R+1):
    for j in range(i+1,R+1):
        if i % 10 == j % 10:
            count += 1

print(count)

print("#################")
# ペアの全探索 3
# N 個の整数 A0~ An-1
# 以下の条件をみたす整数の組 (i,j,k) の個数を求めるプログラムを作成してください。
# Ai,Aj,Akの最大値は Ajである。
# 0≤i<j<k≤N−1

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if A[j] == max(A[i], A[j], A[k]):
                ans += 1
print(ans)

print("#################")
# ペアの全探索 4
# N 個の文字列 S0~Sn-1
# これらの N 個の文字列の中に同じ 2 つの文字列があるかどうかを判定するプログラムを作成してください。

N = int(input())
S = [input().split() for _ in range(N)]

flag = "No"
for i in range(N):
    for j in range(i+1,N):
        if S[i] == S[j]:
            flag = "Yes"

print(flag)

print("#################")
# ペアの全探索 5
# 長さ N の文字列 S が与えられます。
# 以下の条件をみたす整数の組 (x,y) の個数を数えるプログラムを作成してください。
#
# S の x 文字目と y 文字目は等しい
# 0≤x<y≤N−1
# ただし、S の先頭の文字が 0 文字目であるとします。

N = int(input())
S = input()

count = 0
for i in range(N):
    for j in range(i+1,N):
        if S[i] == S[j]:
            count += 1

print(count)

print("#################")
# 同じ部屋にいた時間
# ある日、学生の A さんと B さんは同じ自習室を利用しました。
# A さんは時刻 sAから時刻 tAまでの間自習室を利用しました。
# また、 B さんは時刻 sBから時刻 tBまでの間自習室を利用しました。
# 2 人が同時に自習室を利用した時間の長さを答えてください。


sa, ta = map(int, input().split())
sb, tb = map(int, input().split())
ans = 0
for i in range(1, 101):
    if sa<=i and i<ta and sb<=i and i<tb:
        ans+=1
print(ans)

print("#################")
# 正の整数 N が与えられます。
# 各整数 n=1,2,…,N に対して、順に以下の処理をしてください。
# n が 4 の倍数ならば、Fizz と一行に出力する
# n が 6 の倍数ならば、Buzz と一行に出力する
# ただし、n が 4 の倍数でも 6 の倍数でもあるならば、FizzBuzz と一行に出力する
# それ以外の場合は、そのままの整数 n を一行に出力する

N = int(input())
for n in range(1, N + 1):
    if n % 4 == 0 and n % 6 == 0:
        print("FizzBuzz")
    elif n % 4 == 0:
        print("Fizz")
    elif n % 6 == 0:
        print("Buzz")
    else:
        print(n)

print("#################")
# 市松模様
# H×Wのマス目を市松模様に塗りたいとします。具体的には次のように塗ります。 なおここで、上からx行目(0始まり)、左からy列目(0始まり) のマスを(x, y)と表すことにします。
# 各マスを「黒色」か「白色」のいずれかに塗るマス(0, 0)は黒色に塗る
# どの隣接する2マスも、一方が黒色で他方が白色になるように塗る
# この条件を満たすように各マスの色を塗ったとき、マス(p, q)
# の色が何色になるかを答えてください。

H, W, p, q = map(int, input().split())
if (p + q) % 2 == 0:
    print("Black")
else:
    print("White")

print("#################")
# うるう年判定
# 私たちが普段使っているグレゴリオ暦には、季節と暦のずれを補正するために平年より 1 日多いうるう年が存在します。
# うるう年は次の規則に従って定められています：
# 西暦年が 4 の倍数の年は (原則) うるう年である
# ただし、西暦年が 100 の倍数の年は (原則) うるう年でない
# ただし、西暦年が 400 の倍数の年は必ずうるう年である
# 例えば、 2020 年は 1. のみを満たすのでうるう年です。
# 西暦 N 年はうるう年でしょうか。
N = int(input())

ans = 'No'
if N % 4 == 0:
    ans = 'Yes'
    if N % 100 == 0:
        ans = 'No'
        if N % 400 == 0:
            ans = 'Yes'
print(ans)

print("#################")
# 勤怠管理システム
# 簡単な勤怠管理システムを作成してみましょう。
# ある人のとある月の勤怠情報が与えられます。
# この月は 30 日まであり、 i 日の就労時間は Hi,1時 Mi,1分から Hi,2時 Mi,2分でした。
# ただし、日を跨いで就労した日はありません。また、就労しなかった日は (Hi,1,Mi,1,Hi,2,Mi,2)=(0,0,0,0) が入力されます。 (1≤i≤30)
# 就労時間が 6 時間より長く 8 時間以下の日は 45 分が、 8 時間より長い日は 1 時間が休憩時間として就労時間から差し引かれ、この時間が労働時間となります
# この人のこの月の合計労働時間を計算するプログラムを作成してください。
# なお、1 時間は 60 分であると考えます。
ans = 0
for i in range(30):
    H1, M1, H2, M2 = map(int, input().split())
    if H1 == M1 == H2 == M2 == 0:
        continue
    m = 60 * (H2 - H1) + M2 - M1
    if 360 < m <= 480:
        m -= 45
    elif m > 480:
        m -= 60
    ans += m
print(ans // 60, ans % 60)

print("#################")
# 注文
# カメのアルルは近所のお店で外食をしています。 このお店には、N 個のメニューがあり、それぞれメニュー名はF0 Fn-1
# またメニューFi Ci円です。
# アルルはこのお店で、M 個のメニュー (それぞれのメニュー名は X0 Xm-1)を注文しました。
# アルルが注文したメニューの合計金額を計算するプログラムを作成してください。
N, M = map(int, input().split())

menu = {}
for _ in range(N):
    F, C = input().split()
    menu[F] = int(C)

X = list(input().split())

ans = 0
for item in X:
    ans += menu[item]
print(ans)

print("#################")
# 約分
# 与えられた分数を既約分数(これ以上約分できない形)に変換するプログラムを作成してください
# 例えば、 2/6 という分数を入力すると 1/3 を出力するプログラムを作成してください。
def GCD(A, B):
    if B == 0: return A
    else: return GCD(B, A % B)

S = input()
for i in range (len(S)):
    if S[i] == "/":
        n0 = int(S[0 : i])
        d0 = int(S[i + 1 : ])

g = GCD(n0, d0)
n1 = n0 // g
d1 = d0 // g
print("%d/%d" % (n1, d1))

print("#################")
# アイスの棒
# カメのアルルはお店にアイスを買いにきました。 このアイスは食べ終わった M 本の棒をまとめてお店に持っていくと、 新たなアイス 1 本に無料で引き換えてもらえます。
# アルルが N 本のアイスを買うとき、最大で何本のアイスを食べることができますか。 ただし、アルルははじめアイスの棒を 1 本も持っていません。

N, M = map(int, input().split())

now = N
loop = 0
while now >= M:
    now -= M
    now += 1
    loop += 1

print(N + loop)

print("#################")
# 曜日計算
# カメのアルルの住む世界では、私たちと違った暦が使われています。
# 1 年は 1 月から A 月までの A 個からなり、 1 つの月は常に 1 日から B 日までの B 個からなります。 また、曜日は C 種類あり、曜日 x の次の日の曜日は曜日 x+1 です (1≤x≤C−1) 。
# ただし、曜日 C の次の日の曜日は曜日 1 です。
# アルルの住む世界において、Y0年 M0月 D0日の曜日は曜日 X です。
# アルルの住む世界における Y1年 M1月 D1日の曜日を答えてください。
def days(y, m, d, A, B, C):
    return (y - 1) * (A * B) + (m - 1) * B + (d - 1)

A, B, C = map(int, input().split())
y0, m0, d0, x = map(int, input().split())
y1, m1, d1 = map(int, input().split())

t0 = days(y0, m0, d0, A, B, C)
t1 = days(y1, m1, d1, A, B, C)
x -= 1
ans = (x + (t1 - t0) % C) % C
ans +=1
print(ans)

print("#################")
# 二番目に大きい値
# N 個の整数 A0,An-1
# これらの整数のうち、大きい方から数えて 2 番目に大きい整数値を答えてください。 ただし、最大となる整数が複数個ある場合は、最大値と、2 番目に大きい整数値が等しくなることに注意しましょう。
# たとえば次のようになります。
# A=[1,5,3,7] のとき、2 番目に大きい数は 5 になります
# A=[5,7,5,7,7] のとき、2 番目に大きい数は 7 になります
N = int(input())
A = list(map(int, input().split()))

M0 = M1 = 0
for a in A:
    if M1 < a:
        M1 = a
    if M0 < M1:
        M0, M1 = M1, M0
print(M1)

print("#################")
# 累積最大値
# N 個の正の整数からなる数列 A0 An-1
# i=1,2,…,N に対して、次の問に答えてください。数列A の先頭からi 項についての最大値を求めてください。つまり
# max(A0, Ai-1)
# の値を求めてください。
N = int(input())
A = list(map(int, input().split()))

M = 0
for item in A:
    M = max(M, item)
    print(M)

print("#################")
# 累積最大値個数
# N 個の正の整数からなる数列 A0 ~ AN-1
# i=1,2,…,N に対して、次の問に答えてください。
# 数列 A の先頭からi 項について「最大値の個数」を求めてください。
# Mi = max(A0~ Ai-1)としたとき、A0~Ai-1の中にMiが何個有るのか
# 入力データを受け取る
N = int(input())
A = list(map(int, input().split()))

# 答えを求める途中経過を表す変数
max_value = 0;  # 最大値
max_num = 0;  # 最大値の個数

# 最大値の個数を求める途中経過を出力していく
for item in A:
    # 数が最大値のとき、個数を 1 増やす
    if item == max_value:
        max_num += 1

    # 最大値を更新するときは、個数を 1 にリセットする
    if item > max_value:
        max_value = item
        max_num = 1

    # 出力する
    print(max_num)

print("#################")
# 正規表現 1-1
# 文字列 S が与えられます。
# 文字列 S が algo という文字列を含むか判定するプログラムを作成してください。

import re

S = input()
reg = r'algo'

search = re.search(reg, S)
if search:
    print("Yes")
else:
    print("No")

print("#################")
# 正規表現 1-2
# 文字列Sが与えられます。
# 文字列Sが以下の形式を満たすか判定するプログラムを作成してください。
import re

S = input()
reg = r'^metho+d$'

search = re.search(reg, S)
if search:
    print("Yes")
else:
    print("No")

print("#################")
# 正規表現 1-3
# 文字列 S が与えられます。
# 文字列 S が以下の形式を満たすか判定するプログラムを作成してください。
import re

S = input()
reg = r'^a{1,5}b{10}c*$'

search = re.search(reg, S)
if search:
    print("Yes")
else:
    print("No")

print("#################")
# 正規表現 1-4
# 文字列 S が与えられます。
# 文字列 S が cat または dog という文字列を含むか判定するプログラムを作成してください。
import re

S = input()
reg = r'cat|dog'

search = re.search(reg, S)
if search:
    print("Yes")
else:
    print("No")

print("#################")
# 正規表現 2-1
# 文字列 S が与えられます。
# 文字列 S が 1+1 という文字列を含むか判定するプログラムを作成してください。

import re

S = input()
reg = r'1\+1'

search = re.search(reg, S)
if search:
    print("Yes")
else:
    print("No")

print("#################")
# 正規表現 2-2
# 文字列 S が与えられます。
# 文字列 S に括弧書きが含まれるか判定するプログラムを作成してください。
# ただし、括弧書きは「 ( と ) で挟まれた 1 文字以上の文字列 」のこととします。

import re

S = input()
reg = r'\(.+\)'

search = re.search(reg, S)
if search:
    print("Yes")
else:
    print("No")

print("#################")
# 正規表現 2-3
# 文字列 S が与えられます。
# 文字列 S が 英文として成立しているか判定するプログラムを作成してください。
# ただし、以下の条件をみたすとき「英文として成立している」とします。

import re

S = input()
reg = r'^([a-z]+\-)*[a-z]+$'

search = re.search(reg, S)
if search:
    print("Yes")
else:
    print("No")

print("#################")
# 正規表現 3-1
# 文字列 S が与えられます。
# 文字列 S が数字を含むか判定するプログラムを作成してください。
import re

S = input()
reg = r'\d'

search = re.search(reg, S)
if search:
    print("Yes")
else:
    print("No")

print("#################")
# 正規表現 3-2
# 文字列 S が与えられます。
# 文字列 S が位置が連続する 3 文字以上の数字を含むか判定するプログラムを作成してください。
import re

S = input()
reg = r'\d{3,}'

search = re.search(reg, S)
if search:
    print("Yes")
else:
    print("No")

print("#################")
# 正規表現 3-3
# 文字列 S が与えられます。
# 文字列 S が以下の形式を満たすか判定するプログラムを作成してください。
# (数字が 3 つ) - (数字が 4 つ)
import re
S = input()
reg = r'^\d{3}\-\d{4}$'

search = re.search(reg, S)
if search:
    print("Yes")
else:
    print("No")

print("#################")
# 正規表現 3-4
# 文字列 S が与えられます。
# 文字列 S が以下の形式を満たすか判定するプログラムを作成してください。
# (1 文字以上の半角英数字)@ (1 文字以上の半角英数字). (1 文字以上4 文字以下の半角英数字)
import re

S = input()
reg = r'^\w+\@\w+\.\w{1,4}$'

search = re.search(reg, S)
if search:
    print("Yes")
else:
    print("No")

print("#################")
# 正規表現 4-1
# 英小文字のみからなる文字列 S が与えられます。
# 文字列 S のうち、r に挟まれた(両隣の文字が r である) u を a に置換するプログラムを作成してください。
import re

S = input()

print(re.sub(r'ru(?=r)', 'ra', S))

print("#################")
# 正規表現 4-2
# 空白区切りの複数単語からなる英文字列 S が与えられます。
# 文字列 S の中にある asian という単語のあとに 5 単語以上が続くならば、その asian を global に置き換えた文字列を出力してください。
import re

S = input()

print(re.sub(r'asian(?=( [a-z]+){5,})', 'global', S))

print("#################")
# 正規表現 4-3
# 英小文字のみからなる文字列 S が与えられます。
# 文字列 S のなかに、algo のあとに来るのが rithm でも method でもないような、algo + 5 文字以上の文字からなる部分文字列が含まれているかを答えてください。
import re

S = input()
reg = r'algo(?!method)(?!rithm)[a-z]{5,}'

search = re.search(reg, S)
if search:
    print("Yes")
else:
    print("No")

print("#################")
# 正規表現 4-4
# カメのアルルは確定申告に備えて、すべての領収書を次のようなタイトルで保存しています。
# 整理番号_領収書名_YYYYMMDD.pdf
# アルルに代わって、大量の領収書の中からある年ある月のレシートの領収署名を抽出してください。
# ※ ここで、「YYYYMMDD」は西暦 4 桁の年・2 桁の月・2 桁の日の合計 8 桁からなる、ある特定の日付を表す数字列のことです。
import re
n, y, m = map(int,input().split())
for _ in range(n):
	s = input()
	match_obj = re.search(r'[^_]+(?=_' + str(y).zfill(4) + str(m).zfill(2) + '\d{2}\.pdf)', s)
	if match_obj:
		print(match_obj.group(0))

print("#################")
# 1-1. テーブル
# 顧客情報をはじめとしたさまざまなデータを、管理したり分析するために蓄積された情報や蓄積のための仕組みをデータベース (DB) と呼びます。 特に、現在広く用いられるデータベースはリレーショナルデータベース (RDB) と呼ばれるもので、次のように構成されています。
# RDB にはいくつかのテーブル (表)が入っており、それぞれにはテーブル名がついている。
# テーブルには、1 行あたり 1 つのデータが格納される。
SELECT
    *
FROM
    prefectures;

print("#################")
# 1-2. カラム
# 都道府県の情報が格納されている、 prefectures テーブルのみをもつデータベースが与えられます。
# prefectures テーブルの id カラム (列) と name カラム (列) の情報を取得し表示するクエリを作成してください。 ただし、name カラムのカラム名は 都道府県名 に変更して表示してください。
SELECT
    id,
    name AS "都道府県名"
FROM
    prefectures;

print("#################")
# 1-3. カラム
# 都道府県の情報が格納されている、 prefectures テーブルのみをもつデータベースが与えられます。
# prefectures テーブルに含まれる、人口が 1,000,000 人未満 の都道府県の情報を全て表示するクエリを作成してください。
SELECT
    *
FROM
    prefectures
WHERE
    population < 1000000;

print("#################")
# 1-4. カラム
# 都道府県の情報が格納されている、 prefectures テーブルのみをもつデータベースが与えられます。
# prefectures テーブルに含まれるデータを、面積が大きい順に並び替えたときの上位 10 件を出力するクエリを作成してください。

SELECT
    *
FROM
    prefectures
ORDER BY
    area DESC LIMIT 10;

print("#################")
# 1-5. 島
# 都道府県の情報が格納されている、 prefectures テーブルのみをもつデータベースが与えられます。
# prefectures テーブルに含まれるデータのうち、都道府県名に「島」が含まれる都道府県を抽出して、すべての情報を表示するクエリを作成してください。
SELECT
    *
FROM
    prefectures
WHERE
    name LIKE '%島%';

print("#################")
# 1-6. 夏の気温
# 日本全国にはアメダスが約 1300 箇所設置されており、降水量等のみを計測するものを除いた 900 箇所ほどでは、常に気温が観測されています。
# この観測地点ごと、8 月の平均最高気温と平均最低気温が格納されている temperature_august テーブルのみをもつデータベースが与えられます。
# これに格納されている最高気温のうち最大のものと、最低気温のうち最小のものを取得し、 前者を 最高気温、後者を 最低気温 というカラム名で一行に表示するクエリを作成してください。
SELECT
    MAX(highest) AS '最高気温',
    MIN(lowest) AS '最低気温'
FROM
    temperature_august;

print("#################")
# 1-7. 人口密度ランキング
# 都道府県の情報が格納されている、 prefectures テーブルのみをもつデータベースが与えられます。
# prefectures テーブルに含まれるデータについて、各データの id, name, 人口密度 [人/㎢]の情報を、人口密度 [人/㎢]が高い順に表示するクエリを作成してください。 ただし、name カラムの名前は 都道府県名 に変更し、人口密度を表すカラムの名前は 人口密度 として表示してください。
SELECT
    id,
    name AS '都道府県名',
    population / area AS '人口密度'
FROM
    prefectures
ORDER BY
    `人口密度` DESC;

print("#################")
# 2-1. 副問い合わせ
# 都道府県の情報が格納されている prefectures テーブルと、 関東地方の都道府県の名前が name カラムに格納されている kanto_regions テーブルをもつデータベースが与えられます。
# 関東地方の都道府県を抽出して、それらの prefectures テーブル内のすべての情報を表示するクエリを作成してください。
SELECT
    *
FROM
    prefectures
WHERE name IN (
    SELECT name FROM kanto_regions
);

print("#################")
# 2-2. 地方データ
# 日本の都道府県は、関東地方や四国地方をはじめとした 9 つの地方にそれぞれ分類されます。 この問題では、都道府県データをもとに地方データを集計してみましょう。
# 都道府県の情報が格納されている prefectures テーブルをもつデータベースが与えられます。
# 各都道府県のデータを地方 (region) ごとに集計し、地方ごとの都道府県数と総面積 [㎢] のデータを総面積の大きい順に表示するクエリを作成してください。 ただし、region カラムの名前は 地方名 に変更し、都道府県数と総面積を表すカラムの名前はそれぞれ 都道府県数 と 総面積 として表示してください。
SELECT
    region AS '地方名',
    COUNT(*) AS '都道府県数',
    SUM(area) AS '総面積'
FROM
    prefectures
GROUP BY
    region
ORDER BY
    `総面積` DESC;

print("#################")
# # # 2-3. 茨「城」県
# カメのアルルは、都道府県の情報が格納されている prefectures テーブルをもつデータベースを作成しました。 しかし、アルルはおっちょこちょいなので、茨城県を誤って「茨木県」と記入し、鳥取県を誤って「取鳥県」と記入してしまいました。
UPDATE prefectures SET name = '茨城県' WHERE name = '茨木県';
UPDATE prefectures SET name = '鳥取県' WHERE name = '取鳥県';
SELECT
    *
FROM
    prefectures;

print("#################")
# 2-4. 四国のデータ
# カメのアルルは、都道府県の情報が格納されている prefectures テーブルをもつデータベースを作成しました。 しかし、カメのアルルはおっちょこちょいなので、四国を構成する 4 つの県のデータを作成するのを忘れてしまいました。
# 次の処理を行い、データベースを正しく変更した上で、全ての都道府県のデータを id が小さい順に出力するクエリを実行してください。
# 次の 4 つの県のデータをデータベースに追加する。
# 徳島県 (id: 36, 面積: 4146 [㎢], 人口: 720,000 [人])
# 香川県 (id: 37, 面積: 1876 [㎢], 人口: 950,000 [人])
# 愛媛県 (id: 38, 面積: 5675 [㎢], 人口: 1,335,000 [人])
# 高知県 (id: 39, 面積: 7102 [㎢], 人口: 692,000 [人])
INSERT INTO
    prefectures
VALUES
    (36, '徳島県', 4146, 720000),
    (37, '香川県', 1876, 950000),
    (38, '愛媛県', 5675, 1335000),
    (39, '高知県', 7102, 692000);
SELECT
    *
FROM
    prefectures
ORDER BY
    id;

print("#################")
# 2-5. アルゴ県
# カメのアルルは、都道府県の情報が格納されている prefectures テーブルをもつデータベースを作成しました。 しかし、アルルはおっちょこちょいなので、テスト用に作ったデータを削除し忘れています。
# 次の処理を行い、データベースを正しく変更した上で、全ての都道府県のデータを出力するクエリを実行してください。
# id の値が 0 であるか 48 以上であるデータを削除する。
DELETE FROM
    prefectures
WHERE
    id = 0 OR id >= 48;
SELECT
    *
FROM
    prefectures;

print("#################")
# 2-6.お得意様
# カメのアルルがアルバイトをしているお店では、データベースを用いて台帳を管理しています。 このお店ではある期間内に一定以上の金額の買い物をした「お得意様」にはさまざまな特典を付与するキャンペーンを行なっています。
# アルルは、データベースから 2022年8月8日から8月14日の1週間で 5,000 円以上の買い物をした「お得意様」を抽出する仕事を任されました。
# 顧客の購入履歴情報が格納されている ledger テーブルをもつデータベースが与えられます。 顧客ごとに8月8日から8月14日の間に購入した金額を集計し、「お得意様」の名前を表示するクエリを作成してください。
# ただし、name カラムの名前は 顧客名 に変更し、期間内の合計購入金額を表すカラムの名前は 合計金額 として表示してください。

SELECT
    name AS '顧客名',
    SUM(amount) AS '合計金額'
FROM
    ledger
WHERE
    DATE(date) BETWEEN '2022-08-08' AND '2022-08-14'
GROUP BY
    name
HAVING
    `合計金額` >= 5000;

print("#################")
# 2-7. 地方ID
# ここまでの問題は基本的に 1 つのテーブルをもつデータベース対する操作を扱いましたが、一般的にはデータベースには複数のテーブルが含まれています。 特に、複数のテーブルを参照して処理するクエリを用いることは頻繁に行われます。
# 複数のテーブルを参照する一般的な方法はのちの問題で練習しますが、この問題では今まで得た知識を用いて簡単な例に取り組んでみましょう。
# 都道府県の情報が格納されている prefectures テーブルと、地方の情報が格納されている regions テーブルをもつデータベースが与えられます。
# SELECT 句の内部に副問い合わせ文を書くことで、各都道府県のデータについて「都道府県名」と都道府県に対応する「地方名」を表示するクエリを作成してください。
# それぞれの都道府県に対応する地方は、その ID が「都道府県の地方ID (region_id)」に等しい地方です。 また、「都道府県名」と都道府県に対応する「地方名」を表示するカラム名は、それぞれ「都道府県名」「地方名」としてください。

SELECT
    name AS "都道府県名",
    -- 地方IDをもとに地方名を取得
    (
        SELECT
            name
        FROM
            regions
        WHERE
            regions.id = prefectures.region_id
    ) AS "地方名"
FROM
    prefectures;

print("#################")
# 3-1. 2番目に大きい都道府県
# 日本で一番大きい都道府県は北海道ですが、その次に大きい都道府県はどこでしょう。
# 都道府県の情報が格納されている、 prefectures テーブルのみをもつデータベースが与えられます。
# prefectures テーブルに含まれるデータから、面積が 2 番目に大きい都道府県のデータを表示するクエリを作成してください。
SELECT
    *
FROM
    prefectures
ORDER BY
    area DESC
LIMIT 1 OFFSET 1;

print("#################")
# 3-2. 内陸県
# 都道府県の情報が格納されている、 prefectures テーブルのみをもつデータベースがあります。
# 回答欄に用意されたクエリを完成させ、内陸県のデータを面積が大きい順に表示してください。
# ただし、内陸県とは海に面していない都道府県を指し、具体的には次の 8 つが当てはまります。
# 栃木県, 群馬県, 埼玉県, 山梨県
# 長野県, 岐阜県, 滋賀県, 奈良県

WITH
    inland_prefectures
AS (
    -- ここに適切なクエリを記述してください
    SELECT *
    FROM prefectures
    WHERE name IN (
        '栃木県', '群馬県', '埼玉県', '山梨県',
        '長野県', '岐阜県', '滋賀県', '奈良県'
    )
)

SELECT
    *
FROM
    inland_prefectures
ORDER BY
    area DESC;

print("#################")
# 3-3. 試験評価
# ある学校の期末成績情報が格納されている、 grades テーブルのみをもつデータベースが与えられます。
# この学校では各々の成績に対して、点数に応じて次のような 5 段階の「評価」が付けられます。
# 点数	90～100	80～89	65～79	50～64	0～49
# 評価	秀	優	良	可	不可

SELECT
    id,
    name,
    subject,
    score,
    CASE
        WHEN score BETWEEN 90 AND 100 THEN '秀'
        WHEN score BETWEEN 80 AND 89 THEN '優'
        WHEN score BETWEEN 65 AND 79 THEN '良'
        WHEN score BETWEEN 50 AND 64 THEN '可'
        ELSE '不可'
    END AS '評価'
FROM
    grades;

print("#################")
# 3-4. 年齢3区分
# 年齢別の人口構造を端的に表す指標として、 0 から 14 歳を「年少人口」、15 から 64 歳を「生産年齢人口」、 65 歳以上を「老年人口」と区分する 年齢3区分 があります。
# いま、年齢 1 歳ごとの日本の人口を表す population テーブルが与えられます。 この年齢3区分に当てはまる人口がそれぞれ何人か、集計して表示するクエリを作成してください。
# ただし、年齢3区分が格納されるカラム名を「年齢3区分」、各区分の人口が格納されるカラム名を「総人口」としてください。 また、表示結果において年齢3区分が表示される順序は問わないものとします。

SELECT
    CASE
        WHEN age BETWEEN 0 AND 14 THEN '年少人口'
        WHEN age BETWEEN 15 AND 64 THEN '生産年齢人口'
        ELSE '老年人口'
    END AS '年齢3区分',
    SUM(total) AS '総人口'
FROM
    population
GROUP BY `年齢3区分`;

print("#################")
# 3-5. 家計簿の分析
# カメのアルルは、支出額を管理するために日常的に家計簿を付けています。
# ある年の 4, 5, 6 月の家計簿データが、それぞれ expenses_april, expenses_may, expenses_june テーブルとして与えられます。
# これら 3 ヶ月間の支出額をカテゴリごとに合計して、支出額の多いカテゴリから順番に表示するクエリを作成してください。
# ただし、カテゴリ名と、カテゴリごとの支出額の合計を表示するカラム名はそれぞれ「カテゴリ」「支出額」としてください。

WITH expenses AS (
    SELECT * FROM expenses_april
    UNION ALL
    SELECT * FROM expenses_may
    UNION ALL
    SELECT * FROM expenses_june
)
SELECT
    category AS 'カテゴリ',
    SUM(amount) AS '支出額'
FROM
    expenses
GROUP BY
    category
ORDER BY
    `支出額` DESC;

print("#################")
# 3-6. 参加者名簿
# カメのアルルは 3 日間開催されるイベントに参加しました。 このイベントは各日出し物が異なるため、参加者は興味にあわせて出し物ごとに参加登録をします。
# このイベントの 1 日目 から 3 日目の参加登録情報が、それぞれ registrations_day1, registrations_day2, registrations_day3 テーブルとして与えられます。
# イベントに 3 日とも登録した参加者のメールアドレスを全て取得して表示するクエリを作成してください。
# ただし、このメールアドレスが格納されるカラムのカラム名は email としてください。
SELECT email FROM registrations_day1
INTERSECT
SELECT email FROM registrations_day2
INTERSECT
SELECT email FROM registrations_day3;

print("#################")
# 3-7. 景品の対象者
# カメのアルルたちは一定期間内に様々な課題に挑戦できる、インターネット上のイベントに参加しました。 このイベントでは、参加者ごとに挑戦した課題の合計点が集計され、その合計点が高い 10 名に景品が授与されます。
# このイベントにおける課題の挑戦結果が results テーブルに与えられます。
# また、一部の挑戦結果を集計に使わないで欲しいと参加者が申し出ています。このオプトアウト情報が optout テーブルに与えられます。 optout テーブルの email, game_id, score の組は、それと同じ組を持つレコードが results テーブルに存在することが保証されます。(id は異なる可能性があります。)
# これらのテーブルから、集計対象の結果のみをもとにして合計点を集計し、 景品授与対象 (合計点の上位 10 名) のメールアドレスを取得して表示するクエリを作成してください。
# ただし、このメールアドレスが格納されるカラムのカラム名は email としてください。
WITH ranked_results AS (
    SELECT email, game_id, score FROM results
    EXCEPT
    SELECT email, game_id, score FROM optout
)
SELECT
    email
FROM
    ranked_results
GROUP BY
    email
ORDER BY
    SUM(score) DESC
LIMIT 10;