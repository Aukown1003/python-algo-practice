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
N = int(input())
print(N*2)

print("#################")
# practice2 1-2
# 1 以上 100 以下の整数 N が標準入力から与えられます。
# N を 5 で割ったあまりを標準出力するプログラムを作成してください。
N = int(input())
print(N%5)

print("#################")
# practice2 1-3
# 文字列 S が標準入力から与えられます。
# S を 3 回繰り返してできる文字列を標準出力するプログラムを作成してください。
S = str(input())
print(str(S*3))

print("#################")
# practice2 1-4
# 長さ 5 の文字列 S が標準入力から与えられます。文字列 S の中央の文字を出力してください。
# たとえば入出力例 1 に示す通り、S= power に対しては、文字 w を出力します。
S = str(input())
print(S[2])

print("#################")
# practice2 1-5
# 0 以上 23 以下の整数 X が標準入力から与えられます。
# 現在の時刻が X 時のとき、日が変わる ( 24 時になる) まであと何時間かかるかを計算してください。
X = int(input())
print(24 - X)