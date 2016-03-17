from urllib import request
import myfile

url = 'http://newhouse.njhouse.com.cn/kpgg/'

myfile.save_file('tmp/x0.html', request.urlopen(url).read())


