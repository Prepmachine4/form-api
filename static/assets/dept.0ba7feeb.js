import{a as t}from"./vendor.7785c9e9.js";import{c as r}from"./index.da34fb28.js";function o(){return JSON.parse(localStorage.getItem("user")),t({url:"/system/dept/list/"+r.state.userInfo.enterprise_id,method:"get"})}function u(e){return t({url:"/system/dept/"+e,method:"get"})}function d(e){return JSON.parse(localStorage.getItem("user")),t({url:"/system/dept/"+r.state.userInfo.enterprise_id,method:"post",data:e})}function n(e){return t({url:"/system/dept",method:"put",data:e})}function p(e){return t({url:"/system/dept/"+e,method:"delete"})}function l(){return JSON.parse(localStorage.getItem("user")),t({url:"/system/dept/treeselect/"+r.state.userInfo.enterprise_id,method:"get"})}export{d as a,p as d,u as g,o as l,l as t,n as u};
