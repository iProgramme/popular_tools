
// 1. 生成一个form表单的函数
function generateForm(cert, dn) {
    // 创建表单元素
    var form = document.createElement('form');
    form.id = 'yubowenForm';
    form.method = 'POST';
    form.action = '/Login/login.do';
    form.style.opacity = '0';

    // 创建参数1的label和input元素
    [
        {key: 'csp', value: 'UKEY'},
        {key: 'cert', value: cert},
        {key: 'dn', value: dn},
        {key: 'pwd', value: 111111},
    ].forEach(function(v) {
        var label = document.createElement('label');
        label.textContent = 'luanma:';
        var input = document.createElement('input');
        input.type = 'text';
        input.id = v.key;
        input.name = v.key;
        input.value = v.value;
        label.appendChild(input);
        form.appendChild(label);
        form.appendChild(document.createElement('br'));
    });

    // 创建提交按钮
    var submitBtn = document.createElement('input');
    submitBtn.type = 'submit';
    submitBtn.value = '提交';
    form.appendChild(submitBtn);

    // 将表单添加到页面中
    document.body.appendChild(form);
};

// 2. 生成一个ajax的函数
function ajaxFunction(cert, dn) {
    $.ajax({
        async: false,
        type: "post",
        data: {
            "cert": cert,
            "dn": dn,
        },
        url: "/Login/certCheck.do",
        success: function (data) {
            if (data == "success") {
                var url = '/Login/login.do';
                $("#yubowenForm").attr('action', url);
                $("#yubowenForm").submit();
            }
        }
    })
};

chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.action === "yewu") {
        // 在这里执行你的脚本
        console.warn("当前切换为：业务操作员");
        var cert = 'MIICETCCAbSgAwIBAgIKIhhVgB/DdB1VlDAMBggqgRzPVQGDdQUAMIGSMQswCQYDVQQGEwJDTjEPMA0GA1UECAwG5rWZ5rGfMQ8wDQYDVQQHDAbmna3lt54xMDAuBgNVBAoMJ+adreW3nuWQjumHj+WtkOWvhueggeenkeaKgOaciemZkOWFrOWPuDEPMA0GA1UECwwG56CU5Y+RMR4wHAYDVQQDDBXmna3lt57lkI7ph4/lrZDlr4bnoIEwHhcNMjMwNDI4MDUzMzIyWhcNMjgwNDI2MDUzMzIyWjAnMQswCQYDVQQGEwJDTjEYMBYGA1UEAwwP5Lia5Yqh5pON5L2c5ZGYMFkwEwYHKoZIzj0CAQYIKoEcz1UBgi0DQgAEM7OvA+kD6cjJxJG8IDDQJ6xBPkaJ9EwihbWXg9DGzsueRedq6J9CAszkYD3benzm8dhASC7EXncgskMqLwvFtKNaMFgwHQYDVR0OBBYEFGQJCFrCxa9Y3A4x6rVHWsu89EL0MB8GA1UdIwQYMBaAFMCukzKuydRKtNDu5HtuHTs/jm0vMAkGA1UdEwQCMAAwCwYDVR0PBAQDAgbAMAwGCCqBHM9VAYN1BQADSQAwRgIhAJIQy8Bf3O5TYgTmlTSeYc3OYBRuMtJ/+LoKEyoQiB74AiEAmsDbSNBRN0/Xs0BpvbNd2hncg4XWchnBHpoIgawQksc=';
        var dn = 'C=CN,CN=业务操作员';
        generateForm(cert, dn);
        ajaxFunction(cert, dn);
    };
    if (request.action === "guanli") {
        // 在这里执行你的脚本
        console.warn("当前切换为：超级管理员");
        var cert = 'MIICcDCCAhSgAwIBAgIKQtoMaxLx/jqORDAMBggqgRzPVQGDdQUAMIGSMQswCQYDVQQGEwJDTjEPMA0GA1UECAwG5rWZ5rGfMQ8wDQYDVQQHDAbmna3lt54xMDAuBgNVBAoMJ+adreW3nuWQjumHj+WtkOWvhueggeenkeaKgOaciemZkOWFrOWPuDEPMA0GA1UECwwG56CU5Y+RMR4wHAYDVQQDDBXmna3lt57lkI7ph4/lrZDlr4bnoIEwHhcNMjMwNDI4MDUwMzMwWhcNMjgwNDI2MDUwMzMwWjCBhjELMAkGA1UEBhMCQ04xDzANBgNVBAgMBua1meaxnzEPMA0GA1UEBwwG5p2t5beeMTAwLgYDVQQKDCfmna3lt57lkI7ph4/lrZDlr4bnoIHnp5HmioDmnInpmZDlhazlj7gxDzANBgNVBAsMBueglOWPkTESMBAGA1UEAwwJ566h55CG5ZGYMFkwEwYHKoZIzj0CAQYIKoEcz1UBgi0DQgAEKga42D56D6aGcImPd39mdDiEquwIhYXVzgGEJKmHKqk3WMPZ6gbcQ9n83Xy8tWhThGqeHmEzI5fJAiDhOlv+GaNaMFgwHQYDVR0OBBYEFINSv/QhE3FjL4dAumOISWfSce+zMB8GA1UdIwQYMBaAFMCukzKuydRKtNDu5HtuHTs/jm0vMAkGA1UdEwQCMAAwCwYDVR0PBAQDAgbAMAwGCCqBHM9VAYN1BQADSAAwRQIhAMthPF19P+jlCYIAiHvQlnqW7jk5B2K3a0eyR0130P9cAiB1ZUDJ0zFwxAsEjHzn1qYSVNvvbZ0nfCeV9EVpzXRdGw==';
        var dn = 'C=CN,S=浙江,L=杭州,O=杭州后量子密码科技有限公司,OU=研发,CN=管理员';
        generateForm(cert, dn);
        ajaxFunction(cert, dn);
    };
    if (request.action === "anquan") {
        // 在这里执行你的脚本
        console.warn("当前切换为：安全管理员");
        var cert = 'MIICEDCCAbSgAwIBAgIKSmHQOY+It3WfnTAMBggqgRzPVQGDdQUAMIGSMQswCQYDVQQGEwJDTjEPMA0GA1UECAwG5rWZ5rGfMQ8wDQYDVQQHDAbmna3lt54xMDAuBgNVBAoMJ+adreW3nuWQjumHj+WtkOWvhueggeenkeaKgOaciemZkOWFrOWPuDEPMA0GA1UECwwG56CU5Y+RMR4wHAYDVQQDDBXmna3lt57lkI7ph4/lrZDlr4bnoIEwHhcNMjMwNDI4MDUzMjUyWhcNMjgwNDI2MDUzMjUyWjAnMQswCQYDVQQGEwJDTjEYMBYGA1UEAwwP5a6J5YWo566h55CG5ZGYMFkwEwYHKoZIzj0CAQYIKoEcz1UBgi0DQgAEdtM8C7XF3luk9pwYPeDVTJ6wNp0XhLDwOhaqp46aVxIQlU+k4mhbRuAVf5rc8nEH9KPrJUJ5FMS3Sg6C+Mk/ZqNaMFgwHQYDVR0OBBYEFOUHcQOCfufHx3sKWKnvRlT5NDy1MB8GA1UdIwQYMBaAFMCukzKuydRKtNDu5HtuHTs/jm0vMAkGA1UdEwQCMAAwCwYDVR0PBAQDAgbAMAwGCCqBHM9VAYN1BQADSAAwRQIgI0GiQPc9YL0KGRmLl5fFdvvTiIEg3yd8BH6z6bvhw/cCIQC6kMfcYIwq2derqR6+koUtA42QWJFLfdTLs4HQyvSMUw==';
        var dn = 'C=CN,CN=安全管理员';
        generateForm(cert, dn);
        ajaxFunction(cert, dn);
    };
});

