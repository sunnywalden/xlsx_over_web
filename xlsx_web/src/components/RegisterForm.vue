<template>
  <div class="register-container">
    <a-form ref="regFormRef" :model="regFormState" @submit="handleSubmit">
      <a-form-item
        label="Username"
        name="username"
        :rules="[{ required: true, message: 'Please input your username!' }]"
      >
        <a-input v-model:value="regFormState.username" placeholder="Enter username" />
      </a-form-item>
      <a-form-item
        label="Password"
        name="password"
        :rules="[{ required: true, message: 'Please input your password!' }]"
      >
        <a-input type="password" v-model:value="regFormState.password" placeholder="Enter password" />
      </a-form-item>
      <a-form-item
        label="Confirm Password"
        name="passwd_again"
        :rules="[{ required: true, message: 'Please confirm your password!' }]"
      >
        <a-input type="password" v-model:value="regFormState.passwd_again" placeholder="Confirm password" />
      </a-form-item>
      <a-form-item
        label="Email"
        name="email"
        :rules="[{ required: true, message: 'Please input your email!' }]"
      >
        <a-input v-model:value="regFormState.email" placeholder="Enter email" />
      </a-form-item>
      <a-form-item>
        <a-button type="primary" html-type="submit" class="register-button">Register</a-button>
      </a-form-item>
    </a-form>
    <router-link to="/userlogin" class="login-link">Already have an account? Login here</router-link>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { Form, Input, Button, message } from 'ant-design-vue';
import type { FormInstance } from 'ant-design-vue/es/form';

const regFormState = ref({
  username: '',
  password: '',
  passwd_again: '',
  email: ''
});

const regFormRef = ref<FormInstance | null>(null);
const router = useRouter();

const handleSubmit = async (e: Event) => {
  e.preventDefault();
  if (regFormRef.value) {
    try {
      console.log('Received values of form: ', regFormState.value);
      const response = await fetch('http://localhost:8000/userregistry', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(regFormState.value),
      });
      if (response.ok) {
        const data = await response.json();
        console.log('Registration successful:', data);
        // Redirect to login page
        router.push('/userlogin');
      } else {
        console.error('Registration failed:', response.statusText);
        message.error('Registration failed. Please check your inputs.');
      }
    } catch (error) {
      console.error('Validation failed:', error);
      message.error('Please check your form inputs.');
    }
  }
};
</script>

<style scoped>
.register-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.register-button {
  width: 100%;
}
</style>