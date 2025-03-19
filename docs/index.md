#  

<center><font class="custom-font ml3">好好学习 天天向上</font></center>
<script src="https://cdn.statically.io/libs/animejs/2.0.2/anime.min.js"></script>
<style>
    .custom-font {
    font-size: 38px; /* 默认字体大小为8px */
    color: #757575;
}
@media (max-width: 768px) { /* 假设768px及以下为移动端 */
    .custom-font {
        font-size: 32px; /* 移动端字体大小为6px */
    }
}
</style>

***  


<div class="grid cards" markdown>

-   :octicons-bookmark-16:{ .lg .middle } __article__

    ---

    - [Beijing](Essays/Travel/beijing.md)
    - [Jinan](Essays/Travel/jinan.md)

    
    
-   :simple-aboutdotme:{ .lg .middle } __others__

    ---

    <!-- - [留言板](waline.md) -->
    - [Blogger](blog/index.md)  
    <!-- - [:octicons-arrow-right-24: 了解我](about/geren.md)[^see-how-much-I-love-you] -->

</div>

[:octicons-link-16: 朋友们!](link.md) / 
[:material-chart-line: 站点统计](javascript:toggle_statistics();)

<div id="statistics" markdown="1" class="card" style="width: 27em; border-color: transparent; opacity: 0; font-size: 75%">
<div style="padding-left: 1em;" markdown="1">
页面总数：{{pages}}  
总字数：{{words}}  
代码块行数：{{codes}}  
网站运行时间：<span id="web-time"></span>
</div>
</div>

<style>
.md-grid {
  max-width: 1220px;
}
</style>





<script>
function updateTime() {
    var date = new Date();
    var now = date.getTime();
    var startDate = new Date("2024/06/27 10:21:33");
    var start = startDate.getTime();
    var diff = now - start;
    var y, d, h, m;
    y = Math.floor(diff / (365 * 24 * 3600 * 1000));
    diff -= y * 365 * 24 * 3600 * 1000;
    d = Math.floor(diff / (24 * 3600 * 1000));
    h = Math.floor(diff / (3600 * 1000) % 24);
    m = Math.floor(diff / (60 * 1000) % 60);
    if (y == 0) {
        document.getElementById("web-time").innerHTML = d + "<span class=\"heti-spacing\"> </span>天<span class=\"heti-spacing\"> </span>" + h + "<span class=\"heti-spacing\"> </span>小时<span class=\"heti-spacing\"> </span>" + m + "<span class=\"heti-spacing\"> </span>分钟";
    } else {
        document.getElementById("web-time").innerHTML = y + "<span class=\"heti-spacing\"> </span>年<span class=\"heti-spacing\"> </span>" + d + "<span class=\"heti-spacing\"> </span>天<span class=\"heti-spacing\"> </span>" + h + "<span class=\"heti-spacing\"> </span>小时<span class=\"heti-spacing\"> </span>" + m + "<span class=\"heti-spacing\"> </span>分钟";
    }
    setTimeout(updateTime, 1000 * 60);
}
updateTime();
function toggle_statistics() {
    var statistics = document.getElementById("statistics");
    if (statistics.style.opacity == 0) {
        statistics.style.opacity = 1;
    } else {
        statistics.style.opacity = 0;
    }
}
</script>