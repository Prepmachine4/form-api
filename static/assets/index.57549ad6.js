import{u as ke,r as p,q as Y,a as Ve,aM as we,D as Ie,A as Ue,aN as Ee,a8 as Ce,n as Ne,aa as Te,Z as Re,a9 as Be,ah as Se,_ as De,B as Fe,aO as je,ae as Pe,af as qe,C as $e,ay as Le,e as Oe,S as Ae,aP as Me,ar as ze,aJ as Qe,f as N,j as l,k as e,h as n,o as d,g as b,w,y as u,Q as F,Y as j,m as _,R as Z,z as T,p as Je,l as Ye,E as I,U as Ze,aQ as Ge}from"./vendor.7785c9e9.js";/* empty css                   *//* empty css                */import{t as G}from"./dept.f6a65b77.js";import{_ as He,c as Ke,e as We,f as Xe,g as el,h as ll,u as al,i as tl,j as ol}from"./index.6d080563.js";import{l as nl}from"./role.c795adef.js";const H=R=>(Je("data-v-9813b2b4"),R=R(),Ye(),R),sl={class:"app-container"},dl={class:"head-container"},ul={class:"head-container"},rl=_("\u6DFB\u52A0\u7528\u6237"),il=_("\u5173\u8054\u5DF2\u6709\u7528\u6237"),pl=_("\u5BFC\u5165"),cl=_("\u4FEE\u6539"),_l=_("\u5220\u9664"),ml={class:"dialog-footer"},fl=_("\u786E \u5B9A"),vl=_("\u53D6 \u6D88"),gl=H(()=>b("div",{class:"el-upload__text"},[_("\u5C06\u6587\u4EF6\u62D6\u5230\u6B64\u5904\uFF0C\u6216"),b("em",null,"\u70B9\u51FB\u4E0A\u4F20")],-1)),hl=H(()=>b("div",{class:"el-upload__tip text-center"},[b("span",null,"\u4EC5\u5141\u8BB8\u5BFC\u5165xls\u3001xlsx\u683C\u5F0F\u6587\u4EF6\u3002")],-1)),bl={class:"dialog-footer"},xl=_("\u786E \u5B9A"),yl=_("\u53D6 \u6D88"),kl={setup(R){ke();const{proxy:P}=Ge(),L=p([]),m=p(!1),q=p(!0),O=p([]);p(!0);const x=p("");p([]),p("");const U=p(void 0),B=p([]),S=p([]),E=p(""),v=p(),K=Y({form:{},rules:{name:[{required:!0,message:"\u8BF7\u8F93\u5165\u7528\u6237\u59D3\u540D",trigger:"blur"}],nick_name:[{required:!0,message:"\u7528\u6237\u6635\u79F0\u4E0D\u80FD\u4E3A\u7A7A",trigger:"blur"}],password:[{required:!0,message:"\u7528\u6237\u5BC6\u7801\u4E0D\u80FD\u4E3A\u7A7A",trigger:"blur"},{min:5,max:20,message:"\u7528\u6237\u5BC6\u7801\u957F\u5EA6\u5FC5\u987B\u4ECB\u4E8E 5 \u548C 20 \u4E4B\u95F4",trigger:"blur"}],email:[{required:!0,type:"email",message:"\u8BF7\u8F93\u5165\u6B63\u786E\u7684\u90AE\u7BB1\u5730\u5740",trigger:["blur","change"]}],phone:[{required:!0,pattern:/^1[3|4|5|6|7|8|9][0-9]\d{8}$/,message:"\u8BF7\u8F93\u5165\u6B63\u786E\u7684\u624B\u673A\u53F7\u7801",trigger:"blur"}],deptId:[{required:!0,message:"\u9009\u62E9\u90E8\u95E8",trigger:"blur"}]}}),c=Y({open:!1,title:"",isUploading:!1,headers:{Authorization:"Bearer "+localStorage.getItem("token")},url:Ve.defaults.baseURL+"/system/user/batch/"+Ke.state.userInfo.enterprise_id});function W(){c.title="\u7528\u6237\u5BFC\u5165",c.open=!0}const X=(o,t,r)=>{c.isUploading=!0};function ee(){P.$refs.uploadRef.submit()}const le=(o,t,r)=>{console.log(o,t,r),c.open=!1,c.isUploading=!1,P.$refs.uploadRef.clearFiles(),I.success("\u5BFC\u5165\u6210\u529F"),y()},{form:s,rules:ae}=we(K);function te(){G().then(o=>{U.value=o.data})}function y(){q.value=!0,Xe().then(o=>{q.value=!1,L.value=o.data})}const oe=Ie(()=>L.value.filter(o=>!E.value||o.dept.deptName.includes(E.value)));function ne(o){E.value=o.label}const se=o=>{if(S.value.length!==0)return S.value.filter(t=>t._id===o)[0].roleName},de=o=>{if(B.value.length!==0)return B.value.filter(t=>t._id===o)[0].postName};async function ue(o){D(),$(),v.value=2;const t=o._id||O.value;let r=await el(t);s.value=r.data,s.value.postIds=r.data.postIds,s.value.roleIds=r.data.roleIds,m.value=!0,x.value="\u4FEE\u6539\u7528\u6237"}function re(o){const t=o._id||O.value;Ze.confirm('\u662F\u5426\u786E\u8BA4\u5220\u9664\u7528\u6237\u90AE\u7BB1\u4E3A"'+o.email+'"\u7684\u6570\u636E\u9879\uFF1F',{confirmButtonText:"\u786E\u5B9A",cancelButtonText:"\u53D6\u6D88",type:"warning"}).then(function(){return ll(t)}).then(()=>{y(),I.success("\u5220\u9664\u6210\u529F")}).catch(()=>{})}function $(){U.value===void 0&&G().then(o=>{U.value=o.data})}function D(){s.value={_id:void 0,deptId:void 0,name:void 0,nick_name:void 0,phone:void 0,email:void 0,postIds:[],roleIds:[]}}function ie(){m.value=!1,D(),v.value=void 0}function pe(){D(),$(),v.value=0,m.value=!0,x.value="\u6DFB\u52A0\u7528\u6237"}function ce(){D(),$(),v.value=1,m.value=!0,x.value="\u5173\u8054\u5DF2\u6709\u7528\u6237"}function _e(){P.$refs.userRef.validate(o=>{o&&(x.value==="\u4FEE\u6539\u7528\u6237"?al(s.value).then(t=>{I.success("\u4FEE\u6539\u6210\u529F"),m.value=!1,y()}):x.value==="\u5173\u8054\u5DF2\u6709\u7528\u6237"?tl(s.value).then(t=>{if(t.status!==200){I.error(t.data);return}I.success("\u5173\u8054\u6210\u529F"),m.value=!1,y()}):ol(s.value).then(t=>{I.success("\u65B0\u589E\u6210\u529F"),m.value=!1,y()}))})}return te(),y(),We().then(o=>B.value=o.data),nl().then(o=>S.value=o.data),(o,t)=>{const r=Ue,me=Ee,i=Ce,f=Ne,k=Te,g=Re,A=Be,M=Se,fe=De,h=Fe,ve=je,z=Pe,Q=qe,ge=$e,J=Le,he=Oe("upload-filled"),be=Ae,xe=Me,V=ze("hasPermi"),ye=Qe;return d(),N("div",sl,[l(k,{gutter:20},{default:e(()=>[l(i,{span:4,xs:24},{default:e(()=>[b("div",dl,[l(r,{modelValue:E.value,"onUpdate:modelValue":t[0]||(t[0]=a=>E.value=a),placeholder:"\u8BF7\u8F93\u5165\u90E8\u95E8\u540D\u79F0",clearable:"","prefix-icon":"Search",style:{"margin-bottom":"20px"}},null,8,["modelValue"])]),b("div",ul,[l(me,{data:U.value,props:{label:"label",children:"children"},"expand-on-click-node":!1,ref:"deptTreeRef","default-expand-all":"",onNodeClick:ne},null,8,["data"])])]),_:1}),l(i,{span:20,xs:24},{default:e(()=>[l(k,{gutter:10,class:"mb8"},{default:e(()=>[l(i,{span:1.5},{default:e(()=>[w((d(),u(f,{type:"primary",plain:"",icon:"Plus",onClick:pe},{default:e(()=>[rl]),_:1})),[[V,"1002"]])]),_:1},8,["span"]),l(i,{span:1.5},{default:e(()=>[w((d(),u(f,{type:"primary",plain:"",icon:"Plus",onClick:ce},{default:e(()=>[il]),_:1})),[[V,"1002"]])]),_:1},8,["span"]),l(i,{span:1.5},{default:e(()=>[w((d(),u(f,{type:"success",plain:"",icon:"Upload",onClick:W},{default:e(()=>[pl]),_:1})),[[V,"1002"]])]),_:1},8,["span"])]),_:1}),w((d(),u(fe,{data:n(oe)},{default:e(()=>[l(g,{type:"index"}),l(g,{label:"\u7528\u6237\u90AE\u7BB1",align:"center",key:"email",prop:"email","show-overflow-tooltip":!0}),l(g,{label:"\u7528\u6237\u59D3\u540D",align:"center",key:"name",prop:"name","show-overflow-tooltip":!0}),l(g,{label:"\u90E8\u95E8",align:"center",key:"deptName",prop:"dept.deptName","show-overflow-tooltip":!0}),l(g,{label:"\u89D2\u8272"},{default:e(a=>[(d(!0),N(F,null,j(a.row.roleIds,C=>(d(),u(A,{style:{margin:"0 2px"}},{default:e(()=>[_(Z(se(C)),1)]),_:2},1024))),256))]),_:1}),l(g,{label:"\u5C97\u4F4D"},{default:e(a=>[(d(!0),N(F,null,j(a.row.postIds,C=>(d(),u(A,{style:{margin:"0 2px"}},{default:e(()=>[_(Z(de(C)),1)]),_:2},1024))),256))]),_:1}),l(g,{label:"\u624B\u673A\u53F7\u7801",align:"center",key:"phone",prop:"phone"}),l(g,{label:"\u64CD\u4F5C",align:"center",width:"150","class-name":"small-padding fixed-width"},{default:e(a=>[a.row._id!==a.row.enterprise_id?(d(),u(M,{key:0,content:"\u4FEE\u6539",placement:"top"},{default:e(()=>[w((d(),u(f,{link:"",icon:"Edit",onClick:C=>ue(a.row)},{default:e(()=>[cl]),_:2},1032,["onClick"])),[[V,"1003"]])]),_:2},1024)):T("",!0),a.row._id!==a.row.enterprise_id?(d(),u(M,{key:1,content:"\u5220\u9664",placement:"top"},{default:e(()=>[w((d(),u(f,{link:"",type:"danger",icon:"Delete",onClick:C=>re(a.row)},{default:e(()=>[_l]),_:2},1032,["onClick"])),[[V,"1004"]])]),_:2},1024)):T("",!0)]),_:1})]),_:1},8,["data"])),[[V,"1001"],[ye,q.value]])]),_:1})]),_:1}),l(J,{title:x.value,modelValue:m.value,"onUpdate:modelValue":t[9]||(t[9]=a=>m.value=a),width:"600px","append-to-body":""},{footer:e(()=>[b("div",ml,[l(f,{type:"primary",onClick:_e},{default:e(()=>[fl]),_:1}),l(f,{onClick:ie},{default:e(()=>[vl]),_:1})])]),default:e(()=>[l(ge,{model:n(s),rules:n(ae),ref:"userRef","label-width":"80px"},{default:e(()=>[l(k,null,{default:e(()=>[l(i,{span:12},{default:e(()=>[l(h,{label:"\u90AE\u7BB1",prop:"email"},{default:e(()=>[l(r,{disabled:v.value===2,modelValue:n(s).email,"onUpdate:modelValue":t[1]||(t[1]=a=>n(s).email=a),placeholder:"\u8BF7\u8F93\u5165\u90AE\u7BB1",maxlength:"50"},null,8,["disabled","modelValue"])]),_:1})]),_:1}),l(i,{span:12},{default:e(()=>[l(h,{label:"\u5F52\u5C5E\u90E8\u95E8",prop:"deptId"},{default:e(()=>[l(ve,{modelValue:n(s).deptId,"onUpdate:modelValue":t[2]||(t[2]=a=>n(s).deptId=a),data:U.value,props:{value:"id",label:"label",children:"children"},"value-key":"id","default-expand-all":"",placeholder:"\u8BF7\u9009\u62E9\u5F52\u5C5E\u90E8\u95E8","check-strictly":""},null,8,["modelValue","data"])]),_:1})]),_:1})]),_:1}),v.value!==1?(d(),u(k,{key:0},{default:e(()=>[l(i,{span:12},{default:e(()=>[l(h,{label:"\u624B\u673A\u53F7\u7801",prop:"phone"},{default:e(()=>[l(r,{modelValue:n(s).phone,"onUpdate:modelValue":t[3]||(t[3]=a=>n(s).phone=a),placeholder:"\u8BF7\u8F93\u5165\u624B\u673A\u53F7\u7801",maxlength:"11"},null,8,["modelValue"])]),_:1})]),_:1}),l(i,{span:12},{default:e(()=>[l(h,{label:"\u7528\u6237\u6635\u79F0",prop:"nick_name"},{default:e(()=>[l(r,{modelValue:n(s).nick_name,"onUpdate:modelValue":t[4]||(t[4]=a=>n(s).nick_name=a),placeholder:"\u8BF7\u8F93\u5165\u7528\u6237\u6635\u79F0",maxlength:"30"},null,8,["modelValue"])]),_:1})]),_:1})]),_:1})):T("",!0),v.value!==1?(d(),u(k,{key:1},{default:e(()=>[l(i,{span:12},{default:e(()=>[l(h,{label:"\u7528\u6237\u540D\u79F0",prop:"name"},{default:e(()=>[l(r,{modelValue:n(s).name,"onUpdate:modelValue":t[5]||(t[5]=a=>n(s).name=a),placeholder:"\u8BF7\u8F93\u5165\u7528\u6237\u540D\u79F0",maxlength:"30"},null,8,["modelValue"])]),_:1})]),_:1}),l(i,{span:12},{default:e(()=>[v.value!==2?(d(),u(h,{key:0,label:"\u7528\u6237\u5BC6\u7801",prop:"password"},{default:e(()=>[l(r,{modelValue:n(s).password,"onUpdate:modelValue":t[6]||(t[6]=a=>n(s).password=a),placeholder:"\u8BF7\u8F93\u5165\u7528\u6237\u5BC6\u7801",type:"password",maxlength:"20","show-password":""},null,8,["modelValue"])]),_:1})):T("",!0)]),_:1})]),_:1})):T("",!0),l(k,null,{default:e(()=>[l(i,{span:12},{default:e(()=>[l(h,{label:"\u5C97\u4F4D"},{default:e(()=>[l(Q,{modelValue:n(s).postIds,"onUpdate:modelValue":t[7]||(t[7]=a=>n(s).postIds=a),multiple:"",placeholder:"\u8BF7\u9009\u62E9"},{default:e(()=>[(d(!0),N(F,null,j(B.value,a=>(d(),u(z,{key:a._id,label:a.postName,value:a._id},null,8,["label","value"]))),128))]),_:1},8,["modelValue"])]),_:1})]),_:1}),l(i,{span:12},{default:e(()=>[l(h,{label:"\u89D2\u8272"},{default:e(()=>[l(Q,{modelValue:n(s).roleIds,"onUpdate:modelValue":t[8]||(t[8]=a=>n(s).roleIds=a),multiple:"",placeholder:"\u8BF7\u9009\u62E9"},{default:e(()=>[(d(!0),N(F,null,j(S.value,a=>(d(),u(z,{key:a._id,label:a.roleName,value:a._id},null,8,["label","value"]))),128))]),_:1},8,["modelValue"])]),_:1})]),_:1})]),_:1})]),_:1},8,["model","rules"])]),_:1},8,["title","modelValue"]),l(J,{title:n(c).title,modelValue:n(c).open,"onUpdate:modelValue":t[11]||(t[11]=a=>n(c).open=a),width:"400px","append-to-body":""},{footer:e(()=>[b("div",bl,[l(f,{type:"primary",onClick:ee},{default:e(()=>[xl]),_:1}),l(f,{onClick:t[10]||(t[10]=a=>n(c).open=!1)},{default:e(()=>[yl]),_:1})])]),default:e(()=>[l(xe,{ref:"uploadRef",limit:1,accept:".xlsx, .xls",headers:n(c).headers,action:n(c).url,disabled:n(c).isUploading,"on-progress":X,"on-success":le,"auto-upload":!1,drag:""},{tip:e(()=>[hl]),default:e(()=>[l(be,{class:"el-icon--upload"},{default:e(()=>[l(he)]),_:1}),gl]),_:1},8,["headers","action","disabled"])]),_:1},8,["title","modelValue"])])}}};var Nl=He(kl,[["__scopeId","data-v-9813b2b4"]]);export{Nl as default};
