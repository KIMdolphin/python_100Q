name = list(map(str, input().split(' ')))
score = list(map(int, input().split(' ')))

dic = { name:score for name, score in zip(name, score) }
# result = dict(zip(name, score))
