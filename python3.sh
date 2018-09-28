sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python3.6

# change symlink --> dangerous!!!
cd /usr/bin
sudo rm python
sudo ln -s python3.5 python