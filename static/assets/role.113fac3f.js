import{a as t}from"./vendor.7785c9e9.js";import{c as r}from"./index.e17427d4.js";function n(e){return t({url:"/system/role/list/"+r.state.userInfo.enterprise_id,method:"get",params:e})}function a(e){return t({url:"/system/role/"+e,method:"get"})}function u(e){return t({url:"/system/role/"+r.state.userInfo.enterprise_id,method:"post",data:e})}function d(e){return e.enterprise_id=r.state.userInfo.enterprise_id,t({url:"/system/role",method:"put",data:e})}function l(e){return t({url:"/system/role/dataScope",method:"put",data:e})}function i(e){return t({url:"/system/role/"+e,method:"delete"})}export{u as a,l as b,i as d,a as g,n as l,d as u};