btc-difficulty
==============

Bitcoin Difficulty Parser

Usage: 'python difficulty.py'

Requires that bitcoind is running in background as daemon so that 'bitcoind getinfo' RPC-style
commands can be passed to it.

This will parse through each block until the last one that exists at the start of the run 
cycle. It will append to the file as well so that only changes will need to be added on
each run. This will be a non-optimized approach to maintaining a personal record of bitcoin
difficulty over time.

This application will work for altcoins as well using ***coind in place of bitcoind. Simply
modify the program as needed. Outputs in tab deliminated format for importing to excel or other
spreadsheet program for plotting.

Bonus points if someone forks this to add matplotlib to generate plots. May do in future.


