import{_ as J,b as q,u as L,d as T,q as C,r as d,Q as P,a as g,R as H,e as U,o as x,f as $,g as D,j as e,k as a,z as B,h as b,y as W,m as c,S as z,E,n as R,W as Q,X,aE as G,aF as K,am as Z,A as ee,B as te,C as ae,as as oe,P as le,p as se,l as ne}from"./vendor.3587a8c4.js";const re={class:"box"},ie={class:"card"},de={key:0,style:{width:"60%",display:"flex","justify-content":"right"}},ue=c("\u6682\u5B58"),ce=c("\u63D0\u4EA4"),_e={props:["enableEdit","formData","formId"],setup(n){const s=n,I=q(),_=L(),h=T();let m=C({}),v=C({}),p=C({});const r=d(null);let y=I.query._id||s.formId;const w=h.state.userInfo;P(async()=>{m=(await g.get(`/form/${y}`)).data.struct,r.value.setFormJson(m),await H(()=>{s.enableEdit||r.value.disableForm(),s.formData&&!s.enableEdit&&r.value.setFormData(JSON.parse(s.formData)),s.enableEdit&&localStorage.getItem("formData")&&r.value.setFormData(JSON.parse(localStorage.getItem("formData")))})});const S=()=>{r.value.getFormData().then(i=>{let o=JSON.stringify(i);localStorage.setItem("formData",o)})},k=()=>{r.value.getFormData().then(i=>{let o=JSON.stringify(i),t=w._id,l=z().format("YYYY-MM-DD HH:mm:ss");g.post(`/data/${y}`,{create_time:l,user_id:t,data:o}).then(f=>{f.status!==200?E.error("\u63D0\u4EA4\u5931\u8D25\uFF01"):(E.success("\u63D0\u4EA4\u6210\u529F\uFF01"),_.push(`/user/${t}`))}),localStorage.removeItem("formData")}).catch(i=>{E.error(i)})};return(i,o)=>{const t=R,l=U("v-form-render");return x(),$("div",re,[D("div",ie,[s.enableEdit?(x(),$("span",de,[e(t,{onClick:S},{default:a(()=>[ue]),_:1})])):B("",!0),e(l,{"form-json":b(m),"form-data":b(v),"option-data":b(p),ref_key:"vFormRef",ref:r},null,8,["form-json","form-data","option-data"]),s.enableEdit?(x(),W(t,{key:1,type:"primary",style:{width:"200px"},onClick:k},{default:a(()=>[ce]),_:1})):B("",!0)])])}}};var me=J(_e,[["__scopeId","data-v-b26f7fe4"]]);function pe(){let n=JSON.parse(localStorage.getItem("user"));return g.get(`/audit/list/now/${n._id}`)}function fe(){let n=JSON.parse(localStorage.getItem("user"));return g.get(`/audit/list/history/${n._id}`)}function ve(n,s){return g.post(`/audit/${n}`,s)}const ge=n=>(se("data-v-1557619c"),n=n(),ne(),n),be={class:"app-container"},he=c("\u5BA1\u6838"),ye=c("\u5BA1\u6279\u610F\u89C1"),xe={style:{display:"flex",width:"100%","justify-content":"center"}},De=ge(()=>D("br",null,null,-1)),Ee={style:{"text-align":"center"}},Ie=c("\u6E05\u7A7A"),we=c("\u901A\u8FC7"),Se=c("\u4E0D\u901A\u8FC7"),ke={setup(n){const s=d([]),I=d([]),_=d(!1),h=d(),m=d(),v=d(),p=d(""),r=d(),y=T(),w=o=>{r.value=o,h.value=o.data,m.value=o.form._id,_.value=!0};function S(){pe().then(o=>s.value=o.data),fe().then(o=>I.value=o.data)}const k=()=>{p.value="",v.value.reset()},i=o=>{v.value.generate().then(t=>{console.log(t),ve(r.value._id,{user_id:y.state.userInfo._id,index:r.value.audit_user_index,opinion:p.value,sign:t,result:o}),_.value=!1,E.success("\u5BA1\u6838\u6210\u529F")})};return S(),(o,t)=>{const l=Q,f=R,N=X,F=G,j=K,O=Z,A=ee,V=te,M=ae,Y=oe;return x(),$("div",be,[e(j,{"tab-position":"left"},{default:a(()=>[e(F,{label:"\u7B49\u5F85\u5BA1\u6279"},{default:a(()=>[e(N,{data:s.value},{default:a(()=>[e(l,{type:"index",align:"center"}),e(l,{label:"\u4E1A\u52A1\u540D\u79F0",align:"center",prop:"form.name"}),e(l,{label:"\u586B\u5199\u4EBA",align:"center",prop:"user.name"}),e(l,{label:"\u586B\u5199\u8005\u90E8\u95E8",align:"center",prop:"user.deptName"}),e(l,{label:"\u586B\u5199\u65F6\u95F4",align:"center",prop:"create_time",width:"180"}),e(l,{label:"\u64CD\u4F5C",align:"center","class-name":"small-padding fixed-width"},{default:a(u=>[e(f,{type:"text",icon:"View",onClick:Ce=>w(u.row)},{default:a(()=>[he]),_:2},1032,["onClick"])]),_:1})]),_:1},8,["data"])]),_:1}),e(F,{label:"\u5BA1\u6279\u5386\u53F2"},{default:a(()=>[e(N,{data:s.value},{default:a(()=>[e(l,{type:"index",align:"center"}),e(l,{label:"\u4E1A\u52A1\u540D\u79F0",align:"center",prop:"form.name"}),e(l,{label:"\u586B\u5199\u4EBA",align:"center",prop:"user.name"}),e(l,{label:"\u586B\u5199\u8005\u90E8\u95E8",align:"center",prop:"user.deptName"}),e(l,{label:"\u586B\u5199\u65F6\u95F4",align:"center",prop:"create_time",width:"180"})]),_:1},8,["data"])]),_:1})]),_:1}),e(Y,{top:"5vh",title:"\u5BA1\u6838",modelValue:_.value,"onUpdate:modelValue":t[3]||(t[3]=u=>_.value=u),width:"80vw"},{default:a(()=>[e(b(me),{"form-id":m.value,"enable-edit":!1,"form-data":h.value},null,8,["form-id","form-data"]),e(O,null,{default:a(()=>[ye]),_:1}),D("span",xe,[e(M,{style:{width:"30vw",border:"1px dashed gray",padding:"20px"}},{default:a(()=>[e(V,{label:"\u610F\u89C1"},{default:a(()=>[e(A,{modelValue:p.value,"onUpdate:modelValue":t[0]||(t[0]=u=>p.value=u)},null,8,["modelValue"])]),_:1}),e(V,{required:"",label:"\u7B7E\u540D"},{default:a(()=>[e(b(le),{ref_key:"sign",ref:v,isClearBgColor:!1,bgColor:"#eceef1",width:300,height:150,isCrop:!1,lineWidth:6,lineColor:"#000000"},null,512)]),_:1})]),_:1})]),De,D("div",Ee,[e(f,{type:"info",onClick:k},{default:a(()=>[Ie]),_:1}),e(f,{type:"success",onClick:t[1]||(t[1]=u=>i(!0))},{default:a(()=>[we]),_:1}),e(f,{type:"danger",onClick:t[2]||(t[2]=u=>i(!1))},{default:a(()=>[Se]),_:1})])]),_:1},8,["modelValue"])])}}};var Ne=J(ke,[["__scopeId","data-v-1557619c"]]);export{Ne as default};