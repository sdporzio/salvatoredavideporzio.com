DATETIME="$(date +%d%m%y%H%M%S)"

python HouseEnvironment/makePlots.py
git add .
git commit -m "automatic update ${DATETIME}"
git push origin master