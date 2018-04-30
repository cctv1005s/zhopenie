# -*- coding: UTF-8 -*-`
import sys
from zhopenie.extractor import Extractor

def main(argv):

    data = '语言技术平台(Language Technology Platform，LTP)是 哈工大社会计算与信息检索研究中心 历时十年开发的一整套中文语言处理系统。LTP制定了基于XML的语言处理结果表示，并在此基础上提供了一整套自底向上的丰富而且高效的中文语言处理模块(包括词法、句法、语义等6项中文处理核心技术)，以及基于动态链接库(Dynamic Link Library, DLL)的应用程序接口，可视化工具，并且能够以网络服务(Web Service)的形式进行使用'
    data = data.replace('\n', ' ').replace('\r', '')
    print(data)	
	
    extractor = Extractor()
    extractor.load()
    extractor.chunk_str(data)
    extractor.resolve_all_conference()
    print("Triple: ")
    sudo apt-get install python-dev libxml2-dev libxslt-devprint('\n'.join(str(p) for p in extractor.triple_list))
	
    extractor.release()


if __name__ == "__main__":
	main(sys.argv)
https://github.com/HIT-SCIR/ltp/archive/v3.3.0.zip