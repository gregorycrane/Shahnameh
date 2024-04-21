all:  shahnameh-warn02-index.xml shahnameh-warn02.xml shahnameh.mohl02.xml

shahnameh-warn02-index.xml: warn02-index.txt
	python3 tagind.py > $@

shahnameh-warn02.xml: shahnam-warn02.eng1.txt shahnameh-warn02-index.xml lb.py
	python3 lb.py > shahnameh-warn02a; python3 addind.py  > shahnameh-warn02.xml

shahnameh.mohl02.xml: shahnameh.mohl02.txt fb.py
	python3 fb.py > $@

