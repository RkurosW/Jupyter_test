## Jupyter Notebook の設定手順
1. 仮想環境設定
    - venv  
    `python -m venv .venv`
    - アクティベート  
    `. .venv/bin/activate`
2. ライブラリのインストール
    ```
    pip install --upgrade pip
    pip install notebook
    ```
3. ノートの作成  
    (VSCode CommandPallet)  
    Create: New Jupyter Notebook 

:::
問い合わせの際はこちらにご連絡ください
:::  
[Jupyter公式サイト](https://jupyter.org/)

## Git の設定手順
1. 環境変数設定(初回のみ)
```
git config --global user.name "xxxx"
git config --global user.email xxxx@xxxxxx
```
2. ローカルリポジトリ作成
```
git init
```
3. Gitの管理対象外を設定
``` 
touch .gitignore
```
仮想環境のディレクトリを追加

4. ステージング→コミット
```
git add .
git commit -m "コミットコメント"
```

5. GitHubへのコミット
```
git push origin master
```
