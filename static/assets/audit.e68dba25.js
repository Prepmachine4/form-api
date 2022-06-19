import{o as D,f as $,r as v,d as P,a1 as L,s as U,a2 as W,aM as z,aN as A,av as H,D as F,G as J,I as O,L as q,j as a,k as i,h as E,g as _,q as g,p as G,n as K,E as Q}from"./vendor.3bf6c43c.js";import{_ as B,a as Z,b as j,D as tt,p as et}from"./index.af28e13d.js";const st={props:{width:{type:Number,default:800},height:{type:Number,default:300},lineWidth:{type:Number,default:4},lineColor:{type:String,default:"#000000"},bgColor:{type:String,default:""},isCrop:{type:Boolean,default:!1},isClearBgColor:{type:Boolean,default:!0}},data(){return{hasDrew:!1,resultImg:"",points:[],canvasTxt:null,startX:0,startY:0,isDrawing:!1,sratio:1}},computed:{ratio(){return this.height/this.width},stageInfo(){return this.$refs.canvas.getBoundingClientRect()},myBg(){return this.bgColor?this.bgColor:"rgba(255, 255, 255, 0)"}},watch:{myBg:function(t){this.$refs.canvas.style.background=t}},beforeMount(){window.addEventListener("resize",this.$_resizeHandler)},beforeDestroy(){window.removeEventListener("resize",this.$_resizeHandler)},mounted(){const t=this.$refs.canvas;t.height=this.height,t.width=this.width,t.style.background=this.myBg,this.$_resizeHandler(),document.onmouseup=()=>{this.isDrawing=!1}},methods:{$_resizeHandler(){const t=this.$refs.canvas;t.style.width=this.width+"px";const e=parseFloat(window.getComputedStyle(t).width);t.style.height=this.ratio*e+"px",this.canvasTxt=t.getContext("2d"),this.canvasTxt.scale(1*this.sratio,1*this.sratio),this.sratio=e/this.width,this.canvasTxt.scale(1/this.sratio,1/this.sratio)},mouseDown(t){t=t||event,t.preventDefault(),this.isDrawing=!0,this.hasDrew=!0;let e={x:t.offsetX,y:t.offsetY};this.drawStart(e)},mouseMove(t){if(t=t||event,t.preventDefault(),this.isDrawing){let e={x:t.offsetX,y:t.offsetY};this.drawMove(e)}},mouseUp(t){t=t||event,t.preventDefault();let e={x:t.offsetX,y:t.offsetY};this.drawEnd(e),this.isDrawing=!1},touchStart(t){if(t=t||event,t.preventDefault(),this.hasDrew=!0,t.touches.length===1){let e={x:t.targetTouches[0].clientX-this.$refs.canvas.getBoundingClientRect().left,y:t.targetTouches[0].clientY-this.$refs.canvas.getBoundingClientRect().top};this.drawStart(e)}},touchMove(t){if(t=t||event,t.preventDefault(),t.touches.length===1){let e={x:t.targetTouches[0].clientX-this.$refs.canvas.getBoundingClientRect().left,y:t.targetTouches[0].clientY-this.$refs.canvas.getBoundingClientRect().top};this.drawMove(e)}},touchEnd(t){if(t=t||event,t.preventDefault(),t.touches.length===1){let e={x:t.targetTouches[0].clientX-this.$refs.canvas.getBoundingClientRect().left,y:t.targetTouches[0].clientY-this.$refs.canvas.getBoundingClientRect().top};this.drawEnd(e)}},drawStart(t){this.startX=t.x,this.startY=t.y,this.canvasTxt.beginPath(),this.canvasTxt.moveTo(this.startX,this.startY),this.canvasTxt.lineTo(t.x,t.y),this.canvasTxt.lineCap="round",this.canvasTxt.lineJoin="round",this.canvasTxt.lineWidth=this.lineWidth*this.sratio,this.canvasTxt.stroke(),this.canvasTxt.closePath(),this.points.push(t)},drawMove(t){this.canvasTxt.beginPath(),this.canvasTxt.moveTo(this.startX,this.startY),this.canvasTxt.lineTo(t.x,t.y),this.canvasTxt.strokeStyle=this.lineColor,this.canvasTxt.lineWidth=this.lineWidth*this.sratio,this.canvasTxt.lineCap="round",this.canvasTxt.lineJoin="round",this.canvasTxt.stroke(),this.canvasTxt.closePath(),this.startY=t.y,this.startX=t.x,this.points.push(t)},drawEnd(t){this.canvasTxt.beginPath(),this.canvasTxt.moveTo(this.startX,this.startY),this.canvasTxt.lineTo(t.x,t.y),this.canvasTxt.lineCap="round",this.canvasTxt.lineJoin="round",this.canvasTxt.stroke(),this.canvasTxt.closePath(),this.points.push(t),this.points.push({x:-1,y:-1})},generate(){return new Promise((e,u)=>{if(!this.hasDrew){u("Warning: Not Signned!");return}var l=this.canvasTxt.getImageData(0,0,this.$refs.canvas.width,this.$refs.canvas.height);this.canvasTxt.globalCompositeOperation="destination-over",this.canvasTxt.fillStyle=this.myBg,this.canvasTxt.fillRect(0,0,this.$refs.canvas.width,this.$refs.canvas.height),this.resultImg=this.$refs.canvas.toDataURL();var h=this.resultImg;if(this.canvasTxt.clearRect(0,0,this.$refs.canvas.width,this.$refs.canvas.height),this.canvasTxt.putImageData(l,0,0),this.canvasTxt.globalCompositeOperation="source-over",this.isCrop){const n=this.getCropArea(l.data);var s=document.createElement("canvas");const o=s.getContext("2d");s.width=n[2]-n[0],s.height=n[3]-n[1];const p=this.canvasTxt.getImageData(...n);o.globalCompositeOperation="destination-over",o.putImageData(p,0,0),o.fillStyle=this.myBg,o.fillRect(0,0,s.width,s.height),h=s.toDataURL(),s=null}e(h)})},reset(){this.canvasTxt.clearRect(0,0,this.$refs.canvas.width,this.$refs.canvas.height),this.isClearBgColor&&(this.$emit("update:bgColor",""),this.$refs.canvas.style.background="rgba(255, 255, 255, 0)"),this.points=[],this.hasDrew=!1,this.resultImg=""},getCropArea(t){for(var e=this.$refs.canvas.width,u=0,l=this.$refs.canvas.height,h=0,s=0;s<this.$refs.canvas.width;s++)for(var n=0;n<this.$refs.canvas.height;n++){var o=(s+this.$refs.canvas.width*n)*4;(t[o]>0||t[o+1]>0||t[o+2]||t[o+3]>0)&&(h=Math.max(n,h),u=Math.max(s,u),l=Math.min(n,l),e=Math.min(s,e))}return e++,u++,l++,h++,[e,l,u,h]}}};function at(t,e,u,l,h,s){return D(),$("canvas",{ref:"canvas",onMousedown:e[0]||(e[0]=(...n)=>s.mouseDown&&s.mouseDown(...n)),onMousemove:e[1]||(e[1]=(...n)=>s.mouseMove&&s.mouseMove(...n)),onMouseup:e[2]||(e[2]=(...n)=>s.mouseUp&&s.mouseUp(...n)),onTouchstart:e[3]||(e[3]=(...n)=>s.touchStart&&s.touchStart(...n)),onTouchmove:e[4]||(e[4]=(...n)=>s.touchMove&&s.touchMove(...n)),onTouchend:e[5]||(e[5]=(...n)=>s.touchEnd&&s.touchEnd(...n))},null,544)}var x=B(st,[["render",at],["__scopeId","data-v-acbd7c1e"]]);x.install=function(t){this.installed||(this.installed=!0,t.component("vueEsign",x))};const I=t=>(G("data-v-3f213102"),t=t(),K(),t),nt={class:"app-container"},it=g("\u5BA1\u6838 "),ot=g("\u5BA1\u6279\u610F\u89C1"),lt={style:{display:"flex",width:"100%","justify-content":"center"}},rt=I(()=>_("br",null,null,-1)),ht={style:{"text-align":"center"}},dt=g("\u6E05\u7A7A"),ut=g("\u901A\u8FC7"),ct=g("\u4E0D\u901A\u8FC7"),vt=I(()=>_("br",null,null,-1)),ft={setup(t){const e=v([]),u=v([]),l=v(!1),h=v(),s=v(),n=v(),o=v(""),p=v(),M=P(),S=c=>{p.value=c,h.value=c.data,s.value=c.form._id,l.value=!0};function w(){Z().then(c=>e.value=c.data),j().then(c=>u.value=c.data)}const k=()=>{o.value="",n.value.reset()},T=c=>{n.value.generate().then(d=>{console.log(d),et(p.value._id,{user_id:M.state.userInfo._id,index:p.value.audit_user_index,opinion:o.value,sign:d,result:c}).then(r=>{l.value=!1,Q.success("\u5BA1\u6838\u6210\u529F"),w()})})};return w(),(c,d)=>{const r=L,m=U,b=W,y=z,R=A,X=H,Y=F,C=J,N=O,V=q;return D(),$("div",nt,[a(R,{"tab-position":"left"},{default:i(()=>[a(y,{label:"\u7B49\u5F85\u5BA1\u6279"},{default:i(()=>[a(b,{data:e.value},{default:i(()=>[a(r,{type:"index",align:"center"}),a(r,{label:"\u4E1A\u52A1\u540D\u79F0",align:"center",prop:"form.name"}),a(r,{label:"\u586B\u5199\u4EBA",align:"center",prop:"user.name"}),a(r,{label:"\u586B\u5199\u8005\u90E8\u95E8",align:"center",prop:"user.deptName"}),a(r,{label:"\u586B\u5199\u65F6\u95F4",align:"center",prop:"create_time",width:"180"}),a(r,{label:"\u64CD\u4F5C",align:"center","class-name":"small-padding fixed-width"},{default:i(f=>[a(m,{text:"",icon:"View",onClick:pt=>S(f.row)},{default:i(()=>[it]),_:2},1032,["onClick"])]),_:1})]),_:1},8,["data"])]),_:1}),a(y,{label:"\u5BA1\u6279\u5386\u53F2"},{default:i(()=>[a(b,{data:u.value},{default:i(()=>[a(r,{type:"index",align:"center"}),a(r,{label:"\u4E1A\u52A1\u540D\u79F0",align:"center",prop:"form.name"}),a(r,{label:"\u586B\u5199\u4EBA",align:"center",prop:"user.name"}),a(r,{label:"\u586B\u5199\u8005\u90E8\u95E8",align:"center",prop:"user.deptName"}),a(r,{label:"\u586B\u5199\u65F6\u95F4",align:"center",prop:"create_time",width:"180"})]),_:1},8,["data"])]),_:1})]),_:1}),a(V,{top:"5vh",title:"\u5BA1\u6838",modelValue:l.value,"onUpdate:modelValue":d[3]||(d[3]=f=>l.value=f),width:"80vw"},{default:i(()=>[a(E(tt),{"form-id":s.value,"enable-edit":!1,"form-data":h.value},null,8,["form-id","form-data"]),a(X,null,{default:i(()=>[ot]),_:1}),_("span",lt,[a(N,{style:{width:"30vw",border:"1px dashed gray",padding:"20px"}},{default:i(()=>[a(C,{label:"\u610F\u89C1"},{default:i(()=>[a(Y,{modelValue:o.value,"onUpdate:modelValue":d[0]||(d[0]=f=>o.value=f)},null,8,["modelValue"])]),_:1}),a(C,{required:"",label:"\u7B7E\u540D"},{default:i(()=>[a(E(x),{ref_key:"sign",ref:n,isClearBgColor:!1,bgColor:"#eceef1",width:300,height:150,isCrop:!1,lineWidth:6,lineColor:"#000000"},null,512)]),_:1})]),_:1})]),rt,_("div",ht,[a(m,{type:"info",onClick:k},{default:i(()=>[dt]),_:1}),a(m,{type:"success",onClick:d[1]||(d[1]=f=>T(!0))},{default:i(()=>[ut]),_:1}),a(m,{type:"danger",onClick:d[2]||(d[2]=f=>T(!1))},{default:i(()=>[ct]),_:1})]),vt]),_:1},8,["modelValue"])])}}};var _t=B(ft,[["__scopeId","data-v-3f213102"]]);export{_t as default};
