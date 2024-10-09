<template>
  <div class="container demo-1">
    <div class="content">
      <div id="large-header" class="large-header">
        <canvas id="demo-canvas"></canvas>
        <div class="uploader_box" style="width: 80%; margin-left: 10%">
          <h3>XLSX Uploader</h3>
          <a-upload
            :beforeUpload="beforeUpload"
            :customRequest="customRequest"
            :fileList="fileList"
            multiple
          >
            <a-button type="primary">Upload XLSX</a-button>
          </a-upload>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { Upload, Button } from 'ant-design-vue';

const fileList = ref([]);

const beforeUpload = (file: any) => {
  const isXlsx = file.type === 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet';
  if (!isXlsx) {
    console.error('You can only upload XLSX files!');
  }
  return isXlsx;
};

const customRequest = async ({ file, onSuccess, onError }: any) => {
  const formData = new FormData();
  formData.append('file', file);

  try {
    const response = await fetch('http://localhost:8000/xlsxuploader', {
      method: 'POST',
      body: formData,
    });
    if (response.ok) {
      onSuccess(await response.json());
      console.log('Upload successful');
    } else {
      onError(new Error('Upload failed'));
      console.error('Upload failed:', response.statusText);
    }
  } catch (error) {
    onError(error);
    console.error('Error during upload:', error);
  }
};
</script>

<style scoped>
/* Add your styles here */
</style>