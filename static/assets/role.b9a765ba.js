import{a as r}from"./vendor.3587a8c4.js";function o(e){let t=JSON.parse(localStorage.getItem("user"));return r({url:"/system/role/list/"+(t.enterprise_id?t.enterprise_id:"abc"),method:"get",params:e})}function a(e){return r({url:"/system/role/"+e,method:"get"})}function l(e){let t=JSON.parse(localStorage.getItem("user"));return r({url:"/system/role/"+(t.enterprise_id?t.enterprise_id:"abc"),method:"post",data:e})}function n(e){let t=JSON.parse(localStorage.getItem("user"));return e.enterprise_id=t.enterprise_id?t.enterprise_id:"abc",r({url:"/system/role",method:"put",data:e})}function u(e){return r({url:"/system/role/dataScope",method:"put",data:e})}function d(e){return r({url:"/system/role/"+e,method:"delete"})}export{l as a,u as b,d,a as g,o as l,n as u};
