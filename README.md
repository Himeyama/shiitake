# shiitake

shiitake は POST リクエストを受け取り、"data" の値をそのまま返すサーバーを立ち上げます。

例えば、

```json
{
    "data": "Hello, world!"
}
```

の場合は、`Hello, world!` を返します。

## 依存パッケージのインストール
```sh
poetry install
```

## 使い方

### 実行
以下のコマンドでサーバーを起動します。

```sh
poetry run python -m shiitake
```

### リクエストを送る
次のコマンドは、サーバーに対し PowerShell でリクエストを送る例です。

```ps1
Invoke-WebRequest -Uri "http://127.0.0.1:8000/api" -Method POST -Body '{"data": "hello, world"}' -ContentType "application/json"
```

## 開発

### 準備
以下のコマンドで、仮想環境の作成およびアクティブ化と依存パッケージをインストールします。

```sh
poetry shell # 仮想環境の作成およびアクティブ化
poetry install # 依存パッケージのインストール
```

### 実行ファイルの生成

```sh
poetry run task build
```
