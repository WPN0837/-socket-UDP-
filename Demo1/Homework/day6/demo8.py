# 编写程序实现以下功能
# 		要求用户输入音乐数据 包括 类型,名字,作者,时长,发布时间
# 		每种类型可以有多个音曲目信息(循环录入多个曲目)
# 		输入指定命令可以退出输入
# 		输入完成后
# 			可以按照类型查看音乐
# 			可以按照名称查看音乐
# 			拓展,按照名称查看时 可以模糊查找 例如 输入 气球 可以查看到 告白气球
#
# 	注:先完成录入部分 在完成查看信息部分
#
# 数据样例:
# {
# 	"pop":[
# 			{
# 				"title":"告白气球",
# 				"auth":"周杰伦",
# 				"time":"3:54"
# 				"date":"2017-09-20"
# 			}
# 		],
# 	"rock":[
# 			{
# 				"title":"一无所有",
# 				"auth":"周建",
# 				"time":"4:50",
# 				"date":"1987-10-02"
# 			}
# 		]
# }
song_info = {
	"pop":[
			{
				"title":"告白气球",
				"auth":"周杰伦",
				"time":"3:54",
				"date":"2017-09-20"
			}
		],
	"rock":[
			{
				"title":"一无所有",
				"auth":"周建",
				"time":"4:50",
				"date":"1987-10-02"
			}
		]
}
while True:
    print(
    '''
    0.添加
    1.类型
    2.名称 模糊查找
    '''
    )
    c = input('>>')
    if c == 'quit':
        break
    elif c == '0':
        # "title":"告白气球",
        # "auth":"周杰伦",
        # "time":"3:54"
        # "date":"2017-09-20"
        style = input('音乐类型:')
        title = input('音乐名:')
        auth = input('作者:')
        time = input('时长:')
        date = input('发布时间:')
        song_info.setdefault(style, [])
        song_info[style].append({"title": title, "auth": auth, "time": time, "date": date})
        # if style in song_info:
        #     song_info[style].append({"title": title, "auth": auth, "time": time, "date": date})
        # else:
        #     song_info[style] = [{"title": title, "auth": auth, "time": time, "date": date}]
    elif c == '1':
        style = input('类型:')
        if style in song_info:
            for i in song_info[style]:
                print(i['title'])
        else:
            print('%s类型不存在！' % style)
    elif c == '2':
        title = input('输入音乐名称:')
        for value in song_info.values():
            for i in value:
                if title in i['title']:
                    print(i['title'])
    else:
        print('命令错误！')

