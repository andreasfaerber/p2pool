FEATHERCOIN P2POOL USERS:

Please use https://github.com/wellenreiter01/p2pool-neoscrypt as a source for a
feathercoin p2pool version. This repository has been merged with the above repository
but will no longer be updated. If it will, it will only merge updates from the 
p2pool-neoscrypt repository.



Requirements:
-------------------------
Generic:
* Python >=2.6
* Twisted >=10.0.0
* python-argparse (for Python =2.6)

Linux:
* sudo apt-get install python-zope.interface python-twisted python-twisted-web
* sudo apt-get install python-argparse # if on Python 2.6

Windows:
* Install Python 2.7: http://www.python.org/getit/
* Install Twisted: http://twistedmatrix.com/trac/wiki/Downloads
* Install Zope.Interface: http://pypi.python.org/pypi/zope.interface/3.8.0
* Install python win32 api: http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/
* Install python win32 api wmi wrapper: https://pypi.python.org/pypi/WMI/#downloads
* Unzip the files into C:\Python27\Lib\site-packages

Running P2Pool:
-------------------------
To use P2Pool, you must be running your own local coin daemon. For standard
configurations, using P2Pool should be as simple as:

    python run_p2pool.py

Then run your miner program, connecting to 127.0.0.1 on the default worker
port with any username and password.

If you are behind a NAT, you should enable TCP port forwarding on your
router. Forward port 9333 to the host running P2Pool.

Run for additional options.

    python run_p2pool.py --help

Official wiki :
-------------------------
https://en.bitcoin.it/wiki/P2Pool

Alternate web front end :
-------------------------
* https://github.com/hardcpp/P2PoolExtendedFrontEnd

Notes for NeoScrypt:
=========================
Requirements:
-------------------------
In order to use P2Pool with any NeoScrypt powered coin, you need to build
and install the NeoScrypt Python module first.

Linux:

    cd neoscrypt
    sudo python setup.py install

Windows (mingw):
* Install MinGW: http://www.mingw.org/wiki/Getting_Started
* Install Python 2.7: http://www.python.org/getit/

In bash type this:

    cd neoscrypt
    C:\Python27\python.exe setup.py build --compile=mingw32 install

Windows (microsoft visual c++)
* Open visual studio console

In bash type this:

    SET VS90COMNTOOLS=%VS110COMNTOOLS%	           # For visual c++ 2012
    SET VS90COMNTOOLS=%VS100COMNTOOLS%             # For visual c++ 2010
    cd litecoin_scrypt
    C:\Python27\python.exe setup.py build --compile=mingw32 install

If you run into an error with unrecognized command line option '-mno-cygwin', see this:
http://stackoverflow.com/questions/6034390/compiling-with-cython-and-mingw-produces-gcc-error-unrecognized-command-line-o

Running P2Pool for Phoenixcoin:
-------------------------------
Run P2Pool with the "--net phoenixcoin" option.
Run your miner program, connecting to 127.0.0.1 on port 10554.
Forward port 10555 on your router to any PXC nodes running P2Pool.

Running P2Pool for Feathercoin:
-------------------------------
Run P2Pool with the "--net feathercoin" option.
Run your miner program, connecting to 127.0.0.1 on port 19327.
Forward port 19339 on your router to any FTC nodes running P2Pool.

Notes for Feathercoin:
=========================
Requirements:
-------------------------
In order to run P2Pool with the Feathercoin network, you would need to build and install the
ltc_scrypt module that includes the scrypt proof of work code that Litecoin uses for hashes.

See "Notes for Litecoin" above on how to install the ltc_script module.

Running P2Pool:
-------------------------
Run P2Pool with the "--net feathercoin" option.
Run your miner program, connecting to 127.0.0.1 on port 19327.
Forward port 19339 to the host running P2Pool.

Feathercoin's use of ports could conflicts with P2Pool running on one of
the Cryptocoin networks. To avoid problems, add these lines to litecoin.conf
and restart litecoind:

    rpcport=11332
    port=11333
=======
Sponsors:
-------------------------

Thanks to:
* The Bitcoin Foundation for its generous support of P2Pool
* The Litecoin Project for its generous donations to P2Pool
 
License:
-------------------------

[Available here](LICENCE)


