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