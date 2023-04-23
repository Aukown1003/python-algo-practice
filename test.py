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