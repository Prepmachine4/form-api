import{u as ye,r as u,t as ge,aO as Ce,s as Ve,ac as Se,ad as xe,a1 as Ee,ak as we,a2 as Ne,D as Ke,G as Re,e as Te,J as Ue,aS as Ie,aT as De,aP as Be,I as Le,L as Me,ah as je,ai as qe,au as Ae,aL as Fe,f as Z,j as t,k as a,w as g,l as v,o as c,g as N,C as Oe,m as z,h as d,F as Pe,B as $e,aw as Ge,q as r,Z as He,E as K,_ as Q,aR as Je}from"./vendor.3bf6c43c.js";/* empty css                   *//* empty css                *//* empty css                        */import{l as Ze,d as ze,g as W,u as Qe,a as We,b as Xe}from"./role.c07df151.js";import{_ as Ye}from"./index.3091a82d.js";function X(){let j=[{id:"0",label:"\u8868\u5355\u7BA1\u7406",children:[{id:"000",label:"\u67E5\u8BE2\u8868\u5355"},{id:"001",label:"\u67E5\u8BE2\u8868\u5355\u6570\u636E"},{id:"002",label:"\u521B\u5EFA\u95EE\u5377\u578B\u8868\u5355"},{id:"003",label:"\u521B\u5EFA\u4E1A\u52A1\u578B\u8868\u5355"},{id:"004",label:"\u4FEE\u6539\u8868\u5355"},{id:"005",label:"\u5220\u9664\u8868\u5355"}]},{id:"1",label:"\u4F01\u4E1A\u7BA1\u7406",children:[{id:"100",label:"\u7528\u6237\u7BA1\u7406",children:[{id:"1001",label:"\u7528\u6237\u67E5\u8BE2"},{id:"1002",label:"\u7528\u6237\u65B0\u589E"},{id:"1003",label:"\u7528\u6237\u4FEE\u6539"},{id:"1004",label:"\u7528\u6237\u5220\u9664"}]},{id:"101",label:"\u89D2\u8272\u7BA1\u7406",children:[{id:"1008",label:"\u89D2\u8272\u67E5\u8BE2"},{id:"1009",label:"\u89D2\u8272\u65B0\u589E"},{id:"1010",label:"\u89D2\u8272\u4FEE\u6539"},{id:"1011",label:"\u89D2\u8272\u5220\u9664"}]},{id:"102",label:"\u90E8\u95E8\u7BA1\u7406",children:[{id:"1017",label:"\u90E8\u95E8\u67E5\u8BE2"},{id:"1018",label:"\u90E8\u95E8\u65B0\u589E"},{id:"1019",label:"\u90E8\u95E8\u4FEE\u6539"},{id:"1020",label:"\u90E8\u95E8\u5220\u9664"}]},{id:"103",label:"\u5C97\u4F4D\u7BA1\u7406",children:[{id:"1021",label:"\u5C97\u4F4D\u67E5\u8BE2"},{id:"1022",label:"\u5C97\u4F4D\u65B0\u589E"},{id:"1023",label:"\u5C97\u4F4D\u4FEE\u6539"},{id:"1024",label:"\u5C97\u4F4D\u5220\u9664"}]}]},{id:"2",label:"\u6D41\u7A0B\u7BA1\u7406",children:[{id:"200",label:"\u67E5\u8BE2\u6D41\u7A0B"},{id:"201",label:"\u6DFB\u52A0\u6D41\u7A0B"},{id:"202",label:"\u5220\u9664\u6D41\u7A0B"},{id:"203",label:"\u7EC8\u6B62\u6D41\u7A0B"}]}];return new Promise(R=>R(j))}const el={class:"app-container"},ll=r("\u65B0\u589E "),tl=r("\u4FEE\u6539"),al=r("\u5220\u9664"),ol=r(" \u6743\u9650\u5B57\u7B26 "),nl=r("\u5C55\u5F00/\u6298\u53E0"),dl=r("\u5168\u9009/\u5168\u4E0D\u9009"),ul=r("\u7236\u5B50\u8054\u52A8 "),sl={class:"dialog-footer"},rl=r("\u786E \u5B9A"),il=r("\u53D6 \u6D88"),cl=r("\u5C55\u5F00/\u6298\u53E0"),pl=r("\u5168\u9009/\u5168\u4E0D\u9009"),ml=r("\u7236\u5B50\u8054\u52A8 "),fl={class:"dialog-footer"},_l=r("\u786E \u5B9A"),vl=r("\u53D6 \u6D88"),bl={setup(j){ye();const{proxy:R}=Je(),q=u([]),f=u(!1),T=u(!0);u(!0);const A=u([]);u(!0),u(!0),u(0);const C=u("");u([]);const h=u(),U=u(!1),I=u(!1),D=u(!0),B=u(!1),L=u([]),V=u(!1),p=u(null),S=u(null),Y=u([{value:"1",label:"\u5168\u90E8\u6570\u636E\u6743\u9650"},{value:"4",label:"\u672C\u90E8\u95E8\u53CA\u4EE5\u4E0B\u6570\u636E\u6743\u9650"},{value:"5",label:"\u4EC5\u672C\u4EBA\u6570\u636E\u6743\u9650"}]),ee=ge({form:{},rules:{roleName:[{required:!0,message:"\u89D2\u8272\u540D\u79F0\u4E0D\u80FD\u4E3A\u7A7A",trigger:"blur"}],roleKey:[{required:!0,message:"\u6743\u9650\u5B57\u7B26\u4E0D\u80FD\u4E3A\u7A7A",trigger:"blur"}],roleSort:[{required:!0,message:"\u89D2\u8272\u987A\u5E8F\u4E0D\u80FD\u4E3A\u7A7A",trigger:"blur"}]}}),{form:o,rules:le}=Ce(ee);function k(){T.value=!0,Ze().then(n=>{q.value=n.data,T.value=!1})}function te(n){const e=n._id||A.value;He.confirm('\u662F\u5426\u786E\u8BA4\u5220\u9664\u89D2\u8272\u540D\u79F0\u4E3A"'+n.roleName+'"\u7684\u6570\u636E\u9879?',{confirmButtonText:"\u786E\u5B9A",cancelButtonText:"\u53D6\u6D88",type:"warning"}).then(function(){return ze(e)}).then(()=>{k(),K.success("\u5220\u9664\u6210\u529F")}).catch(()=>{})}function ae(){X().then(n=>{h.value=n})}function x(){p.value!=null&&p.value.setCheckedKeys([]),U.value=!1,I.value=!1,D.value=!0,B.value=!1,o.value={_id:void 0,roleName:void 0,roleKey:void 0,roleSort:0,menuIds:[],dataScope:void 0,menuCheckStrictly:!0,deptCheckStrictly:!0}}function oe(){x(),ae(),f.value=!0,C.value="\u6DFB\u52A0\u89D2\u8272"}function ne(n){x();const e=n._id||A.value,s=de(e);W(e).then(i=>{o.value=i.data,o.value.roleSort=Number(o.value.roleSort),f.value=!0,Q(()=>{s.then(M=>{M.data.menuIds.forEach(y=>{Q(()=>{p.value.setChecked(y,!0,!1)})})})}),C.value="\u4FEE\u6539\u89D2\u8272"})}function de(n){return X().then(e=>(h.value=e,W(n)))}function F(n,e){if(e=="menu"){let s=h.value;for(let i=0;i<s.length;i++)p.value.store.nodesMap[s[i].id].expanded=n}else if(e=="dept"){let s=L.value;for(let i=0;i<s.length;i++)S.value.store.nodesMap[s[i].id].expanded=n}}function O(n,e){e=="menu"?p.value.setCheckedNodes(n?h.value:[]):e=="dept"&&S.value.setCheckedNodes(n?L.value:[])}function P(n,e){e=="menu"?o.value.menuCheckStrictly=!!n:e=="dept"&&(o.value.deptCheckStrictly=!!n)}function $(){let n=p.value.getCheckedKeys(),e=p.value.getHalfCheckedKeys();return n.unshift.apply(n,e),n}function ue(){R.$refs.roleRef.validate(n=>{n&&(o.value._id!=null?(o.value.menuIds=$(),Qe(o.value).then(e=>{K.success("\u4FEE\u6539\u6210\u529F"),f.value=!1,k()})):(o.value.menuIds=$(),We(o.value).then(e=>{K.success("\u65B0\u589E\u6210\u529F"),f.value=!1,k()})))})}function se(){f.value=!1,x()}function re(n){n!=="2"&&S.value.setCheckedKeys([])}function ie(){o.value._id!=null&&Xe(o.value).then(n=>{K.success("\u4FEE\u6539\u6210\u529F"),V.value=!1,k()})}function ce(){V.value=!1,x()}return k(),(n,e)=>{const s=Ve,i=Se,M=xe,_=Ee,y=we,pe=Ne,E=Ke,m=Re,me=Te("question-filled"),fe=Ue,_e=Ie,b=De,G=Be,H=Le,J=Me,ve=je,be=qe,w=Ae("hasPermi"),he=Fe;return c(),Z("div",el,[t(M,{gutter:10,class:"mb8"},{default:a(()=>[t(i,{span:1.5},{default:a(()=>[g((c(),v(s,{type:"primary",plain:"",icon:"Plus",onClick:oe},{default:a(()=>[ll]),_:1})),[[w,"1009"]])]),_:1},8,["span"])]),_:1}),g((c(),v(pe,{data:q.value},{default:a(()=>[t(_,{type:"index"}),t(_,{label:"\u89D2\u8272\u540D\u79F0",prop:"roleName","show-overflow-tooltip":!0}),t(_,{label:"\u6743\u9650\u5B57\u7B26",prop:"roleKey","show-overflow-tooltip":!0}),t(_,{label:"\u663E\u793A\u987A\u5E8F",prop:"roleSort"}),t(_,{label:"\u521B\u5EFA\u65F6\u95F4",align:"center",prop:"createTime"},{default:a(l=>[N("span",null,Oe(l.row.createTime),1)]),_:1}),t(_,{label:"\u64CD\u4F5C",align:"center","class-name":"small-padding fixed-width"},{default:a(l=>[l.row.admin?z("",!0):(c(),v(y,{key:0,content:"\u4FEE\u6539",placement:"top"},{default:a(()=>[g((c(),v(s,{link:"",icon:"Edit",onClick:ke=>ne(l.row)},{default:a(()=>[tl]),_:2},1032,["onClick"])),[[w,"1010"]])]),_:2},1024)),l.row.admin?z("",!0):(c(),v(y,{key:1,content:"\u5220\u9664",placement:"top"},{default:a(()=>[g((c(),v(s,{link:"",type:"danger",icon:"Delete",onClick:ke=>te(l.row)},{default:a(()=>[al]),_:2},1032,["onClick"])),[[w,"1011"]])]),_:2},1024))]),_:1})]),_:1},8,["data"])),[[w,"1008"],[he,T.value]]),t(J,{title:C.value,modelValue:f.value,"onUpdate:modelValue":e[9]||(e[9]=l=>f.value=l),width:"500px","append-to-body":""},{footer:a(()=>[N("div",sl,[t(s,{type:"primary",onClick:ue},{default:a(()=>[rl]),_:1}),t(s,{onClick:se},{default:a(()=>[il]),_:1})])]),default:a(()=>[t(H,{ref:"roleRef",model:d(o),rules:d(le),"label-width":"100px"},{default:a(()=>[t(m,{label:"\u89D2\u8272\u540D\u79F0",prop:"roleName"},{default:a(()=>[t(E,{modelValue:d(o).roleName,"onUpdate:modelValue":e[0]||(e[0]=l=>d(o).roleName=l),placeholder:"\u8BF7\u8F93\u5165\u89D2\u8272\u540D\u79F0"},null,8,["modelValue"])]),_:1}),t(m,{prop:"roleKey"},{label:a(()=>[N("span",null,[t(y,{content:"\u5982\uFF1Aadmin common",placement:"top"},{default:a(()=>[t(fe,null,{default:a(()=>[t(me)]),_:1})]),_:1}),ol])]),default:a(()=>[t(E,{modelValue:d(o).roleKey,"onUpdate:modelValue":e[1]||(e[1]=l=>d(o).roleKey=l),placeholder:"\u8BF7\u8F93\u5165\u6743\u9650\u5B57\u7B26"},null,8,["modelValue"])]),_:1}),t(m,{label:"\u89D2\u8272\u987A\u5E8F",prop:"roleSort"},{default:a(()=>[t(_e,{modelValue:d(o).roleSort,"onUpdate:modelValue":e[2]||(e[2]=l=>d(o).roleSort=l),"controls-position":"right",min:0},null,8,["modelValue"])]),_:1}),t(m,{label:"\u83DC\u5355\u6743\u9650"},{default:a(()=>[t(b,{modelValue:U.value,"onUpdate:modelValue":e[3]||(e[3]=l=>U.value=l),onChange:e[4]||(e[4]=l=>F(l,"menu"))},{default:a(()=>[nl]),_:1},8,["modelValue"]),t(b,{modelValue:I.value,"onUpdate:modelValue":e[5]||(e[5]=l=>I.value=l),onChange:e[6]||(e[6]=l=>O(l,"menu"))},{default:a(()=>[dl]),_:1},8,["modelValue"]),t(b,{modelValue:d(o).menuCheckStrictly,"onUpdate:modelValue":e[7]||(e[7]=l=>d(o).menuCheckStrictly=l),onChange:e[8]||(e[8]=l=>P(l,"menu"))},{default:a(()=>[ul]),_:1},8,["modelValue"]),t(G,{class:"tree-border",data:h.value,"show-checkbox":"",ref_key:"menuRef",ref:p,"node-key":"id","check-strictly":!d(o).menuCheckStrictly,"empty-text":"\u52A0\u8F7D\u4E2D\uFF0C\u8BF7\u7A0D\u5019",props:{label:"label",children:"children"}},null,8,["data","check-strictly"])]),_:1})]),_:1},8,["model","rules"])]),_:1},8,["title","modelValue"]),t(J,{title:C.value,modelValue:V.value,"onUpdate:modelValue":e[19]||(e[19]=l=>V.value=l),width:"500px","append-to-body":""},{footer:a(()=>[N("div",fl,[t(s,{type:"primary",onClick:ie},{default:a(()=>[_l]),_:1}),t(s,{onClick:ce},{default:a(()=>[vl]),_:1})])]),default:a(()=>[t(H,{model:d(o),"label-width":"80px"},{default:a(()=>[t(m,{label:"\u89D2\u8272\u540D\u79F0"},{default:a(()=>[t(E,{modelValue:d(o).roleName,"onUpdate:modelValue":e[10]||(e[10]=l=>d(o).roleName=l),disabled:!0},null,8,["modelValue"])]),_:1}),t(m,{label:"\u6743\u9650\u5B57\u7B26"},{default:a(()=>[t(E,{modelValue:d(o).roleKey,"onUpdate:modelValue":e[11]||(e[11]=l=>d(o).roleKey=l),disabled:!0},null,8,["modelValue"])]),_:1}),t(m,{label:"\u6743\u9650\u8303\u56F4"},{default:a(()=>[t(be,{modelValue:d(o).dataScope,"onUpdate:modelValue":e[12]||(e[12]=l=>d(o).dataScope=l),onChange:re},{default:a(()=>[(c(!0),Z(Pe,null,$e(Y.value,l=>(c(),v(ve,{key:l.value,label:l.label,value:l.value},null,8,["label","value"]))),128))]),_:1},8,["modelValue"])]),_:1}),g(t(m,{label:"\u6570\u636E\u6743\u9650"},{default:a(()=>[t(b,{modelValue:D.value,"onUpdate:modelValue":e[13]||(e[13]=l=>D.value=l),onChange:e[14]||(e[14]=l=>F(l,"dept"))},{default:a(()=>[cl]),_:1},8,["modelValue"]),t(b,{modelValue:B.value,"onUpdate:modelValue":e[15]||(e[15]=l=>B.value=l),onChange:e[16]||(e[16]=l=>O(l,"dept"))},{default:a(()=>[pl]),_:1},8,["modelValue"]),t(b,{modelValue:d(o).deptCheckStrictly,"onUpdate:modelValue":e[17]||(e[17]=l=>d(o).deptCheckStrictly=l),onChange:e[18]||(e[18]=l=>P(l,"dept"))},{default:a(()=>[ml]),_:1},8,["modelValue"]),t(G,{class:"tree-border",data:L.value,"show-checkbox":"","default-expand-all":"",ref_key:"deptRef",ref:S,"node-key":"id","check-strictly":!d(o).deptCheckStrictly,"empty-text":"\u52A0\u8F7D\u4E2D\uFF0C\u8BF7\u7A0D\u5019",props:{label:"label",children:"children"}},null,8,["data","check-strictly"])]),_:1},512),[[Ge,d(o).dataScope==2]])]),_:1},8,["model"])]),_:1},8,["title","modelValue"])])}}};var Sl=Ye(bl,[["__scopeId","data-v-3b65defc"]]);export{Sl as default};
