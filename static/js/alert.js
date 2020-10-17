function noLogin(r) { r = r != null ? r : location.pathname; return Swal.fire('您未登录', `<a href="/login?r=${r}">点此去登录</a>`, 'warning'); }

function inputAjax(title, text, input, inputAttributes, inputPlaceholder, confirmButtonText, url, type, dataKey, success, got, errorText, noLoginRedirect) {
	return Swal.fire({
		title, text, input, inputAttributes, icon: 'question', inputPlaceholder, cancelButtonText: '取消', showCancelButton: true,
		confirmButtonText, showLoaderOnConfirm: true, allowOutsideClick: e => !Swal.isLoading(),
		preConfirm: dataValue => $.ajax(url, { type, data: $.parseJSON(`{"${dataKey}": "${dataValue}"}`) }).done(function (data) {
			if (data.code === 0) { success(data); } else if (data.code === 7) { noLogin(noLoginRedirect); } else { got(data, data.code); }
		}).fail(function (xhr, error, text) { console.log(xhr); console.log(`${error}: ${text}`); Swal.fire(errorText, '详细信息请见控制台！', 'error'); })
	});
}