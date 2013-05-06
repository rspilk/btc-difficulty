#_,.~'`'~.,_,.~'`'~.,_,.~'`'~.,_,.~'`'~.,_,.~'`'~.,_,.~'`'~.,_,.~'`'~.,#
#                                                                      #
#   Project             :   Bitcoin Difficulty Parser                  #
#                                                                      #
#   Program Name        :   difficulty.py                              #
#                                                                      #
#   Author              :   Tyler Spilker                              #
#                                                                      #
#   Date Created        :   2013-05-06                                 #
#                                                                      #
#   Purpose             :   To iterate through bitcoind calls to       #
#                           gather difficulty of every block           #
#                                                                      #
#_,.~'`'~.,_,.~'`'~.,_,.~'`'~.,_,.~'`'~.,_,.~'`'~.,_,.~'`'~.,_,.~'`'~.,#

# If this helped, please feel free to donate me some coins :)
# BTC : 1Lu5kcCh1vU68XmAT9E9KZZAR4deEhTDr4
# LTC : LcvAhhVPgQxRmoGDnNrCBkWdgz3n2dnEYg

import os, ast, time
path = './blockdiff'
#os.system('echo "" >'+path)
last_line = os.popen("tail -n 1 %s" % path).read().split()

f = open(path,'a')
try:
  last_block = int(last_line[0])
except:
  last_block = 0
 
block_count = int(os.popen("bitcoind getblockcount").read().split()[0])


for i in range(block_count)[last_block:]:
  hash = os.popen("bitcoind getblockhash "+str(i)).read().strip("\n")

  block = ast.literal_eval(os.popen("bitcoind getblock " + hash).read())

  f.write(str(block["height"]+1)+"\t")
  f.write(str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(block["time"]))))+"\t")
  f.write(str(block["difficulty"])+"\n")
  if i%100 == 0:
    print i
f.close()

