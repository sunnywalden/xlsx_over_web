<template>
  <div class="login-container">
    <a-form ref="formRef" :model="formState" @submit="handleSubmit">
      <a-form-item
        label="Username"
        name="username"
        :rules="[{ required: true, message: 'Please input your username!' }]"
      >
        <a-input v-model:value="formState.username" placeholder="Enter username" />
      </a-form-item>
      <a-form-item
        label="Password"
        name="password"
        :rules="[{ required: true, message: 'Please input your password!' }]"
      >
        <a-input type="password" v-model:value="formState.password" placeholder="Enter password" />
      </a-form-item>
      <a-form-item>
        <a-button type="primary" html-type="submit" class="login-button">Login</a-button>
      </a-form-item>
    </a-form>
    <router-link to="/register" class="register-link">Don't have an account? Register here</router-link>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { Form, Input, Button, message } from 'ant-design-vue';
import type { FormInstance } from 'ant-design-vue/es/form';

const formState = ref({
  username: '',
  password: ''
});

const formRef = ref<FormInstance | null>(null);
const router = useRouter();

const handleSubmit = async (e: Event) => {
  e.preventDefault();
  if (formRef.value) {
    try {
      console.log('Received values of form: ', formState.value);
      const response = await fetch('http://localhost:8000/userlogin', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formState.value),
      });
      if (response.ok) {
        const data = await response.json();
        console.log('Login successful:', data);
        router.push('/productiondashboard'); // Redirect to ProductionDashboard
      } else {
        console.error('Login failed:', response.statusText);
        message.error('Login failed. Please check your credentials.');
      }
    } catch (error) {
      console.error('Validation failed:', error);
      message.error('Please check your form inputs.');
    }
  }
};
</script>

<style scoped>
.login-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.login-button {
  width: 100%;
}
</style>