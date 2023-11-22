const https = require('https');

const data = JSON.stringify({ "text": { "content": '我来部署一下看看'}, "msgtype":"text" }); // 设置POST请求的数据

const options = {
  hostname: 'oapi.dingtalk.com',
  path: '/robot/send?access_token=56ceb967c435bb1331d7a60d5d062e237eef7b13ea015633c37c168782388680',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  }
};

const req = https.request(options, (res) => {
  console.log(`状态码: ${res.statusCode}`);

  res.on('data', (chunk) => {
    console.log(`响应主体: ${chunk}`);
  });

  res.on('end', () => {
    console.log('响应数据接收完毕。');
  });
});

req.on('error', (e) => {
  console.error(`请求遇到问题: ${e.message}`);
});

req.write(data);
req.end();


// curl 'https://oapi.dingtalk.com/robot/send?access_token=56ceb967c435bb1331d7a60d5d062e237eef7b13ea015633c37c168782388680' \
//  -H 'Content-Type: application/json' \
//  -d '{"msgtype": "text","text": {"content":"我就是我, 是不一样的烟火"}}'