<template>
  <div class="container demo-1">
    <div class="content">
      <div id="large-header" class="large-header">
        <canvas id="demo-canvas"></canvas>
        <div class="dashboard_box">
          <h3>Production Dashboard</h3>
          <a-table :columns="columns" :dataSource="data" rowKey="id" bordered />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { Table } from 'ant-design-vue';

const columns = ref([]);
const data = ref([]);

onMounted(async () => {
  try {
    const response = await fetch('http://localhost:8000/loader/', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    });
    if (response.ok) {
      const responseData = await response.json();
      const [header, ...rows] = responseData.data; // Extract header and rows
      columns.value = header.map((title, index) => ({
        title,
        dataIndex: `col${index}`,
        key: `col${index}`,
      }));
      data.value = rows.map((row, rowIndex) => {
        const rowData = { id: rowIndex };
        row.forEach((cell, cellIndex) => {
          rowData[`col${cellIndex}`] = cell;
        });
        return rowData;
      });
    } else {
      console.error('Failed to fetch data:', response.statusText);
    }
  } catch (error) {
    console.error('Error fetching data:', error);
  }
});
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f0f2f5;
}

.content {
  width: 100%;
  max-width: 1200px;
  padding: 20px;
  background: #fff;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}

.large-header {
  position: relative;
  width: 100%;
  height: 100%;
}

.dashboard_box {
  width: 100%;
  margin: 0 auto;
  padding: 20px;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

h3 {
  text-align: center;
  margin-bottom: 20px;
  color: #1890ff;
}

a-table {
  width: 100%;
}

.ant-table {
  border-radius: 8px;
  overflow: hidden;
}

.ant-table-thead > tr > th {
  background-color: #fafafa;
  color: #333;
  font-weight: bold;
}

.ant-table-tbody > tr > td {
  background-color: #fff;
}

.ant-table-tbody > tr:hover > td {
  background-color: #e6f7ff;
}
</style>