n,x,y = map(int, input().split())
a = list(map(int, input().split()))
#先手:- 後手の点数と距離を離したい
#後手:- 先手の点数と出来るだけ近づきたい
#自分が最後のカードを取るのか、相手が最後のカードを取るのかの二択しかない。
#自分がとったほうがいい場合は、自分で取る
#相手がとったほうがいい場合は、相手にとらせる
