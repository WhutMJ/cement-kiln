  window.onload=function(){
    var line=document.getElementById('line');
    var first=document.getElementById('fst');
  var second=document.getElementById('snd');
  var box=document.getElementById('box1')

    line.onmousedown = function(e){
        var e=e||window.event;
        if(typeof line.setCapture!='undefined'){  
            line.setCapture();  
          };//兼容不同浏览器版本
        document.onmousemove=function(e){
            var e=e||window.event;
            var firH=e.pageY-fst.offsetTop;
            first.style.height=firH+'px';
            line.style.offsetTop=first.height+'px';
            document.onmouseup = function(e) { //当鼠标弹起来的时候不再移动  
            this.onmousemove = null;  
            this.onmouseup = null; //预防鼠标弹起来后还会循环（即预防鼠标放上去的时候还会移动）  
  
            //修复低版本ie bug  
            if(typeof line.releaseCapture!='undefined'){  
                line.releaseCapture();  
            };  
        };

    };

};

};