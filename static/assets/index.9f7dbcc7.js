import{_ as Ce,u as ge,r as u,q as Ve,aG as xe,n as Se,a5 as we,a7 as Ee,W as Ne,ae as Ke,X as Re,A as Ue,B as Te,e as Ie,O as De,aM as Be,aN as Me,aH as Le,C as qe,as as Ae,ab as je,ac as Oe,aJ as Fe,aD as Pe,f as X,j as t,k as a,w as M,y as h,o as m,g as w,N as $e,z as L,h as d,U as He,V as ze,an as Ge,m as r,aK as Je,E,R as Q,aL as We}from"./vendor.3587a8c4.js";/* empty css                   */import{l as Xe,d as Qe,g as q,u as Ye,a as Ze,b as el}from"./role.b9a765ba.js";/* empty css                        */function Y(){let A=[{id:"0",label:"\u8868\u5355\u7BA1\u7406",children:[]},{id:"1",label:"\u4F01\u4E1A\u7BA1\u7406",children:[{id:"100",label:"\u7528\u6237\u7BA1\u7406",children:[{id:"1001",label:"\u7528\u6237\u67E5\u8BE2"},{id:"1002",label:"\u7528\u6237\u65B0\u589E"},{id:"1003",label:"\u7528\u6237\u4FEE\u6539"},{id:"1004",label:"\u7528\u6237\u5220\u9664"}]},{id:"101",label:"\u89D2\u8272\u7BA1\u7406",children:[{id:"1008",label:"\u89D2\u8272\u67E5\u8BE2"},{id:"1009",label:"\u89D2\u8272\u65B0\u589E"},{id:"1010",label:"\u89D2\u8272\u4FEE\u6539"},{id:"1011",label:"\u89D2\u8272\u5220\u9664"}]},{id:"102",label:"\u90E8\u95E8\u7BA1\u7406",children:[{id:"1017",label:"\u90E8\u95E8\u67E5\u8BE2"},{id:"1018",label:"\u90E8\u95E8\u65B0\u589E"},{id:"1019",label:"\u90E8\u95E8\u4FEE\u6539"},{id:"1020",label:"\u90E8\u95E8\u5220\u9664"}]},{id:"103",label:"\u5C97\u4F4D\u7BA1\u7406",children:[{id:"1021",label:"\u5C97\u4F4D\u67E5\u8BE2"},{id:"1022",label:"\u5C97\u4F4D\u65B0\u589E"},{id:"1023",label:"\u5C97\u4F4D\u4FEE\u6539"},{id:"1024",label:"\u5C97\u4F4D\u5220\u9664"}]}]},{id:"2",label:"\u6D41\u7A0B\u7BA1\u7406",children:[]},{id:"3",label:"\u4EFB\u52A1\u7BA1\u7406",children:[]}];return new Promise(N=>N(A))}const ll={class:"app-container"},tl=r("\u65B0\u589E "),al=r(" \u6743\u9650\u5B57\u7B26 "),ol=r("\u5C55\u5F00/\u6298\u53E0"),nl=r("\u5168\u9009/\u5168\u4E0D\u9009"),dl=r("\u7236\u5B50\u8054\u52A8 "),ul={class:"dialog-footer"},sl=r("\u786E \u5B9A"),rl=r("\u53D6 \u6D88"),il=r("\u5C55\u5F00/\u6298\u53E0"),cl=r("\u5168\u9009/\u5168\u4E0D\u9009"),pl=r("\u7236\u5B50\u8054\u52A8 "),ml={class:"dialog-footer"},fl=r("\u786E \u5B9A"),_l=r("\u53D6 \u6D88"),vl={setup(A){ge();const{proxy:N}=We(),j=u([]),f=u(!1),K=u(!0);u(!0);const O=u([]);u(!0),u(!0),u(0);const k=u("");u([]);const y=u(),R=u(!1),U=u(!1),T=u(!0),I=u(!1),D=u([]),C=u(!1),c=u(null),x=u(null),Z=u([{value:"1",label:"\u5168\u90E8\u6570\u636E\u6743\u9650"},{value:"4",label:"\u672C\u90E8\u95E8\u53CA\u4EE5\u4E0B\u6570\u636E\u6743\u9650"},{value:"5",label:"\u4EC5\u672C\u4EBA\u6570\u636E\u6743\u9650"}]),ee=Ve({form:{},rules:{roleName:[{required:!0,message:"\u89D2\u8272\u540D\u79F0\u4E0D\u80FD\u4E3A\u7A7A",trigger:"blur"}],roleKey:[{required:!0,message:"\u6743\u9650\u5B57\u7B26\u4E0D\u80FD\u4E3A\u7A7A",trigger:"blur"}],roleSort:[{required:!0,message:"\u89D2\u8272\u987A\u5E8F\u4E0D\u80FD\u4E3A\u7A7A",trigger:"blur"}]}}),{form:o,rules:le}=xe(ee);function g(){K.value=!0,Xe().then(n=>{j.value=n.data,K.value=!1})}function te(n){const e=n._id||O.value;Je.confirm('\u662F\u5426\u786E\u8BA4\u5220\u9664\u89D2\u8272\u540D\u79F0\u4E3A"'+n.roleName+'"\u7684\u6570\u636E\u9879?',{confirmButtonText:"\u786E\u5B9A",cancelButtonText:"\u53D6\u6D88",type:"warning"}).then(function(){return Qe(e)}).then(()=>{g(),E.success("\u5220\u9664\u6210\u529F")}).catch(()=>{})}function ae(){Y().then(n=>{y.value=n})}function V(){c.value!=null&&c.value.setCheckedKeys([]),R.value=!1,U.value=!1,T.value=!0,I.value=!1,o.value={_id:void 0,roleName:void 0,roleKey:void 0,roleSort:0,menuIds:[],dataScope:void 0,menuCheckStrictly:!0,deptCheckStrictly:!0}}function oe(){V(),ae(),f.value=!0,k.value="\u6DFB\u52A0\u89D2\u8272"}function ne(n){V();const e=n._id||O.value,s=de(e);q(e).then(i=>{o.value=i.data,o.value.roleSort=Number(o.value.roleSort),f.value=!0,Q(()=>{s.then(B=>{B.data.menuIds.forEach(v=>{Q(()=>{c.value.setChecked(v,!0,!1)})})})}),k.value="\u4FEE\u6539\u89D2\u8272"})}function de(n){return Y().then(e=>(y.value=e,q(n)))}function F(n,e){if(e=="menu"){let s=y.value;for(let i=0;i<s.length;i++)c.value.store.nodesMap[s[i].id].expanded=n}else if(e=="dept"){let s=D.value;for(let i=0;i<s.length;i++)x.value.store.nodesMap[s[i].id].expanded=n}}function P(n,e){e=="menu"?c.value.setCheckedNodes(n?y.value:[]):e=="dept"&&x.value.setCheckedNodes(n?D.value:[])}function $(n,e){e=="menu"?o.value.menuCheckStrictly=!!n:e=="dept"&&(o.value.deptCheckStrictly=!!n)}function H(){let n=c.value.getCheckedKeys(),e=c.value.getHalfCheckedKeys();return n.unshift.apply(n,e),n}function ue(){N.$refs.roleRef.validate(n=>{n&&(o.value._id!=null?(o.value.menuIds=H(),Ye(o.value).then(e=>{E.success("\u4FEE\u6539\u6210\u529F"),f.value=!1,g()})):(o.value.menuIds=H(),Ze(o.value).then(e=>{E.success("\u65B0\u589E\u6210\u529F"),f.value=!1,g()})))})}function se(){f.value=!1,V()}function re(n){n!=="2"&&x.value.setCheckedKeys([])}function ie(n){V(),q(n._id).then(e=>{o.value=e.data,C.value=!0,k.value="\u5206\u914D\u6570\u636E\u6743\u9650"})}function ce(){o.value._id!=null&&el(o.value).then(n=>{E.success("\u4FEE\u6539\u6210\u529F"),C.value=!1,g()})}function pe(){C.value=!1,V()}return g(),(n,e)=>{const s=Se,i=we,B=Ee,_=Ne,v=Ke,me=Re,S=Ue,p=Te,fe=Ie("question-filled"),_e=De,ve=Be,b=Me,z=Le,G=qe,J=Ae,be=je,he=Oe,ke=Fe("hasPermi"),ye=Pe;return m(),X("div",ll,[t(B,{gutter:10,class:"mb8"},{default:a(()=>[t(i,{span:1.5},{default:a(()=>[M((m(),h(s,{type:"primary",plain:"",icon:"Plus",onClick:oe},{default:a(()=>[tl]),_:1})),[[ke,["system:role:add"]]])]),_:1},8,["span"])]),_:1}),M((m(),h(me,{data:j.value},{default:a(()=>[t(_,{type:"index"}),t(_,{label:"\u89D2\u8272\u540D\u79F0",prop:"roleName","show-overflow-tooltip":!0}),t(_,{label:"\u6743\u9650\u5B57\u7B26",prop:"roleKey","show-overflow-tooltip":!0}),t(_,{label:"\u663E\u793A\u987A\u5E8F",prop:"roleSort"}),t(_,{label:"\u521B\u5EFA\u65F6\u95F4",align:"center",prop:"createTime"},{default:a(l=>[w("span",null,$e(l.row.createTime),1)]),_:1}),t(_,{label:"\u64CD\u4F5C",align:"center","class-name":"small-padding fixed-width"},{default:a(l=>[l.row.admin?L("",!0):(m(),h(v,{key:0,content:"\u4FEE\u6539",placement:"top"},{default:a(()=>[t(s,{type:"text",icon:"Edit",onClick:W=>ne(l.row)},null,8,["onClick"])]),_:2},1024)),l.row.admin?L("",!0):(m(),h(v,{key:1,content:"\u6570\u636E\u6743\u9650",placement:"top"},{default:a(()=>[t(s,{type:"text",icon:"CircleCheck",onClick:W=>ie(l.row)},null,8,["onClick"])]),_:2},1024)),l.row.admin?L("",!0):(m(),h(v,{key:2,content:"\u5220\u9664",placement:"top"},{default:a(()=>[t(s,{type:"text",icon:"Delete",onClick:W=>te(l.row)},null,8,["onClick"])]),_:2},1024))]),_:1})]),_:1},8,["data"])),[[ye,K.value]]),t(J,{title:k.value,modelValue:f.value,"onUpdate:modelValue":e[9]||(e[9]=l=>f.value=l),width:"500px","append-to-body":""},{footer:a(()=>[w("div",ul,[t(s,{type:"primary",onClick:ue},{default:a(()=>[sl]),_:1}),t(s,{onClick:se},{default:a(()=>[rl]),_:1})])]),default:a(()=>[t(G,{ref:"roleRef",model:d(o),rules:d(le),"label-width":"100px"},{default:a(()=>[t(p,{label:"\u89D2\u8272\u540D\u79F0",prop:"roleName"},{default:a(()=>[t(S,{modelValue:d(o).roleName,"onUpdate:modelValue":e[0]||(e[0]=l=>d(o).roleName=l),placeholder:"\u8BF7\u8F93\u5165\u89D2\u8272\u540D\u79F0"},null,8,["modelValue"])]),_:1}),t(p,{prop:"roleKey"},{label:a(()=>[w("span",null,[t(v,{content:"\u5982\uFF1Aadmin common",placement:"top"},{default:a(()=>[t(_e,null,{default:a(()=>[t(fe)]),_:1})]),_:1}),al])]),default:a(()=>[t(S,{modelValue:d(o).roleKey,"onUpdate:modelValue":e[1]||(e[1]=l=>d(o).roleKey=l),placeholder:"\u8BF7\u8F93\u5165\u6743\u9650\u5B57\u7B26"},null,8,["modelValue"])]),_:1}),t(p,{label:"\u89D2\u8272\u987A\u5E8F",prop:"roleSort"},{default:a(()=>[t(ve,{modelValue:d(o).roleSort,"onUpdate:modelValue":e[2]||(e[2]=l=>d(o).roleSort=l),"controls-position":"right",min:0},null,8,["modelValue"])]),_:1}),t(p,{label:"\u83DC\u5355\u6743\u9650"},{default:a(()=>[t(b,{modelValue:R.value,"onUpdate:modelValue":e[3]||(e[3]=l=>R.value=l),onChange:e[4]||(e[4]=l=>F(l,"menu"))},{default:a(()=>[ol]),_:1},8,["modelValue"]),t(b,{modelValue:U.value,"onUpdate:modelValue":e[5]||(e[5]=l=>U.value=l),onChange:e[6]||(e[6]=l=>P(l,"menu"))},{default:a(()=>[nl]),_:1},8,["modelValue"]),t(b,{modelValue:d(o).menuCheckStrictly,"onUpdate:modelValue":e[7]||(e[7]=l=>d(o).menuCheckStrictly=l),onChange:e[8]||(e[8]=l=>$(l,"menu"))},{default:a(()=>[dl]),_:1},8,["modelValue"]),t(z,{class:"tree-border",data:y.value,"show-checkbox":"",ref_key:"menuRef",ref:c,"node-key":"id","check-strictly":!d(o).menuCheckStrictly,"empty-text":"\u52A0\u8F7D\u4E2D\uFF0C\u8BF7\u7A0D\u5019",props:{label:"label",children:"children"}},null,8,["data","check-strictly"])]),_:1})]),_:1},8,["model","rules"])]),_:1},8,["title","modelValue"]),t(J,{title:k.value,modelValue:C.value,"onUpdate:modelValue":e[19]||(e[19]=l=>C.value=l),width:"500px","append-to-body":""},{footer:a(()=>[w("div",ml,[t(s,{type:"primary",onClick:ce},{default:a(()=>[fl]),_:1}),t(s,{onClick:pe},{default:a(()=>[_l]),_:1})])]),default:a(()=>[t(G,{model:d(o),"label-width":"80px"},{default:a(()=>[t(p,{label:"\u89D2\u8272\u540D\u79F0"},{default:a(()=>[t(S,{modelValue:d(o).roleName,"onUpdate:modelValue":e[10]||(e[10]=l=>d(o).roleName=l),disabled:!0},null,8,["modelValue"])]),_:1}),t(p,{label:"\u6743\u9650\u5B57\u7B26"},{default:a(()=>[t(S,{modelValue:d(o).roleKey,"onUpdate:modelValue":e[11]||(e[11]=l=>d(o).roleKey=l),disabled:!0},null,8,["modelValue"])]),_:1}),t(p,{label:"\u6743\u9650\u8303\u56F4"},{default:a(()=>[t(he,{modelValue:d(o).dataScope,"onUpdate:modelValue":e[12]||(e[12]=l=>d(o).dataScope=l),onChange:re},{default:a(()=>[(m(!0),X(He,null,ze(Z.value,l=>(m(),h(be,{key:l.value,label:l.label,value:l.value},null,8,["label","value"]))),128))]),_:1},8,["modelValue"])]),_:1}),M(t(p,{label:"\u6570\u636E\u6743\u9650"},{default:a(()=>[t(b,{modelValue:T.value,"onUpdate:modelValue":e[13]||(e[13]=l=>T.value=l),onChange:e[14]||(e[14]=l=>F(l,"dept"))},{default:a(()=>[il]),_:1},8,["modelValue"]),t(b,{modelValue:I.value,"onUpdate:modelValue":e[15]||(e[15]=l=>I.value=l),onChange:e[16]||(e[16]=l=>P(l,"dept"))},{default:a(()=>[cl]),_:1},8,["modelValue"]),t(b,{modelValue:d(o).deptCheckStrictly,"onUpdate:modelValue":e[17]||(e[17]=l=>d(o).deptCheckStrictly=l),onChange:e[18]||(e[18]=l=>$(l,"dept"))},{default:a(()=>[pl]),_:1},8,["modelValue"]),t(z,{class:"tree-border",data:D.value,"show-checkbox":"","default-expand-all":"",ref_key:"deptRef",ref:x,"node-key":"id","check-strictly":!d(o).deptCheckStrictly,"empty-text":"\u52A0\u8F7D\u4E2D\uFF0C\u8BF7\u7A0D\u5019",props:{label:"label",children:"children"}},null,8,["data","check-strictly"])]),_:1},512),[[Ge,d(o).dataScope==2]])]),_:1},8,["model"])]),_:1},8,["title","modelValue"])])}}};var Cl=Ce(vl,[["__scopeId","data-v-07243b6e"]]);export{Cl as default};