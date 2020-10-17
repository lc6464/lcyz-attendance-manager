function htmlEscape(html) { var r = $('#htmlEscape').text(html).html().replace(/\\r\\n/g, '<br/>'); $('#htmlEscape').html(''); return r; }
function sudo(success, noLoginRedirect) {
	return inputAjax('敏感操作验证', '请输入此账户的密码：', 'password', { required: 'required' }, '请输入此账户的密码', '验证', '/sudo', 'post', 'Password', function () {
		Swal.fire('成功', `验证成功！30分钟内无需再次验证！`, 'success').then(success);
	}, function (data, code) {
		if (code === 5) {
			Swal.fire('提示', htmlEscape(data.msg), 'info').then(success);
		} else {
			Swal.fire('失败', htmlEscape(data.msg), 'error');
		}
	}, '验证失败！', noLoginRedirect);
}
function getAjaxConfig(url, info, inputsLength, success, sudoSuccess) { return { url, type: 'post', dataType: 'json', success: function (data) {
	switch (data.code) { case 0: Swal.fire('成功', htmlEscape(data.msg), 'success').then(success); break; case 7: noLogin(); break; case 8: sudo(sudoSuccess); break;
		default: Swal.fire('失败', htmlEscape(data.msg), 'error');
	} }, error: function (xhr, error, text) { console.log(xhr); console.log(`${error}: ${text}`); Swal.fire(info + '失败！', '详细信息请见控制台！', 'error');
	}, beforeSubmit: function (arr) { console.log(arr); if (arr.length !== inputsLength) { Swal.fire('提示', '请选择性别！', 'warning'); return false; } } };
}