// Vue Routerのインポート
//createRouter はルーターインスタンスを作成するための関数。
//createWebHistory は、ブラウザのヒストリーAPIを利用して、URLの履歴を管理するための関数です。これにより、ページ遷移時にURLが変更されます。
import { createRouter, createWebHistory } from 'vue-router';


// ルートコンポーネントのインポート
// これらのコンポーネントは、src/viewsディレクトリ内にあると仮定しています。
import HomeView from '../views/HomeView.vue';
import TodoView from '../views/TodoView.vue';

// ルート定義
// path: URLパスです。このパスにアクセスすると、対応するコンポーネントが表示されます。
// name: ルートに名前を付けることができます。これを使うことで、プログラム的にルートを参照できます。
// component: 対象となる Vue コンポーネントです。HomeView や AboutView コンポーネントが表示されます。
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/todo',
    name: 'todo',
    component: TodoView,
  },
];

// ルーターインスタンスの作成（ルーターオブジェクトを作成する）
// createRouter関数を使って、ルーターインスタンスを作成します。
// createWebHistory関数を使って、ブラウザのヒストリーAPIを利用した履歴管理を行います。
const router = createRouter({
  history: createWebHistory(),
  routes,
});

// ルーターインスタンスをエクスポート
// これにより、Vueアプリケーション全体でルーティング機能を利用できるようになります。
// 例えば、main.jsでVueアプリケーションにルーターを追加する際に使用します。
export default router;