import random
print('*'*50)
print('		 欢迎进入游戏')
print('*'*50)
a = input('请输入用户名：')
b = input('请输入密码：')
print('{}恭喜您登陆成功，请充值继续游戏，当前余额为0'.format(a))
c = int(input('请输入充值金额（必须是10的倍数）：'))
while c % 10 == 0 and c != 0:
	print('充值成功，当前余额为{}，请开始游戏！'.format(c))
	print('游戏规则：每局游戏开始扣除2个游戏币，胜利获得3个游戏币，失败则不获得')
	while c >= 2:
		c -= 2
		print('游戏开始扣除2个游戏币，当前余额为{}'.format(c))
		ran = int(random.randint(2,12))
		d = input('请输入您的结果（大或小）：')
		if 1< ran <7:
			e = '小'
		else:
			e = '大'
		if d == e:
			c += 3
			print('游戏胜利，获得3个游戏币,当前余额为{},是否继续游戏？'.format(c),end=' ')
		else:
			print('游戏失败，余额为{}，是否继续游戏？'.format(c),end=' ')
		f = input('')
		if f == '是':
			pass
		else:
			print('游戏结束，余额不退回！！！！！！')
			break
	else:
		print('余额不足退出游戏')		
	break		
else:
	print('充值失败，充值金额必须是10的倍数！！！')
