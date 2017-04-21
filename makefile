clean:
	rm -f *.pyc *~ example.csv example.png
test:
	echo "Test takes 30 minutes..."
	python timing.py
example:
	echo "Running on 4 cores"
	mpirun -n 4 python pysrim.py --numIons=10 --ionEnergy=100000 --elementIon=P -o example.csv
	python distribution.py example.csv example.png
	echo "Output is file example.csv"
	echo "plot is named example.png"
	display example.png

release: clean
	cd ..; tar -zcvf pysrim.tgz pysrim; mv pysrim.tgz pysrim/.
