<div class="post-body">
   <div id="links">
      <style>
/* 用于大屏幕和小屏幕的通用样式 */
.card {
    width: 45%;
    font-size: 1rem;
    padding: 10px 20px;
    border-radius: 4px;
    transition-duration: 0.15s;
    margin-bottom: 1rem;
    display: flex;
 }
 .card:nth-child(odd) {
    float: left;
 }
 .card:nth-child(even) {
    float: right;
 }
 .card:hover {
    transform: scale(1.1);
    box-shadow: 0 2px 6px 0 rgba(0, 0, 0, 0.12), 0 0 6px 0 rgba(0, 0, 0, 0.04);
 }
 .card a {
    border: none;
 }
 .card .ava {
    width: 3rem!important;
    height: 3rem!important;
    margin: 0!important;
    margin-right: 1em!important;
    border-radius: 4px;
 }
 .card .card-header {
    font-style: italic;
    overflow: hidden;
    width: 100%;
 }
 .card .card-header a {
    font-style: normal;
    color: #608DBD;
    font-weight: bold;
    text-decoration: none;
 }
 .card .card-header a:hover {
    color: #d480aa;
    text-decoration: none;
 }
 .card .card-header .info {
    font-style: normal;
    color: #a3a3a3;
    font-size: 14px;
    min-width: 0;
    overflow: hidden;
    white-space: nowrap;
 }
 /* 媒体查询：小屏幕 */
 @media (max-width: 768px) {
    .card {
       width: 100%; /* 在小屏幕上显示为单列 */
       float: none; /* 清除浮动 */
    }
 }
      </style>
      <div class="links-content">
         <div class="link-navigation">
            <div class="card">
               <img class="ava" src="/assets/zsy_avatar.jpg" />
               <div class="card-header">
                  <div>
                     <a href="http://donotknowsjtu.top " target=“_blank”>donot-know's blog</a>
                  </div>
                  <div class="info">阳光开朗大男孩。</div>
               </div>
            </div>
            <div class="card">
               <img class="ava" src="https://s2.loli.net/2025/03/19/efFOsAY2MdwDH7S.jpg"/>
               <div class="card-header">
                  <div>
                     <a href="https://awslasasd.github.io/" target=“_blank”>Twinkle's blog</a>
                  </div>
                  <div class="info">帅气迷人大瑶瑶</div>
               </div>
            </div>
         </div>
      </div>
   </div>
</div>