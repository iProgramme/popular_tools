const fs = require('fs');

// 测试数据
const MENU_CONFIG = [
  
  {
    name: '系统配置',
    route: '/',
    key: '/systemConfig',
    subMenu: [
      {
        name: '系统信息',
        route: '/systemInfo',
        key: '/systemInfo',
      },
      {
        name: '白名单管理',
        route: '/whiteList',
        key: '/whiteList',
      },
    ]
  },
  // 设备管理
  {
    name: '设备管理',
    route: '/',
    key: '/deviceManage',
    subMenu: [
      {
        name: '系统命令',
        route: '/systemCommand',
        key: '/systemCommand',
      },
      {
        name: '时间设置',
        route: '/timeSetting',
        key: '/timeSetting',
      },
      {
        name: '网络配置',
        route: '/networkConfig',
        key: '/networkConfig',
      },
      {
        name: '双机热备',
        route: '/doubleHotBackup',
        key: '/doubleHotBackup',
      },
      {
        name: '设备证书',
        route: '/deviceCertificate',
        key: '/deviceCertificate',
      },
    ]
  },
  // 系统维护
  {
    name: '系统维护',
    route: '/',
    key: '/systemMaintenance',
    subMenu: [
      {
        name: '备份&恢复',
        route: '/keyBackUpAndRestore',
        key: '/keyBackUpAndRestore',
      },
      {
        name: '还原&升级',
        route: '/restoreAndUpgrade',
        key: '/restoreAndUpgrade',
      },
    ]
  },
  // 管理员管理
  {
    name: '管理员管理',
    route: '/',
    key: '/adminManage',
    subMenu: [
      {
        name: '管理员列表',
        route: '/adminList',
        key: '/adminList',
      },
      {
        name: '管理员策略',
        route: '/adminStrategy',
        key: '/adminStrategy',
      },
    ]
  },
  // 系统监控
  {
    name: '系统监控',
    route: '/',
    key: '/systemMonitor',
    subMenu: [
      {
        name: '在线用户',
        route: '/onlineUser',
        key: '/onlineUser',
      },
      {
        name: '定时任务',
        route: '/scheduledTask',
        key: '/scheduledTask',
      },
      {
        name: '设备监控',
        route: '/deviceMonitor',
        key: '/deviceMonitor',
      },
      {
        name: '监控阈值',
        route: '/monitorThreshold',
        key: '/monitorThreshold',
      },
    ]
  },
  // 关于
  {
    name: '关于',
    route: '/',
    key: '/about',
    subMenu: [
      {
        name: '授权信息',
        route: '/licenseInfo',
        key: '/licenseInfo',
      },
    ]
  }
]

function generateComponentCode(name, key) {
  return `
import React from 'react';
import { Button } from 'antd';

const ${key.charAt(1).toUpperCase() + key.slice(2)} = () => {
  return (
    <div>
      <h1> ${name} </h1>
      {/* 这里可以写你的具体页面内容 */}
      <Button type="primary">Primary Button</Button>
    </div>
  );
};

export default ${key.charAt(1).toUpperCase() + key.slice(2)};
  `;
}


MENU_CONFIG.forEach(({ name, key, subMenu }) => {
  // 生成主文件夹
  fs.mkdirSync(`./${key.charAt(1).toUpperCase() + key.slice(2)}`, { recursive: true });
  console.log(`创建文件夹: ./${key.charAt(1).toUpperCase() + key.slice(2)}`);

  // 生成子文件夹
  subMenu.forEach(({ name: subName, key: subKey }) => {
    fs.mkdirSync(`./${key.charAt(1).toUpperCase() + key.slice(2)}/${subKey.charAt(1).toUpperCase() + subKey.slice(2)}`, { recursive: true });
    console.log(`创建子文件夹: ./${key.charAt(1).toUpperCase() + key.slice(2)}/${subKey.charAt(1).toUpperCase() + subKey.slice(2)}`);

    // 生成文件
    const code = generateComponentCode(subName, subKey);
    fs.writeFileSync(`./${key.charAt(1).toUpperCase() + key.slice(2)}/${subKey.charAt(1).toUpperCase() + subKey.slice(2)}/index.jsx`, code);
    console.log(`创建index.jsx文件: ./${key.charAt(1).toUpperCase() + key.slice(2)}/${subKey.charAt(1).toUpperCase() + subKey.slice(2)}/index.jsx`);
  });
});

