import { createRouter, createWebHistory } from 'vue-router';
import LoginForm from '../components/LoginForm.vue';
import RegisterForm from '../components/RegisterForm.vue';
import ProductionDashboard from '../components/ProductionDashboard.vue';
import ProductionManage from '../components/ProductionManage.vue';
import XlsxUploader from '../components/XlsxUploader.vue';

const routes = [
  {
    path: '/',
    name: 'login',
    component: LoginForm
  },
  {
    path: '/register',
    name: 'register',
    component: RegisterForm
  },
  {
    path: '/productiondashboard',
    name: 'productiondashboard',
    component: ProductionDashboard
  },
  {
    path: '/productionmanage',
    name: 'productionmanage',
    component: ProductionManage
  },
  {
    path: '/xlsxuploader',
    name: 'xlsxuploader',
    component: XlsxUploader
  },
  {
    path: '/query',
    name: 'query',
    component: ProductionDashboard
  },
  {
    path: '/index',
    name: 'index',
    component: ProductionDashboard
  },
  {
    path: '/loader',
    name: 'loader',
    component: ProductionDashboard
  },
  {
    path: '/userlogin',
    name: 'userlogin',
    component: LoginForm
  },
  {
    path: '/userregistry',
    name: 'userregistry',
    component: RegisterForm
  },
  {
    path: '/registry',
    name: 'registry',
    component: RegisterForm
  },
  {
    path: '/userlogout',
    name: 'userlogout',
    component: LoginForm
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;