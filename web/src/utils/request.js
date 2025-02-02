import axios from "axios";
import { parse_token } from "./tools";
import store from "../store";
export const get_token = () => {
  let t = localStorage.getItem("token");
  if (t != null) {
    store().is_login = true;
  } else {
    store.is_login = false;
  }
  return "Bearer " + t;
};

// TODO:axios-自定义请求对象
const r = () => {
  let r_ = axios.create({
    baseURL: import.meta.env.VITE_BASE_API,
    timeout: 15000,
    headers: {
      Authorization: get_token(),
    },
  });
  //TODO:axios-拦截器
  r_.interceptors.request.use(
    (config) => {
      console.log(config.url);
      console.log(config);
      if (config.url.startsWith("/admin")) {
        parse_token();
      }
      return config; //必须返回
    },
    (error) => {
      // if (error?.response?.data?.code == "token_not_valid") {
      //   localStorage.removeItem("token"); //token无效了必须删除token
      //   window.location = "/#/login"; //token失效跳转登录页
      // }
      // return Promise.reject("interceptors.request.error", error);
    }
  );
  r_.interceptors.response.use(
    (res) => {
      return res; //必须返回
    },
    (error) => {
      console.log("error", error);
      if (error?.response?.status == 401) {
        ElMessage({
          showClose: true,
          message: error.response.data.detail,
          center: true,
        });
        localStorage.clear();
        window.location = "/#/login/";
      } else if (error?.response?.status == 500) {
        ElMessage({
          showClose: true,
          message: "服务器错误",
          center: true,
        });
      } else if (error?.response?.data?.detail) {
        ElMessage({
          showClose: true,
          message: error?.response?.data?.detail,
          center: true,
        });
      } else if (error?.response?.data?.code) {
        ElMessage({
          showClose: true,
          message: error?.response?.data?.code[0],
          center: true,
        });
      } else if (error?.response?.data) {
        ElMessage({
          showClose: true,
          message: error?.response?.data,
          center: true,
        });
      } else {
        ElMessage({
          showClose: true,
          message: error,
          center: true,
        });
      }
      return error?.response;
    }
  );
  return r_;
};

export default r;
