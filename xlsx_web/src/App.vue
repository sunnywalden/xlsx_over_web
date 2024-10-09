<template>
  <div id="app">
    <a-layout>
      <a-layout-header>Header</a-layout-header>
      <a-layout-content>
        <router-view></router-view>
      </a-layout-content>
      <a-layout-footer>Footer</a-layout-footer>
    </a-layout>
  </div>
</template>

<script>
import LoginForm from './components/LoginForm.vue';
import RegisterForm from './components/RegisterForm.vue';
import ProductionManage from './components/ProductionManage.vue';
import XlsxUploader from './components/XlsxUploader.vue';
import ProductionDashboard from './components/ProductionDashboard.vue';
export default {
  name: 'App',
    components: {
        LoginForm,
        RegisterForm,
        ProductionManage,
        XlsxUploader,
        ProductionDashboard
    }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
