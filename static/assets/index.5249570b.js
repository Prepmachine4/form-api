import{_ as ce,u as me,r,q as _e,aG as fe,D as ve,A as ge,aH as he,a5 as be,n as ye,a7 as xe,W as Ve,a6 as ke,ae as we,X as Ie,B as Ee,aI as Ue,ab as Ce,ac as Ne,C as Te,as as Be,aJ as De,aD as Re,f as E,j as e,k as l,o as d,g as P,w as y,y as i,U as B,V as D,m as g,N as M,z as U,h as s,aK as je,E as R,aL as qe}from"./vendor.3587a8c4.js";/* empty css                   */import{l as Pe}from"./role.b9a765ba.js";import{t as z}from"./dept.6045f47f.js";import{a as Le,b as Se,g as Fe,c as Oe,u as $e,e as Ae,f as Me}from"./index.f1e71e2e.js";const ze={class:"app-container"},Ge={class:"head-container"},He={class:"head-container"},Je=g("\u6DFB\u52A0\u7528\u6237"),Ke=g("\u5173\u8054\u5DF2\u6709\u7528\u6237"),We=g("\u5BFC\u51FA"),Xe={class:"dialog-footer"},Qe=g("\u786E \u5B9A"),Ye=g("\u53D6 \u6D88"),Ze={setup(el){me();const{proxy:G}=qe(),L=r([]),c=r(!1),j=r(!0),S=r([]);r(!0);const h=r("");r([]),r("");const x=r(void 0),C=r([]),N=r([]),V=r(""),m=r(),H=_e({form:{},rules:{name:[{required:!0,message:"\u8BF7\u8F93\u5165\u7528\u6237\u59D3\u540D",trigger:"blur"}],nick_name:[{required:!0,message:"\u7528\u6237\u6635\u79F0\u4E0D\u80FD\u4E3A\u7A7A",trigger:"blur"}],password:[{required:!0,message:"\u7528\u6237\u5BC6\u7801\u4E0D\u80FD\u4E3A\u7A7A",trigger:"blur"},{min:5,max:20,message:"\u7528\u6237\u5BC6\u7801\u957F\u5EA6\u5FC5\u987B\u4ECB\u4E8E 5 \u548C 20 \u4E4B\u95F4",trigger:"blur"}],email:[{required:!0,type:"email",message:"\u8BF7\u8F93\u5165\u6B63\u786E\u7684\u90AE\u7BB1\u5730\u5740",trigger:["blur","change"]}],phone:[{required:!0,pattern:/^1[3|4|5|6|7|8|9][0-9]\d{8}$/,message:"\u8BF7\u8F93\u5165\u6B63\u786E\u7684\u624B\u673A\u53F7\u7801",trigger:"blur"}]}}),{form:o,rules:J}=fe(H);function K(){z().then(n=>{x.value=n.data})}function k(){j.value=!0,Se().then(n=>{j.value=!1,L.value=n.data})}const W=ve(()=>L.value.filter(n=>!V.value||n.dept.deptName.includes(V.value)));function X(n){V.value=n.label}const Q=n=>{if(N.value.length!==0)return N.value.filter(t=>t._id===n)[0].roleName},Y=n=>{if(C.value.length!==0)return C.value.filter(t=>t._id===n)[0].postName};async function Z(n){T(),q(),m.value=2;const t=n._id||S.value;let p=await Fe(t);o.value=p.data,o.value.postIds=p.data.postIds,o.value.roleIds=p.data.roleIds,c.value=!0,h.value="\u4FEE\u6539\u7528\u6237"}function ee(n){const t=n._id||S.value;je.confirm('\u662F\u5426\u786E\u8BA4\u5220\u9664\u7528\u6237\u90AE\u7BB1\u4E3A"'+n.email+'"\u7684\u6570\u636E\u9879\uFF1F',{confirmButtonText:"\u786E\u5B9A",cancelButtonText:"\u53D6\u6D88",type:"warning"}).then(function(){return Oe(t)}).then(()=>{k(),R.success("\u5220\u9664\u6210\u529F")}).catch(()=>{})}function le(){}function q(){x.value===void 0&&z().then(n=>{x.value=n.data})}function T(){o.value={_id:void 0,deptId:void 0,name:void 0,nick_name:void 0,phone:void 0,email:void 0,postIds:[],roleIds:[]}}function ae(){c.value=!1,T(),m.value=void 0}function te(){T(),q(),m.value=0,c.value=!0,h.value="\u6DFB\u52A0\u7528\u6237"}function ne(){T(),q(),m.value=1,c.value=!0,h.value="\u5173\u8054\u5DF2\u6709\u7528\u6237"}function oe(){G.$refs.userRef.validate(n=>{n&&(h.value==="\u4FEE\u6539\u7528\u6237"?$e(o.value).then(t=>{R.success("\u4FEE\u6539\u6210\u529F"),c.value=!1,k()}):h.value==="\u5173\u8054\u5DF2\u6709\u7528\u6237"?Ae(o.value).then(t=>{R.success("\u5173\u8054\u6210\u529F"),c.value=!1,k()}):Me(o.value).then(t=>{R.success("\u65B0\u589E\u6210\u529F"),c.value=!1,k()}))})}return K(),k(),Le().then(n=>C.value=n.data),Pe().then(n=>N.value=n.data),(n,t)=>{const p=ge,se=he,u=be,v=ye,b=xe,_=Ve,F=ke,O=we,de=Ie,f=Ee,ue=Ue,$=Ce,A=Ne,re=Te,ie=Be,w=De("hasPermi"),pe=Re;return d(),E("div",ze,[e(b,{gutter:20},{default:l(()=>[e(u,{span:4,xs:24},{default:l(()=>[P("div",Ge,[e(p,{modelValue:V.value,"onUpdate:modelValue":t[0]||(t[0]=a=>V.value=a),placeholder:"\u8BF7\u8F93\u5165\u90E8\u95E8\u540D\u79F0",clearable:"","prefix-icon":"Search",style:{"margin-bottom":"20px"}},null,8,["modelValue"])]),P("div",He,[e(se,{data:x.value,props:{label:"label",children:"children"},"expand-on-click-node":!1,ref:"deptTreeRef","default-expand-all":"",onNodeClick:X},null,8,["data"])])]),_:1}),e(u,{span:20,xs:24},{default:l(()=>[e(b,{gutter:10,class:"mb8"},{default:l(()=>[e(u,{span:1.5},{default:l(()=>[y((d(),i(v,{type:"primary",plain:"",icon:"Plus",onClick:te},{default:l(()=>[Je]),_:1})),[[w,["system:user:add"]]])]),_:1},8,["span"]),e(u,{span:1.5},{default:l(()=>[y((d(),i(v,{type:"primary",plain:"",icon:"Plus",onClick:ne},{default:l(()=>[Ke]),_:1})),[[w,["system:user:add"]]])]),_:1},8,["span"]),e(u,{span:1.5},{default:l(()=>[y((d(),i(v,{type:"warning",plain:"",icon:"Download",onClick:le},{default:l(()=>[We]),_:1})),[[w,["system:user:export"]]])]),_:1},8,["span"])]),_:1}),y((d(),i(de,{data:s(W)},{default:l(()=>[e(_,{type:"index"}),e(_,{label:"\u7528\u6237\u90AE\u7BB1",align:"center",key:"email",prop:"email","show-overflow-tooltip":!0}),e(_,{label:"\u7528\u6237\u59D3\u540D",align:"center",key:"name",prop:"name","show-overflow-tooltip":!0}),e(_,{label:"\u90E8\u95E8",align:"center",key:"deptName",prop:"dept.deptName","show-overflow-tooltip":!0}),e(_,{label:"\u89D2\u8272"},{default:l(a=>[(d(!0),E(B,null,D(a.row.roleIds,I=>(d(),i(F,{style:{margin:"0 2px"}},{default:l(()=>[g(M(Q(I)),1)]),_:2},1024))),256))]),_:1}),e(_,{label:"\u5C97\u4F4D"},{default:l(a=>[(d(!0),E(B,null,D(a.row.postIds,I=>(d(),i(F,{style:{margin:"0 2px"}},{default:l(()=>[g(M(Y(I)),1)]),_:2},1024))),256))]),_:1}),e(_,{label:"\u624B\u673A\u53F7\u7801",align:"center",key:"phone",prop:"phone"}),e(_,{label:"\u64CD\u4F5C",align:"center",width:"150","class-name":"small-padding fixed-width"},{default:l(a=>[a.row._id!==a.row.enterprise_id?(d(),i(O,{key:0,content:"\u4FEE\u6539",placement:"top"},{default:l(()=>[y(e(v,{type:"text",icon:"Edit",onClick:I=>Z(a.row)},null,8,["onClick"]),[[w,["system:user:edit"]]])]),_:2},1024)):U("",!0),a.row._id!==a.row.enterprise_id?(d(),i(O,{key:1,content:"\u5220\u9664",placement:"top"},{default:l(()=>[y(e(v,{type:"text",icon:"Delete",onClick:I=>ee(a.row)},null,8,["onClick"]),[[w,["system:user:remove"]]])]),_:2},1024)):U("",!0)]),_:1})]),_:1},8,["data"])),[[pe,j.value]])]),_:1})]),_:1}),e(ie,{title:h.value,modelValue:c.value,"onUpdate:modelValue":t[9]||(t[9]=a=>c.value=a),width:"600px","append-to-body":""},{footer:l(()=>[P("div",Xe,[e(v,{type:"primary",onClick:oe},{default:l(()=>[Qe]),_:1}),e(v,{onClick:ae},{default:l(()=>[Ye]),_:1})])]),default:l(()=>[e(re,{model:s(o),rules:s(J),ref:"userRef","label-width":"80px"},{default:l(()=>[e(b,null,{default:l(()=>[e(u,{span:12},{default:l(()=>[e(f,{label:"\u90AE\u7BB1",prop:"email"},{default:l(()=>[e(p,{disabled:m.value===2,modelValue:s(o).email,"onUpdate:modelValue":t[1]||(t[1]=a=>s(o).email=a),placeholder:"\u8BF7\u8F93\u5165\u90AE\u7BB1",maxlength:"50"},null,8,["disabled","modelValue"])]),_:1})]),_:1}),e(u,{span:12},{default:l(()=>[e(f,{label:"\u5F52\u5C5E\u90E8\u95E8",prop:"deptId"},{default:l(()=>[e(ue,{modelValue:s(o).deptId,"onUpdate:modelValue":t[2]||(t[2]=a=>s(o).deptId=a),data:x.value,props:{value:"id",label:"label",children:"children"},"value-key":"id","default-expand-all":"",placeholder:"\u8BF7\u9009\u62E9\u5F52\u5C5E\u90E8\u95E8","check-strictly":""},null,8,["modelValue","data"])]),_:1})]),_:1})]),_:1}),m.value!==1?(d(),i(b,{key:0},{default:l(()=>[e(u,{span:12},{default:l(()=>[e(f,{label:"\u624B\u673A\u53F7\u7801",prop:"phone"},{default:l(()=>[e(p,{modelValue:s(o).phone,"onUpdate:modelValue":t[3]||(t[3]=a=>s(o).phone=a),placeholder:"\u8BF7\u8F93\u5165\u624B\u673A\u53F7\u7801",maxlength:"11"},null,8,["modelValue"])]),_:1})]),_:1}),e(u,{span:12},{default:l(()=>[e(f,{label:"\u7528\u6237\u6635\u79F0",prop:"nick_name"},{default:l(()=>[e(p,{modelValue:s(o).nick_name,"onUpdate:modelValue":t[4]||(t[4]=a=>s(o).nick_name=a),placeholder:"\u8BF7\u8F93\u5165\u7528\u6237\u6635\u79F0",maxlength:"30"},null,8,["modelValue"])]),_:1})]),_:1})]),_:1})):U("",!0),m.value!==1?(d(),i(b,{key:1},{default:l(()=>[e(u,{span:12},{default:l(()=>[e(f,{label:"\u7528\u6237\u540D\u79F0",prop:"name"},{default:l(()=>[e(p,{modelValue:s(o).name,"onUpdate:modelValue":t[5]||(t[5]=a=>s(o).name=a),placeholder:"\u8BF7\u8F93\u5165\u7528\u6237\u540D\u79F0",maxlength:"30"},null,8,["modelValue"])]),_:1})]),_:1}),e(u,{span:12},{default:l(()=>[m.value!==2?(d(),i(f,{key:0,label:"\u7528\u6237\u5BC6\u7801",prop:"password"},{default:l(()=>[e(p,{modelValue:s(o).password,"onUpdate:modelValue":t[6]||(t[6]=a=>s(o).password=a),placeholder:"\u8BF7\u8F93\u5165\u7528\u6237\u5BC6\u7801",type:"password",maxlength:"20","show-password":""},null,8,["modelValue"])]),_:1})):U("",!0)]),_:1})]),_:1})):U("",!0),e(b,null,{default:l(()=>[e(u,{span:12},{default:l(()=>[e(f,{label:"\u5C97\u4F4D"},{default:l(()=>[e(A,{modelValue:s(o).postIds,"onUpdate:modelValue":t[7]||(t[7]=a=>s(o).postIds=a),multiple:"",placeholder:"\u8BF7\u9009\u62E9"},{default:l(()=>[(d(!0),E(B,null,D(C.value,a=>(d(),i($,{key:a._id,label:a.postName,value:a._id},null,8,["label","value"]))),128))]),_:1},8,["modelValue"])]),_:1})]),_:1}),e(u,{span:12},{default:l(()=>[e(f,{label:"\u89D2\u8272"},{default:l(()=>[e(A,{modelValue:s(o).roleIds,"onUpdate:modelValue":t[8]||(t[8]=a=>s(o).roleIds=a),multiple:"",placeholder:"\u8BF7\u9009\u62E9"},{default:l(()=>[(d(!0),E(B,null,D(N.value,a=>(d(),i($,{key:a._id,label:a.roleName,value:a._id},null,8,["label","value"]))),128))]),_:1},8,["modelValue"])]),_:1})]),_:1})]),_:1})]),_:1},8,["model","rules"])]),_:1},8,["title","modelValue"])])}}};var sl=ce(Ze,[["__scopeId","data-v-3f6e51cc"]]);export{sl as default};