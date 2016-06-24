
sudo rm -rf dist/*
./runtests.sh
sudo python setup.py clean --all
sudo python setup.py install
sudo twine upload dist/*
