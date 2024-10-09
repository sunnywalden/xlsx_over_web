import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import { createStyleImportPlugin, AndDesignVueResolve } from 'vite-plugin-style-import';
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    createStyleImportPlugin({
      resolves: [AndDesignVueResolve()],
    }),
    vue(),
    vueJsx(),
    vueDevTools(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})