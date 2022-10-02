let loadDiv = document.getElementById('load');

// 获取地址栏参数函数
function getSearchString(key, url) {
    var str = url.substring(1, url.length);
    var arr = str.split("&");
    var obj = new Object();

    for (var i = 0; i < arr.length; i++) {
        var paramArr = arr[i].split("=");

        obj[decodeURIComponent(paramArr[0])] = decodeURIComponent(paramArr[1]);
    }

    return obj[key];
}

// 加载并解析 Markdown 函数
function loadMD(file) {
    var xmlhttp;

    if (window.XMLHttpRequest) { xmlhttp=new XMLHttpRequest(); }
    else { xmlhttp=new ActiveXObject("Microsoft.XMLHTTP"); }

    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            loadDiv.innerHTML = marked(xmlhttp.responseText);
            document.body.style.background = '#FFF';
            loadDiv.setAttribute('class', '');
        } else if (xmlhttp.status == 404) {
            loadDiv.innerHTML = '<h1>未找到该文章</h1><a href="./">返回首页</a>'
        }
    }
    
    xmlhttp.open("GET",file,true);
    xmlhttp.send();
}

// 文章标题点击事件
var btn_read = document.querySelectorAll('.list a');

for(var i =0;i<btn_read.length;i++){
    btn_read[i].onclick = function(){
        let url = this.getAttribute('href').replace(/[^0-9]/ig,"");

        window.location.href = '?p=' + url;

        return false;
    }
}

// 文章内容加载
var p = getSearchString('p', window.location.search);

if(p != undefined && p != '') {
    let file = `../post/${p}.md`;

    loadMD(file);
}

// 博客存活天数
console.log(Math.floor((new Date() - new Date('2022/10/2'))/(24*3600*1000)) + ' Days');