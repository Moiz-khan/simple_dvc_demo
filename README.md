conda create -n wineq

conda create -n wineq python=3.7 -y

conda activate wineq

touch requirements.txt

pip install -r requirements.txt

git init 

dvc init

dvc add data_given/winequality.csv

git add .

git commit -m "first commit"

git add .

git commit -m "update README file"

git remote add origin "repo url"

git branch -M main

'''bash
git push origin main
'''

dvc repro

git add .

git commit -m "stage 1 complete"

git push origin main

step 
run on other terminal
 mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts --host 127.0.0.1 -p 5000

step 
dvc repro

##changing params and experiment then compare the model and than put it for production