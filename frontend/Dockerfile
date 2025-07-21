FROM node:20-alpine

WORKDIR /app

# package.json と package-lock.json を先にコピーしてキャッシュを活用
COPY package.json package-lock.json* ./

# 開発に必要なすべての依存関係をインストール
RUN npm install

# 全てのソースコードをコピー
COPY . .

# 開発サーバーが使用するポートを公開 (Viteのデフォルトは5173, Reactは3000など)
EXPOSE 5173

# 開発サーバーを起動するコマンド
CMD ["npm", "run", "dev"]