import { defineConfig } from 'vite';
// import CopyPlugin from 'copy-webpack-plugin';

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        index: 'src/index.js',
        popup: 'src/popup.js',
        jquery: 'src/jquery.js',
        // 添加其他入口文件
      },
      output: {
        dir: 'dist', // 输出目录
        format: 'es' // 输出格式
      },
      minify: 'terser',
    },
    assetsInlineLimit: 0, // 禁用资源内联限制
  },
  
});
