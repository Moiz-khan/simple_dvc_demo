conda create -n wineq
conda create -n wineq python=3.7 -y
conda activate wineq
touch requirements.txt
pip install -r requirements.txt

git init 

dvc init

dvc add data_given/winequality.csv
