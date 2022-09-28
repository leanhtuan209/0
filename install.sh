echo "updating..."
sudo apt -y update
echo "done."

echo "installing... ['screen', 'nodejs']"
sudo apt -y install screen nodejs
echo "done."

echo "installing... ['randomstring', 'request']"
npm i randomstring
npm i request
echo "mdone."

echo "installing... ['httpx', 'requests', 'colorama', 'speedtest-cli']"
pip3 install -r requirements.txt
echo "done."

echo "Executing..."
ulimit -n 999999
cd utils/L4; chmod 777 *; cd ../../
python3 t.py
