import{r as u,q as le,aI as ae,n as te,a6 as ne,a8 as oe,Y as de,a7 as re,Z as ue,A as se,B as ie,aN as pe,ac as _e,ad as ce,C as me,au as fe,an as ve,aF as ge,f as k,j as e,k as a,w as x,y as p,z as I,o as r,Q as w,X as T,m as _,R as A,g as L,h as d,aM as he,U as be,E as D,T as ke}from"./vendor.79e55f37.js";/* empty css                   *//* empty css                        */import{l as xe,g as Ne,u as Ve,a as Ee,d as ye}from"./dept.149aa4c9.js";import{_ as Ce,f as Ie}from"./index.e0f133fc.js";import{l as we}from"./role.68dea753.js";const Te={class:"app-container"},De=_("\u5C55\u5F00/\u6298\u53E0"),Be=_("\u4FEE\u6539"),Ue=_("\u65B0\u589E"),je=_("\u5220\u9664"),Re={class:"dialog-footer"},qe=_("\u786E \u5B9A"),Fe=_("\u53D6 \u6D88"),$e={setup(Ae){const B=u([]),s=u(!1),N=u(!0);u(!0);const V=u(""),v=u([]);u([]);const E=u(!0),y=u(!0),U=u([]),M=le({form:{},rules:{parentId:[{required:!0,message:"\u4E0A\u7EA7\u90E8\u95E8\u4E0D\u80FD\u4E3A\u7A7A",trigger:"blur"}],deptName:[{required:!0,message:"\u90E8\u95E8\u540D\u79F0\u4E0D\u80FD\u4E3A\u7A7A",trigger:"blur"}],orderNum:[{required:!0,message:"\u663E\u793A\u6392\u5E8F\u4E0D\u80FD\u4E3A\u7A7A",trigger:"blur"}],leader_id:[{required:!0,message:"\u8D1F\u8D23\u4EBA\u4E0D\u80FD\u4E3A\u7A7A",trigger:"blur"}],phone:[{required:!0,pattern:/^1[3|4|5|6|7|8|9][0-9]\d{8}$/,message:"\u8BF7\u8F93\u5165\u6B63\u786E\u7684\u624B\u673A\u53F7\u7801",trigger:"blur"}]}}),{proxy:j}=he(),{form:o,rules:O}=ae(M);function g(){N.value=!0,xe().then(n=>{B.value=j.handleTree(n.data,"_id"),N.value=!1})}function P(){s.value=!1,C()}function C(){o.value={_id:void 0,parentId:void 0,deptName:void 0,orderNum:0,leader_id:void 0,phone:void 0,roleIds:void 0}}const S=n=>{if(v.value.length!==0)return v.value.filter(t=>t._id===n)[0].roleName};function z(n){C(),n!=null&&(o.value.parentId=n._id),s.value=!0,V.value="\u6DFB\u52A0\u90E8\u95E8"}function Q(){y.value=!1,E.value=!E.value,be(()=>{y.value=!0})}function X(n){C(),Ne(n._id).then(t=>{o.value=t.data,s.value=!0,V.value="\u4FEE\u6539\u90E8\u95E8"})}function Y(){j.$refs.deptRef.validate(n=>{n&&(o.value._id!=null?Ve(o.value).then(t=>{D.success("\u4FEE\u6539\u6210\u529F"),s.value=!1,g()}):Ee(o.value).then(t=>{D.success("\u65B0\u589E\u6210\u529F"),s.value=!1,g()}))})}function Z(n){ke.confirm('\u662F\u5426\u786E\u8BA4\u5220\u9664\u540D\u79F0\u4E3A"'+n.deptName+'"\u7684\u6570\u636E\u9879?',"\u7CFB\u7EDF\u63D0\u793A",{confirmButtonText:"\u786E\u5B9A",cancelButtonText:"\u53D6\u6D88",type:"warning"}).then(function(){return ye(n._id)}).then(()=>{g(),D.success("\u5220\u9664\u6210\u529F")}).catch(()=>{})}return g(),Ie().then(n=>{n.data.forEach(t=>{U.value.push({label:t.name,value:t._id})})}),we().then(n=>v.value=n.data),(n,t)=>{const c=te,m=ne,R=oe,i=de,G=re,H=ue,q=se,f=ie,J=pe,F=_e,$=ce,K=me,W=fe,h=ve("hasPermi"),ee=ge;return r(),k("div",Te,[e(R,{gutter:10,class:"mb8"},{default:a(()=>[e(m,{span:1.5},{default:a(()=>[e(c,{type:"info",plain:"",icon:"Sort",onClick:Q},{default:a(()=>[De]),_:1})]),_:1},8,["span"])]),_:1}),y.value?x((r(),p(H,{key:0,data:B.value,"row-key":"_id","default-expand-all":E.value,"tree-props":{children:"children",hasChildren:"hasChildren"}},{default:a(()=>[e(i,{prop:"deptName",label:"\u90E8\u95E8\u540D\u79F0"}),e(i,{prop:"orderNum",label:"\u6392\u5E8F"}),e(i,{prop:"leader_name",label:"\u8D1F\u8D23\u4EBA"}),e(i,{prop:"phone",label:"\u90E8\u95E8\u7535\u8BDD"}),e(i,{label:"\u89D2\u8272"},{default:a(l=>[(r(!0),k(w,null,T(l.row.roleIds,b=>(r(),p(G,{style:{margin:"0 2px"}},{default:a(()=>[_(A(S(b)),1)]),_:2},1024))),256))]),_:1}),e(i,{label:"\u521B\u5EFA\u65F6\u95F4",align:"center",prop:"createTime"},{default:a(l=>[L("span",null,A(l.row.createTime),1)]),_:1}),e(i,{label:"\u64CD\u4F5C",align:"center","class-name":"small-padding fixed-width"},{default:a(l=>[l.row.parentId?x((r(),p(c,{key:0,link:"",icon:"Edit",onClick:b=>X(l.row)},{default:a(()=>[Be]),_:2},1032,["onClick"])),[[h,"1019"]]):I("",!0),x((r(),p(c,{link:"",icon:"Plus",onClick:b=>z(l.row)},{default:a(()=>[Ue]),_:2},1032,["onClick"])),[[h,"1018"]]),l.row.parentId?x((r(),p(c,{key:1,link:"",type:"danger",icon:"Delete",onClick:b=>Z(l.row)},{default:a(()=>[je]),_:2},1032,["onClick"])),[[h,"1020"]]):I("",!0)]),_:1})]),_:1},8,["data","default-expand-all"])),[[ee,N.value],[h,"1017"]]):I("",!0),e(W,{title:V.value,modelValue:s.value,"onUpdate:modelValue":t[5]||(t[5]=l=>s.value=l),width:"600px","append-to-body":""},{footer:a(()=>[L("div",Re,[e(c,{type:"primary",onClick:Y},{default:a(()=>[qe]),_:1}),e(c,{onClick:P},{default:a(()=>[Fe]),_:1})])]),default:a(()=>[e(K,{ref:"deptRef",model:d(o),rules:d(O),"label-width":"80px"},{default:a(()=>[e(R,null,{default:a(()=>[e(m,{span:12},{default:a(()=>[e(f,{label:"\u90E8\u95E8\u540D\u79F0",prop:"deptName"},{default:a(()=>[e(q,{modelValue:d(o).deptName,"onUpdate:modelValue":t[0]||(t[0]=l=>d(o).deptName=l),placeholder:"\u8BF7\u8F93\u5165\u90E8\u95E8\u540D\u79F0"},null,8,["modelValue"])]),_:1})]),_:1}),e(m,{span:12},{default:a(()=>[e(f,{label:"\u663E\u793A\u6392\u5E8F",prop:"orderNum"},{default:a(()=>[e(J,{modelValue:d(o).orderNum,"onUpdate:modelValue":t[1]||(t[1]=l=>d(o).orderNum=l),"controls-position":"right",min:0},null,8,["modelValue"])]),_:1})]),_:1}),e(m,{span:12},{default:a(()=>[e(f,{label:"\u8D1F\u8D23\u4EBA",prop:"leader_id"},{default:a(()=>[e($,{modelValue:d(o).leader_id,"onUpdate:modelValue":t[2]||(t[2]=l=>d(o).leader_id=l),placeholder:"\u8BF7\u9009\u62E9"},{default:a(()=>[(r(!0),k(w,null,T(U.value,l=>(r(),p(F,{key:l._id,label:l.label,value:l.value},null,8,["label","value"]))),128))]),_:1},8,["modelValue"])]),_:1})]),_:1}),e(m,{span:12},{default:a(()=>[e(f,{label:"\u8054\u7CFB\u7535\u8BDD",prop:"phone"},{default:a(()=>[e(q,{modelValue:d(o).phone,"onUpdate:modelValue":t[3]||(t[3]=l=>d(o).phone=l),placeholder:"\u8BF7\u8F93\u5165\u90E8\u95E8\u7535\u8BDD",maxlength:"11"},null,8,["modelValue"])]),_:1})]),_:1}),e(m,{span:12},{default:a(()=>[e(f,{label:"\u89D2\u8272"},{default:a(()=>[e($,{modelValue:d(o).roleIds,"onUpdate:modelValue":t[4]||(t[4]=l=>d(o).roleIds=l),multiple:"",placeholder:"\u8BF7\u9009\u62E9"},{default:a(()=>[(r(!0),k(w,null,T(v.value,l=>(r(),p(F,{key:l._id,label:l.roleName,value:l._id},null,8,["label","value"]))),128))]),_:1},8,["modelValue"])]),_:1})]),_:1})]),_:1})]),_:1},8,["model","rules"])]),_:1},8,["title","modelValue"])])}}};var Qe=Ce($e,[["__scopeId","data-v-1eedd402"]]);export{Qe as default};
