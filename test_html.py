from bs4 import BeautifulSoup
import requests

url = "http://data.xhjingling.com/tb/ssq/index/client.php?action=red2&from=client&src=0000100001%7C0302041190"

#html_doc = requests.get(url).text
html_doc = """
<html style="font-size: 87.2222px;"><head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <meta name="format-detection" content="telephone=no">
    <title data-tp="2">红球综合形态</title>
    <script type="text/javascript" async="" src="https://www.google-analytics.com/analytics.js"></script><script src="http://data.zhongcaishou.com/tb/ssq/statics/js/jq.mobi.min.js?202004211500"></script>
    <script>
        ~(function(dw){
            var winW;
            winW=document.documentElement.clientWidth;
            document.documentElement.style.fontSize = (winW /dw * 100)+"px";
        })(1080);
    </script>
    <link rel="stylesheet" href="http://data.zhongcaishou.com/tb/ssq/statics/css/ssq.css?202004211500">
    <style>
        tbody .coLor_01{font-size: 0.22rem;color: #000 !important;}
    </style>
</head>
<body>
    <div class="teltop">
	<a href="http://data.xhjingling.com/wxtb/dsjtb.html" class="goback"></a>
	<div class="tbbt">
		<div class="style">类<br>型</div>
		<span class="bt">红球综合形态</span><span class="tpTip"></span>
	</div>
	<div class="fx1"></div>
	<div class="fx2"></div>
</div>
<div class="tptk" style="display: none;">
	<div class="topbg"></div>
	<div class="lists">
		<!-- <a href="http://data.zhongcs.com/tb/ssq/index/client.php?action=red1#f=t">红球号码分布</a>	 -->
		<a href="?action=ssqnew#f=t">新走势总表</a>
		<a href="?action=red1#f=t">红球号码分布</a>
		<a href="?action=red2#f=t" class="active">红球综合形态</a>
		<a href="?action=red3#f=t">红球大小奇偶综合分布</a>
		<a href="?action=red17#f=t">红球和值走势</a>
		<a href="?action=red18#f=t">红球和尾走势</a>

		<a href="?action=red5#f=t">红球012路分布</a>
		<a href="?action=red22#f=t">红球012路个数分布</a>
		<a href="?action=red15#f=t">红球跨度走势</a>
		<a href="?action=red6#f=t">红球尾数综合走势</a>
		<a href="?action=red7#f=t">红球尾数分组走势</a>

		<a href="?action=red10#f=t">红球头尾号走势</a>
		<a href="?action=red20#f=t">红球连号分布</a>
		<a href="?action=red21#f=t">红球和值尾数3D分析</a>
		<div class="clearDiv"></div>
		<a href="?action=blue5#f=t">蓝球大小奇偶综合分布</a>
		<a href="?action=blue7#f=t">蓝球尾数综合走势</a>
		<div class="clearDiv"></div>							
	</div>
</div>
<script>
	if(window.location.host.indexOf("xhjingling")>=0){
		$(".goback").attr({"href":"http://data.xhjingling.com/wxtb/dsjtb.html"})
	}else if(window.location.host.indexOf("shujujl")>=0){
		$(".goback").attr({"href":"http://data.shujujl.com/wxtb/dsjtb.html"})
	}else if(window.location.host.indexOf("caiminbang")>=0){
		$(".goback").attr({"href":"http://data.caiminbang.com/wxtb/dsjtb.html"})
	}
</script>
<script type="text/javascript">
	$(".bt").html($("title").html());
	var tpnum = $("title").attr("data-tp");
	if(tpnum>=0){
		$(".lists a").eq(tpnum).addClass("active")
	}
	$("*").click(function (event) {
        event.stopPropagation(); //阻止事件冒泡
        if($(this).hasClass("bt") || $(this).hasClass("tpTip")){
            $(".tptk").toggle();
            return;
        }
        if (!$(this).hasClass("lists")){
            $(".tptk").hide();
        }
    });
</script>
<style>
	.fixbot{
		position: fixed;
		width:100%;
		bottom:0;
		left: 0;
		height: 1.1rem;
		background: url(http://data.zhongcaishou.com/tb/ssq/statics/images/botbg.jpg);
		background-size: 100% 100%;
		display: none;
		z-index: 2002;
	}
	.fixbot img{
		width:100%;
		float: left;
	}
	.close{
		width:0.8rem;
		height: 1.1rem;
		float: left;
		background: url(http://data.zhongcaishou.com/tb/ssq/statics/images/cha.png) no-repeat center;
		background-size: 0.2rem 0.2rem;
	}
	.more{
		width:2.9rem;
		height: 0.87rem;
		float: right;
		background: url(http://data.zhongcaishou.com/tb/ssq/statics/images/more.png) no-repeat center;
		background-size: 100% 100%;
		margin-top:0.18rem;
		margin-right: 0.15rem;
	}
	.xyhm{
		position:fixed;
		width: 0.77rem;
		height:1.39rem;
		background: url(http://data.zhongcaishou.com/tb/ssq/statics/images/xyhm.png) no-repeat center;
		background-size: 100% 100%;
		bottom: 1rem;
		right: 0;
		z-index: 2002;
		display: none;
	}
</style>
<div class="fixbot">
	<div class="close"></div>
	<div class="more"></div>
</div>
<a class="xyhm" id="fd"></a>
<script>
	var toUrl='http://jltbapp.xhjingling.cn/LuckyNumPay?src=0000100001|0500010001'
	$(function(){
		// var lmid=17452//测试栏目id
		var lmid=16468//正式栏目id
		$.get('http://m.zhcw.com/clienth5.do?transactionType=10990101&catalogId='+lmid,function(res){
			if(res){
				var jsObj=res.datas[0][lmid].dataList;
				if(jsObj.length!=0){
					$('.fixbot').css('background','url('+jsObj[0].logoFile+')').css('background-size','100% 100%')
					toUrl=jsObj[0].url
				}
			}
		},'json')
	})
	var end = new Date(new Date(new Date().toLocaleDateString()).getTime() + 12 * 60 * 60 * 1000 - 1); 
	window.onload = function () {
        var flag = 0; //标记是拖曳还是点击
        var oDiv = document.getElementById('fd');
        var disX, moveX, L, T, starX, starY, starXEnd, starYEnd;
        oDiv.addEventListener('touchstart', function (e) {
            flag = 0;
            e.preventDefault();//阻止触摸时页面的滚动，缩放
            disX = e.touches[0].clientX - this.offsetLeft;
            disY = e.touches[0].clientY - this.offsetTop;
            //手指按下时的坐标
            starX = e.touches[0].clientX;
            starY = e.touches[0].clientY;
            //console.log(disX);
        });
        oDiv.addEventListener('touchmove', function (e) {
            L = e.touches[0].clientX - disX;
            T = e.touches[0].clientY - disY;
            //移动时 当前位置与起始位置之间的差值
            starXEnd = e.touches[0].clientX - starX;
            starYEnd = e.touches[0].clientY - starY;
            if(Math.abs(starXEnd)>=5||Math.abs(starYEnd)>=5){
				flag = 1; 
			}
            if (L < 0) {//限制拖拽的X范围，不能拖出屏幕
                L = 0;
            } else if (L > document.documentElement.clientWidth - this.offsetWidth) {
                L = document.documentElement.clientWidth - this.offsetWidth;
            }
            if (T < $(".teltop").height()) {//限制拖拽的Y范围，不能拖出屏幕
                T = $(".teltop").height();
            } else if (T > document.documentElement.clientHeight - this.offsetHeight) {
                T = document.documentElement.clientHeight - this.offsetHeight;
            }
            moveX = L + 'px';
            moveY = T + 'px';
            //console.log(moveX);
            this.style.left = moveX;
            this.style.top = moveY;
        });
        window.addEventListener('touchend', function (e) {
            //alert(parseInt(moveX))
			//判断滑动方向
			//alert(flag)
            if (flag === 0&&e.target.className=='xyhm') {//点击
                window.location.href = toUrl;
            }
        });
	}
	$(".close").unbind("click").bind("click",function(){
		document.cookie=`isEnter=ture; expires=${end}`;
		$(".fixbot").hide();
		$(".xyhm").show();
	})
	$(".more").unbind("click").bind("click",function(){
		document.cookie=`isEnter=ture; expires=${end}`;
		$(".fixbot").hide();
		$(".xyhm").show();
		setTimeout(function(){
			window.location.href = toUrl;
		},50)
	})
	function getCookie(name){ 
		var arr,reg=new RegExp("(^| )"+name+"=([^;]*)(;|$)");
		if(arr=document.cookie.match(reg))
			return unescape(arr[2]); 
		else 
			return null; 
	} 
</script>          <table id="data_body">
      <thead class="tit" style="display: table-header-group;">
            <tr>
                <td colspan="12">红球综合形态</td>
            </tr>
      </thead>
      <thead id="data_menu" class="theight">
        <tr>
            <td rowspan="2" style="min-width: 80px;" class="kjhm">
                <strong>期号</strong>
                <img data-state="Z" onclick="trend.sortTable(true)" id="arrows_logo" class="arrows_logo" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAARCAYAAADpPU2iAAABF0lEQVQokd2QvU7DQBCEjzaSC56LlpLSFba5n/jsC4kChJY38/pOVmwrBAnJjZt7iKFwbEIQSc9II+1pv9k9LWMn6vt+5pzjVVXxvu9np/0f8t4H1lpDRCiKAtZa470P/oSJaDPCZVmiKAoQ0eZXyHsflGUJIgIR4bg++DvUdd31OPmCh5Bzjh8Cb5dsrTVnj/BvZVZPSJRBLHPEMseDzJAIPb0TZZCoDLHUyFfPYFXdhjJdIBLpBMVSI+YpEpUhEgMstUFVtyFjjLGqrkOpDSKR4n6cLDQikSJRBjw9gkdt6xZiPnxt2KYRSw2ucrjtjk8gGLsa67p9D1W2mOB5tkTT7O7OHqHd728e1y9Yrl/RfHzenva/AFqzIL4LkbRiAAAAAElFTkSuQmCC">
            </td>
            <td colspan="2" rowspan="2" style=" min-width:150px;" class="kjhm">
                开奖号码
            </td>
            <td colspan="1" class="kjhm">
                奇偶比
            </td>
            <td colspan="1" class="kjhm">
                大小比
            </td>
            <td colspan="1" class="kjhm">
                质合比
            </td>
            <td colspan="1" class="kjhm">
                三区比
            </td>
            <td colspan="1" class="kjhm">
                012路比
            </td>
            <td colspan="1" class="kjhm">
                和值
            </td>
            <td colspan="1" class="kjhm">
                跨度
            </td>
            <td colspan="1" class="kjhm">
                重号
            </td>
            <td colspan="1">
                连号
            </td>
        </tr>
        <tr>
            
        </tr>
    </thead>
    <tbody id="tbody">
    <tr class="updata odd none"><td class="font_ri kjhm">2022074</td><td class="font_color" colspan="2">05 07 15 19 29 33</td><td class="coLor_01"><span>6:0</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>4:2</span></td><td class="coLor_01"><span>2:2:2</span></td><td class="coLor_01"><span>2:2:2</span></td><td class="coLor_01"><span>108</span></td><td class="coLor_01"><span>28</span></td><td class="coLor_01"><span>0</span></td><td class="coLor_01"><span>0</span></td></tr><tr class="updata even none"><td class="font_ri kjhm">2022075</td><td class="font_color" colspan="2">01 02 04 25 26 30</td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>3:0:3</span></td><td class="coLor_01"><span>1:3:2</span></td><td class="coLor_01"><span>88</span></td><td class="coLor_01"><span>29</span></td><td class="coLor_01"><span>0</span></td><td class="coLor_01"><span>2</span></td></tr><tr class="updata odd none"><td class="font_ri kjhm">2022076</td><td class="font_color" colspan="2">08 09 10 13 24 29</td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>3:1:2</span></td><td class="coLor_01"><span>2:2:2</span></td><td class="coLor_01"><span>93</span></td><td class="coLor_01"><span>21</span></td><td class="coLor_01"><span>0</span></td><td class="coLor_01"><span>3</span></td></tr><tr class="updata even none"><td class="font_ri kjhm">2022077</td><td class="font_color" colspan="2">03 17 18 19 20 27</td><td class="coLor_01"><span>4:2</span></td><td class="coLor_01"><span>5:1</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>1:4:1</span></td><td class="coLor_01"><span>3:1:2</span></td><td class="coLor_01"><span>104</span></td><td class="coLor_01"><span>24</span></td><td class="coLor_01"><span>0</span></td><td class="coLor_01"><span>4</span></td></tr><tr class="updata odd none"><td class="font_ri kjhm">2022078</td><td class="font_color" colspan="2">01 04 05 15 17 31</td><td class="coLor_01"><span>5:1</span></td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>4:2</span></td><td class="coLor_01"><span>3:2:1</span></td><td class="coLor_01"><span>1:3:2</span></td><td class="coLor_01"><span>73</span></td><td class="coLor_01"><span>30</span></td><td class="coLor_01"><span>1</span></td><td class="coLor_01"><span>2</span></td></tr><tr class="updata even none"><td class="font_ri kjhm">2022079</td><td class="font_color" colspan="2">01 09 15 17 22 23</td><td class="coLor_01"><span>5:1</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>2:3:1</span></td><td class="coLor_01"><span>2:2:2</span></td><td class="coLor_01"><span>87</span></td><td class="coLor_01"><span>22</span></td><td class="coLor_01"><span>3</span></td><td class="coLor_01"><span>2</span></td></tr><tr class="updata odd none"><td class="font_ri kjhm">2022080</td><td class="font_color" colspan="2">05 12 15 17 18 27</td><td class="coLor_01"><span>4:2</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>1:4:1</span></td><td class="coLor_01"><span>4:0:2</span></td><td class="coLor_01"><span>94</span></td><td class="coLor_01"><span>22</span></td><td class="coLor_01"><span>2</span></td><td class="coLor_01"><span>2</span></td></tr><tr class="updata even none"><td class="font_ri kjhm">2022081</td><td class="font_color" colspan="2">04 08 11 21 27 30</td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>1:5</span></td><td class="coLor_01"><span>3:1:2</span></td><td class="coLor_01"><span>3:1:2</span></td><td class="coLor_01"><span>101</span></td><td class="coLor_01"><span>26</span></td><td class="coLor_01"><span>1</span></td><td class="coLor_01"><span>0</span></td></tr><tr class="updata odd none"><td class="font_ri kjhm">2022082</td><td class="font_color" colspan="2">04 10 11 23 30 32</td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>3:0:3</span></td><td class="coLor_01"><span>1:2:3</span></td><td class="coLor_01"><span>110</span></td><td class="coLor_01"><span>28</span></td><td class="coLor_01"><span>3</span></td><td class="coLor_01"><span>2</span></td></tr><tr class="updata even none"><td class="font_ri kjhm">2022083</td><td class="font_color" colspan="2">08 12 13 14 19 20</td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>1:5:0</span></td><td class="coLor_01"><span>1:2:3</span></td><td class="coLor_01"><span>86</span></td><td class="coLor_01"><span>12</span></td><td class="coLor_01"><span>0</span></td><td class="coLor_01"><span>3</span></td></tr><tr class="updata odd none"><td class="font_ri kjhm">2022084</td><td class="font_color" colspan="2">03 18 23 24 25 32</td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>5:1</span></td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>1:1:4</span></td><td class="coLor_01"><span>3:1:2</span></td><td class="coLor_01"><span>125</span></td><td class="coLor_01"><span>29</span></td><td class="coLor_01"><span>0</span></td><td class="coLor_01"><span>3</span></td></tr><tr class="updata even none"><td class="font_ri kjhm">2022085</td><td class="font_color" colspan="2">07 09 14 31 32 33</td><td class="coLor_01"><span>4:2</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>2:1:3</span></td><td class="coLor_01"><span>2:2:2</span></td><td class="coLor_01"><span>126</span></td><td class="coLor_01"><span>26</span></td><td class="coLor_01"><span>1</span></td><td class="coLor_01"><span>3</span></td></tr><tr class="updata odd none"><td class="font_ri kjhm">2022086</td><td class="font_color" colspan="2">01 04 08 21 23 24</td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>3:1:2</span></td><td class="coLor_01"><span>2:2:2</span></td><td class="coLor_01"><span>81</span></td><td class="coLor_01"><span>23</span></td><td class="coLor_01"><span>0</span></td><td class="coLor_01"><span>2</span></td></tr><tr class="updata even none"><td class="font_ri kjhm">2022087</td><td class="font_color" colspan="2">05 06 09 13 23 25</td><td class="coLor_01"><span>5:1</span></td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>3:1:2</span></td><td class="coLor_01"><span>2:2:2</span></td><td class="coLor_01"><span>81</span></td><td class="coLor_01"><span>20</span></td><td class="coLor_01"><span>1</span></td><td class="coLor_01"><span>2</span></td></tr><tr class="updata odd none"><td class="font_ri kjhm">2022088</td><td class="font_color" colspan="2">03 09 15 17 20 22</td><td class="coLor_01"><span>4:2</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>2:4:0</span></td><td class="coLor_01"><span>3:1:2</span></td><td class="coLor_01"><span>86</span></td><td class="coLor_01"><span>19</span></td><td class="coLor_01"><span>1</span></td><td class="coLor_01"><span>0</span></td></tr><tr class="updata even none"><td class="font_ri kjhm">2022089</td><td class="font_color" colspan="2">02 07 15 29 31 33</td><td class="coLor_01"><span>5:1</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>4:2</span></td><td class="coLor_01"><span>2:1:3</span></td><td class="coLor_01"><span>2:2:2</span></td><td class="coLor_01"><span>117</span></td><td class="coLor_01"><span>31</span></td><td class="coLor_01"><span>1</span></td><td class="coLor_01"><span>0</span></td></tr><tr class="updata odd none"><td class="font_ri kjhm">2022090</td><td class="font_color" colspan="2">01 04 25 27 29 30</td><td class="coLor_01"><span>4:2</span></td><td class="coLor_01"><span>4:2</span></td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>2:0:4</span></td><td class="coLor_01"><span>2:3:1</span></td><td class="coLor_01"><span>116</span></td><td class="coLor_01"><span>29</span></td><td class="coLor_01"><span>1</span></td><td class="coLor_01"><span>2</span></td></tr><tr class="updata even none"><td class="font_ri kjhm">2022091</td><td class="font_color" colspan="2">08 18 20 22 24 28</td><td class="coLor_01"><span>0:6</span></td><td class="coLor_01"><span>5:1</span></td><td class="coLor_01"><span>0:6</span></td><td class="coLor_01"><span>1:3:2</span></td><td class="coLor_01"><span>2:2:2</span></td><td class="coLor_01"><span>120</span></td><td class="coLor_01"><span>20</span></td><td class="coLor_01"><span>0</span></td><td class="coLor_01"><span>0</span></td></tr><tr class="updata odd none"><td class="font_ri kjhm">2022092</td><td class="font_color" colspan="2">07 10 16 20 21 27</td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>1:5</span></td><td class="coLor_01"><span>2:3:1</span></td><td class="coLor_01"><span>2:3:1</span></td><td class="coLor_01"><span>101</span></td><td class="coLor_01"><span>20</span></td><td class="coLor_01"><span>1</span></td><td class="coLor_01"><span>2</span></td></tr><tr class="updata even none"><td class="font_ri kjhm">2022093</td><td class="font_color" colspan="2">21 22 24 28 29 32</td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>6:0</span></td><td class="coLor_01"><span>1:5</span></td><td class="coLor_01"><span>0:2:4</span></td><td class="coLor_01"><span>2:2:2</span></td><td class="coLor_01"><span>156</span></td><td class="coLor_01"><span>11</span></td><td class="coLor_01"><span>1</span></td><td class="coLor_01"><span>2</span></td></tr><tr class="updata odd none"><td class="font_ri kjhm">2022094</td><td class="font_color" colspan="2">06 11 13 16 19 31</td><td class="coLor_01"><span>4:2</span></td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>4:2</span></td><td class="coLor_01"><span>2:3:1</span></td><td class="coLor_01"><span>1:4:1</span></td><td class="coLor_01"><span>96</span></td><td class="coLor_01"><span>25</span></td><td class="coLor_01"><span>0</span></td><td class="coLor_01"><span>0</span></td></tr><tr class="updata even none"><td class="font_ri kjhm">2022095</td><td class="font_color" colspan="2">04 13 14 18 20 28</td><td class="coLor_01"><span>1:5</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>1:5</span></td><td class="coLor_01"><span>1:4:1</span></td><td class="coLor_01"><span>1:3:2</span></td><td class="coLor_01"><span>97</span></td><td class="coLor_01"><span>24</span></td><td class="coLor_01"><span>1</span></td><td class="coLor_01"><span>2</span></td></tr><tr class="updata odd none"><td class="font_ri kjhm">2022096</td><td class="font_color" colspan="2">03 16 17 19 25 33</td><td class="coLor_01"><span>5:1</span></td><td class="coLor_01"><span>4:2</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>1:3:2</span></td><td class="coLor_01"><span>2:3:1</span></td><td class="coLor_01"><span>113</span></td><td class="coLor_01"><span>30</span></td><td class="coLor_01"><span>0</span></td><td class="coLor_01"><span>2</span></td></tr><tr class="updata even none"><td class="font_ri kjhm">2022097</td><td class="font_color" colspan="2">04 05 10 13 30 31</td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>3:1:2</span></td><td class="coLor_01"><span>1:4:1</span></td><td class="coLor_01"><span>93</span></td><td class="coLor_01"><span>27</span></td><td class="coLor_01"><span>0</span></td><td class="coLor_01"><span>2</span></td></tr><tr class="updata odd none"><td class="font_ri kjhm">2022098</td><td class="font_color" colspan="2">02 03 04 06 21 33</td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>4:1:1</span></td><td class="coLor_01"><span>4:1:1</span></td><td class="coLor_01"><span>69</span></td><td class="coLor_01"><span>31</span></td><td class="coLor_01"><span>1</span></td><td class="coLor_01"><span>3</span></td></tr><tr class="updata even none"><td class="font_ri kjhm">2022099</td><td class="font_color" colspan="2">01 11 23 24 26 32</td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>4:2</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>2:0:4</span></td><td class="coLor_01"><span>1:1:4</span></td><td class="coLor_01"><span>117</span></td><td class="coLor_01"><span>31</span></td><td class="coLor_01"><span>0</span></td><td class="coLor_01"><span>2</span></td></tr><tr class="updata odd none"><td class="font_ri kjhm">2022100</td><td class="font_color" colspan="2">02 06 07 15 20 21</td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>3:3:0</span></td><td class="coLor_01"><span>3:1:2</span></td><td class="coLor_01"><span>71</span></td><td class="coLor_01"><span>19</span></td><td class="coLor_01"><span>0</span></td><td class="coLor_01"><span>2</span></td></tr><tr class="updata even none"><td class="font_ri kjhm">2022101</td><td class="font_color" colspan="2">04 16 18 19 27 28</td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>4:2</span></td><td class="coLor_01"><span>1:5</span></td><td class="coLor_01"><span>1:3:2</span></td><td class="coLor_01"><span>2:4:0</span></td><td class="coLor_01"><span>112</span></td><td class="coLor_01"><span>24</span></td><td class="coLor_01"><span>0</span></td><td class="coLor_01"><span>2</span></td></tr><tr class="updata odd none"><td class="font_ri kjhm">2022102</td><td class="font_color" colspan="2">09 10 12 18 29 32</td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>1:5</span></td><td class="coLor_01"><span>2:2:2</span></td><td class="coLor_01"><span>3:1:2</span></td><td class="coLor_01"><span>110</span></td><td class="coLor_01"><span>23</span></td><td class="coLor_01"><span>1</span></td><td class="coLor_01"><span>2</span></td></tr><tr class="updata even"><td class="font_ri kjhm">2022103</td><td class="font_color" colspan="2">06 09 12 14 20 28</td><td class="coLor_01"><span>1:5</span></td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>0:6</span></td><td class="coLor_01"><span>2:3:1</span></td><td class="coLor_01"><span>3:1:2</span></td><td class="coLor_01"><span>89</span></td><td class="coLor_01"><span>22</span></td><td class="coLor_01"><span>2</span></td><td class="coLor_01"><span>0</span></td></tr><tr class="updata odd"><td class="font_ri kjhm">2022104</td><td class="font_color" colspan="2">01 08 19 25 26 31</td><td class="coLor_01"><span>4:2</span></td><td class="coLor_01"><span>4:2</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>2:1:3</span></td><td class="coLor_01"><span>0:4:2</span></td><td class="coLor_01"><span>110</span></td><td class="coLor_01"><span>30</span></td><td class="coLor_01"><span>0</span></td><td class="coLor_01"><span>2</span></td></tr><tr class="updata even"><td class="font_ri kjhm">2022105</td><td class="font_color" colspan="2">06 12 13 15 21 23</td><td class="coLor_01"><span>4:2</span></td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>1:4:1</span></td><td class="coLor_01"><span>4:1:1</span></td><td class="coLor_01"><span>90</span></td><td class="coLor_01"><span>17</span></td><td class="coLor_01"><span>0</span></td><td class="coLor_01"><span>2</span></td></tr><tr class="updata odd"><td class="font_ri kjhm">2022106</td><td class="font_color" colspan="2">17 20 22 23 24 31</td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>6:0</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>0:3:3</span></td><td class="coLor_01"><span>1:2:3</span></td><td class="coLor_01"><span>137</span></td><td class="coLor_01"><span>14</span></td><td class="coLor_01"><span>1</span></td><td class="coLor_01"><span>3</span></td></tr><tr class="updata even"><td class="font_ri kjhm">2022107</td><td class="font_color" colspan="2">03 09 11 15 19 28</td><td class="coLor_01"><span>5:1</span></td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>3:2:1</span></td><td class="coLor_01"><span>3:2:1</span></td><td class="coLor_01"><span>85</span></td><td class="coLor_01"><span>25</span></td><td class="coLor_01"><span>0</span></td><td class="coLor_01"><span>0</span></td></tr><tr class="updata odd"><td class="font_ri kjhm">2022108</td><td class="font_color" colspan="2">01 07 13 17 18 31</td><td class="coLor_01"><span>5:1</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>5:1</span></td><td class="coLor_01"><span>2:3:1</span></td><td class="coLor_01"><span>1:4:1</span></td><td class="coLor_01"><span>87</span></td><td class="coLor_01"><span>30</span></td><td class="coLor_01"><span>0</span></td><td class="coLor_01"><span>2</span></td></tr><tr class="updata even"><td class="font_ri kjhm">2022109</td><td class="font_color" colspan="2">04 11 13 19 22 33</td><td class="coLor_01"><span>4:2</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>2:3:1</span></td><td class="coLor_01"><span>1:4:1</span></td><td class="coLor_01"><span>102</span></td><td class="coLor_01"><span>29</span></td><td class="coLor_01"><span>1</span></td><td class="coLor_01"><span>0</span></td></tr><tr class="updata odd"><td class="font_ri kjhm">2022110</td><td class="font_color" colspan="2">09 13 15 18 20 28</td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>1:5</span></td><td class="coLor_01"><span>1:4:1</span></td><td class="coLor_01"><span>3:2:1</span></td><td class="coLor_01"><span>103</span></td><td class="coLor_01"><span>19</span></td><td class="coLor_01"><span>1</span></td><td class="coLor_01"><span>0</span></td></tr><tr class="updata even"><td class="font_ri kjhm">2022111</td><td class="font_color" colspan="2">02 10 11 13 28 31</td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>4:2</span></td><td class="coLor_01"><span>3:1:2</span></td><td class="coLor_01"><span>0:4:2</span></td><td class="coLor_01"><span>95</span></td><td class="coLor_01"><span>29</span></td><td class="coLor_01"><span>2</span></td><td class="coLor_01"><span>2</span></td></tr><tr class="updata odd"><td class="font_ri kjhm">2022112</td><td class="font_color" colspan="2">03 05 08 17 25 31</td><td class="coLor_01"><span>5:1</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>4:2</span></td><td class="coLor_01"><span>3:1:2</span></td><td class="coLor_01"><span>1:2:3</span></td><td class="coLor_01"><span>89</span></td><td class="coLor_01"><span>28</span></td><td class="coLor_01"><span>1</span></td><td class="coLor_01"><span>0</span></td></tr><tr class="updata even"><td class="font_ri kjhm">2022113</td><td class="font_color" colspan="2">13 14 20 24 27 29</td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>4:2</span></td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>0:3:3</span></td><td class="coLor_01"><span>2:1:3</span></td><td class="coLor_01"><span>127</span></td><td class="coLor_01"><span>16</span></td><td class="coLor_01"><span>0</span></td><td class="coLor_01"><span>2</span></td></tr><tr class="updata odd"><td class="font_ri kjhm">2022114</td><td class="font_color" colspan="2">01 05 15 19 26 29</td><td class="coLor_01"><span>5:1</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>4:2</span></td><td class="coLor_01"><span>2:2:2</span></td><td class="coLor_01"><span>1:2:3</span></td><td class="coLor_01"><span>95</span></td><td class="coLor_01"><span>28</span></td><td class="coLor_01"><span>1</span></td><td class="coLor_01"><span>0</span></td></tr><tr class="updata even"><td class="font_ri kjhm">2022115</td><td class="font_color" colspan="2">06 07 18 20 27 29</td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>4:2</span></td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>2:2:2</span></td><td class="coLor_01"><span>3:1:2</span></td><td class="coLor_01"><span>107</span></td><td class="coLor_01"><span>23</span></td><td class="coLor_01"><span>1</span></td><td class="coLor_01"><span>2</span></td></tr><tr class="updata odd"><td class="font_ri kjhm">2022116</td><td class="font_color" colspan="2">08 14 26 27 30 33</td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>4:2</span></td><td class="coLor_01"><span>0:6</span></td><td class="coLor_01"><span>1:1:4</span></td><td class="coLor_01"><span>3:0:3</span></td><td class="coLor_01"><span>138</span></td><td class="coLor_01"><span>25</span></td><td class="coLor_01"><span>1</span></td><td class="coLor_01"><span>2</span></td></tr><tr class="updata even"><td class="font_ri kjhm">2022117</td><td class="font_color" colspan="2">04 13 17 18 28 29</td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>4:2</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>1:3:2</span></td><td class="coLor_01"><span>1:3:2</span></td><td class="coLor_01"><span>109</span></td><td class="coLor_01"><span>25</span></td><td class="coLor_01"><span>0</span></td><td class="coLor_01"><span>2</span></td></tr><tr class="updata odd"><td class="font_ri kjhm">2022118</td><td class="font_color" colspan="2">02 06 07 11 14 33</td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>1:5</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>4:1:1</span></td><td class="coLor_01"><span>2:1:3</span></td><td class="coLor_01"><span>73</span></td><td class="coLor_01"><span>31</span></td><td class="coLor_01"><span>0</span></td><td class="coLor_01"><span>2</span></td></tr><tr class="updata even"><td class="font_ri kjhm">2022119</td><td class="font_color" colspan="2">02 05 15 18 26 27</td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>2:2:2</span></td><td class="coLor_01"><span>3:0:3</span></td><td class="coLor_01"><span>93</span></td><td class="coLor_01"><span>25</span></td><td class="coLor_01"><span>1</span></td><td class="coLor_01"><span>2</span></td></tr><tr class="updata odd"><td class="font_ri kjhm">2022120</td><td class="font_color" colspan="2">02 15 19 26 27 29</td><td class="coLor_01"><span>4:2</span></td><td class="coLor_01"><span>4:2</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>1:2:3</span></td><td class="coLor_01"><span>2:1:3</span></td><td class="coLor_01"><span>118</span></td><td class="coLor_01"><span>27</span></td><td class="coLor_01"><span>4</span></td><td class="coLor_01"><span>2</span></td></tr><tr class="updata even"><td class="font_ri kjhm">2022121</td><td class="font_color" colspan="2">12 17 22 27 30 31</td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>5:1</span></td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>0:3:3</span></td><td class="coLor_01"><span>3:2:1</span></td><td class="coLor_01"><span>139</span></td><td class="coLor_01"><span>19</span></td><td class="coLor_01"><span>1</span></td><td class="coLor_01"><span>2</span></td></tr><tr class="updata odd"><td class="font_ri kjhm">2022122</td><td class="font_color" colspan="2">06 08 17 19 24 28</td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>4:2</span></td><td class="coLor_01"><span>2:4</span></td><td class="coLor_01"><span>2:2:2</span></td><td class="coLor_01"><span>2:2:2</span></td><td class="coLor_01"><span>102</span></td><td class="coLor_01"><span>22</span></td><td class="coLor_01"><span>1</span></td><td class="coLor_01"><span>0</span></td></tr><tr class="updata even"><td class="font_ri kjhm">2022123</td><td class="font_color" colspan="2">10 13 16 20 21 25</td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>3:3</span></td><td class="coLor_01"><span>1:5</span></td><td class="coLor_01"><span>1:4:1</span></td><td class="coLor_01"><span>1:4:1</span></td><td class="coLor_01"><span>105</span></td><td class="coLor_01"><span>15</span></td><td class="coLor_01"><span>0</span></td><td class="coLor_01"><span>2</span></td></tr></tbody>

    </table>
    <script src="http://data.zhongcaishou.com/tb/ssq/statics/js/ssq.min.js?202004211500"></script>
    <script>
        // 获取数据并展示
        trend.type = "H_HMGS";
        trend.init_data = function(){
            var S = "";
            trend.get_data(function(data){
                var trStr = tdStr = "";
                var ftrStr = cClass = ftdStr = "";
                console.log(data.list)
                data.list.forEach(function(v, i) {
                    arr = [],//三区比和012路比数组
                    sum = 0,//开奖号和
                    lhlist= [],//连号数组
                    lh=0,//连号
                    ch=0,//重号
                    zh=0,//质合
                    befkj="";//上期的开奖号红球
                    if(i>1){
                       befkj = data.list[i-1].winNum;
                    } 
                    v.winNum = v.winNum.split("|")[0]
                    v.winNumArr = v.winNum.split("|")[0].split(",").sort();
                    trStr = tdStr = "";
                    if (i % 2 == 0) {
                        trStr = '<tr class="updata odd"><td class="font_ri kjhm">'+ v.issue +'</td><td class="font_color" colspan="2">'+ v.winNumArr.join(" ") +'</td>'
                    } else {
                        trStr = '<tr class="updata even"><td class="font_ri kjhm">'+ v.issue +'</td><td class="font_color" colspan="2">'+ v.winNumArr.join(" ") +'</td>'
                    }
                     
                    v.sumData.split(",").forEach(function(v, i) {
                        if (v == "-") {
                            if (i <= 6) {
                                trStr += '<td class="coLor_01" ><span>'+ i%7 +':'+(6-i%7)+'</span></td>';
                            }else if (i >= 14 && i < 21) {
                                trStr += '<td class="coLor_01" ><span>'+ i%7 +':'+(6-i%7)+'</span></td>';
                            }
                        } 
                    });
                    
                    v.sumAttrib.split(",").forEach(function(v, i) {
                        if (v == "-") {
                            arr.push(i%7)    
                        }                        
                    });
                      
                    for(j=0;j<v.winNumArr.length;j++){  
                        var zslist = "01,02,03,05,07,11,13,17,19,23,29,31"
                        if(zslist.indexOf(v.winNumArr[j])>=0){
                            zh++;
                        }
                        sum += parseInt(v.winNumArr[j]);
                        if( j >= 1 ){
                            bef = j-1;  
                            if(v.winNumArr[j]-v.winNumArr[bef] == 1){
                                lh++;
                                if(j==(v.winNumArr.length-1)){                                   
                                    lhlist.push(lh);
                                }
                            }else{
                                lhlist.push(lh);
                                lh = 0;
                            }                            
                        }   
                        eve = v.winNumArr[j];
                        if(befkj.indexOf(eve)>=0){                               
                            ch = ch+1;
                        } 
                    }                     
                    lhlist = lhlist.sort();  
                    tdStr += '<td class="coLor_01"><span>'+zh +':'+ (6-zh) +'</span></td><td class="coLor_01"><span>'+ arr[3] +':'+ arr[4] +':'+ arr[5] +'</span></td><td class="coLor_01"><span>'+ arr[0] +':'+ arr[1] +':'+ arr[2] +'</span></td><td class="coLor_01"><span>'+ sum +'</span></td><td class="coLor_01"><span>'+ (v.winNumArr[5]-v.winNumArr[0]) +'</span></td><td class="coLor_01"><span>'+ ch +'</span></td><td class="coLor_01"><span>'+ (lhlist[lhlist.length-1]>=1? (++lhlist[lhlist.length-1]):0)+'</span></td>';
                    S += trStr + tdStr + "</tr>";

                });
                $("#tbody").append(S);
            });
        }
        trend.draw_svg = function(){
            init_tr();
        }
        trend.init();
    </script>
    <script src="http://data.zhongcaishou.com/tb/ssq/statics/js/trend.min.js?202004211500"></script>

</body></html>
"""

html_doc_1 = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, "html.parser")

#print(soup.find_all("tr", ["updata odd none","updata even none"]))
items = []
for html in soup.find_all("tr", ["updata odd none","updata even none"]):
    item = []
    for child in html.children:
        #print("期号：" + child.td["font_ri kjhm"])
        #print("开号：" + child.td["font_color"])
        item.append(child.string)
    items.append(item)
print(items)
print(len(items))