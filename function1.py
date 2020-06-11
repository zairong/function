def wash(dry = False, water = 8):
	print('加水', water, '分滿')
	print('加洗衣精')
	print('浸泡')
	print('洗衣')
	if dry:
		print('烘乾')
wash()
wash(True)
wash(False)
wash(dry = 1) #dry參數為任意直取代dry並執行
wash(water = 10)

#return 回傳結果
def function(numbers):
	return sum(numbers) / len(numbers)
print(function([5, 8, 9]))
print(function([15, 58, 9]))
print(function([5, 98, 79]))

def add(x, y):
	return x + y
print(add(9, 26))
print(add(89, 26))
print(add(779, 426))