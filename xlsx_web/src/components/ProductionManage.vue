<template>
  <div class="container demo-1">
    <div class="content">
      <div id="large-header" class="large-header">
        <canvas id="demo-canvas"></canvas>
        <div class="manage_box" style="width: 80%; margin-left: 10%">
          <h3>Production Management</h3>
          <a-form :form="form" @submit="handleSubmit">
            <a-form-item>
              <a-input
                v-decorator="['name', { rules: [{ required: true, message: 'Please input the production name!' }] }]"
                placeholder="Enter production name"
              />
            </a-form-item>
            <a-form-item>
              <a-select v-decorator="['status', { rules: [{ required: true, message: 'Please select the status!' }] }]">
                <a-select-option value="active">Active</a-select-option>
                <a-select-option value="inactive">Inactive</a-select-option>
              </a-select>
            </a-form-item>
            <a-form-item>
              <a-button type="primary" html-type="submit" style="width: 100%">Submit</a-button>
            </a-form-item>
          </a-form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { Form, Input, Select, Button } from 'ant-design-vue';
import type { FormInstance } from 'ant-design-vue/es/form';

const form = ref<FormInstance | null>(null);

const handleSubmit = async (e: Event) => {
  e.preventDefault();
  if (form.value) {
    try {
      const values = await form.value.validateFields();
      console.log('Received values of form: ', values);
      const response = await fetch('/api/productionmanage', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(values),
      });
      if (response.ok) {
        const data = await response.json();
        console.log('Submission successful:', data);
        // Handle successful submission
      } else {
        console.error('Submission failed:', response.statusText);
        // Handle submission failure
      }
    } catch (error) {
      console.error('Error during submission:', error);
      // Handle error
    }
  }
};
</script>

<style scoped>
/* Add your styles here */
</style>