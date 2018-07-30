'''
查看提供的(待处理文本.txt)文件 编写代码取出所有图片的网址 住 不需要直接读取文件  把内容复制到代码找中定义为变量即可
'''
import re
s ='''<p align="center"><a target="_blank" href="http://www.gamersky.com/showimage/id_gamersky.shtml?http://img1.gamersky.com/image2018/06/20180616_djy_248_3/gamersky_01origin_01_201861619251A1.jpg"><img class="picact" border="0" alt="游民星空" src="http://img1.gamersky.com/image2018/06/20180616_djy_248_3/gamersky_01small_02_201861619252E7.jpg"></a></p>\
<p align="center"><a target="_blank" href="http://www.gamersky.com/showimage/id_gamersky.shtml?http://img1.gamersky.com/image2018/06/20180616_djy_248_3/gamersky_02origin_03_20186161925574.jpg"><img class="picact" border="0" alt="游民星空" src="http://img1.gamersky.com/image2018/06/20180616_djy_248_3/gamersky_02small_04_2018616192574A.jpg"></a></p>\
<p align="center"><a target="_blank" href="http://www.gamersky.com/showimage/id_gamersky.shtml?http://img1.gamersky.com/image2018/06/20180616_djy_248_3/gamersky_03origin_05_20186161925AF7.jpg"><img class="picact" border="0" alt="游民星空" src="http://img1.gamersky.com/image2018/06/20180616_djy_248_3/gamersky_03small_06_20186161925F0C.jpg"></a></p>\
<p align="center"><a target="_blank" href="http://www.gamersky.com/showimage/id_gamersky.shtml?http://img1.gamersky.com/image2018/06/20180616_djy_248_3/gamersky_04origin_07_201861619251AE.jpg"><img class="picact" border="0" alt="游民星空" src="http://img1.gamersky.com/image2018/06/20180616_djy_248_3/gamersky_04small_08_201861619254F2.jpg"></a></p>\
<p align="center"><a target="_blank" href="http://www.gamersky.com/showimage/id_gamersky.shtml?http://img1.gamersky.com/image2018/06/20180616_djy_248_3/gamersky_05origin_09_20186161925836.jpg"><img class="picact" border="0" alt="游民星空" src="http://img1.gamersky.com/image2018/06/20180616_djy_248_3/gamersky_05small_10_20186161925B7A.jpg"></a></p>\
<p>'''

s = s.replace('<p align="center"><a target="_blank" href="', ' ')
s = s.replace('"><img class="picact" border="0" alt="游民星空" src="', ' ')
s = s.replace('"></a></p><p>', ' ')
s = s.replace('"></a></p>', ' ')
l = s.split()
print(l, len(l))