# Encoding: utf-8
# Author: bingli
# Date: 2018.12.18
# Description: 每次看书、文档都会忘记页码，每次都会...
# version: 0.0.1

from sys import argv
from os import mkdir, mknod
from os.path import exists


def ISEXISTS(fname, ftype):
    '''
    判断文件存在不存在，不存在就创建
    '''
    if not exists(fname):
        if ftype == 0:
            mkdir(fname)
        elif ftype == 1:
            mknod(fname)


if __name__ == '__main__':
    # 目录名称
    folder = 'note'
    # 文件后缀名
    ext = '.txt'

    # 检测目录文件夹是否存在
    ISEXISTS(folder, 0)
    # 获取输入书籍名称
    fname = raw_input('请输入你要记录的书籍名称：')
    fpath = '%s/%s%s' % (folder, fname, ext)
    # 检测文件是否存在
    ISEXISTS(fpath, 1)

    # 开始文件操作
    txt = open(fpath, 'w')
    print '将会清空: %s' % fpath
    # 确认是否清空文件内容
    isExit = raw_input('是否继续？(Y/n)')
    if isExit.lower() == 'n':
        exit()
    txt.truncate()
    content = raw_input('请输入要记录的页码：')
    txt.write('%s\n\t' % fname + content)
    print '写入完成'
    # 关闭文件
    txt.close()

