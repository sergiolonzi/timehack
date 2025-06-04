import { createWebHashHistory, createRouter } from "vue-router";
import Login from "./auth/Login.vue";
import Register from "./auth/Register.vue";
import Settings from "./auth/Settings.vue";
import MainTasks from "./tasks/MainTasks.vue";
import Home from "./Home.vue";
import axios from "axios";

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function isLoggedIn() {
  const csrftoken = getCookie("csrftoken");
  return axios
    .post(
      "/api/is-login",
      {},
      {
        headers: { "X-CSRFToken": csrftoken }, /// Overide this to check Token
      }
    )
    .then(function (response) {
      console.log("------");
      const validUser = response.data.is_login;
      console.log("------" + validUser);
      return validUser;
    })
    .catch(function (error) {
      console.log("------" + error.response.status);
      return false;
    });
}

async function log(to, from) {}

const routes = [
  {
    path: "/",
    component: Home,
    name: "home",
  },
  {
    path: "/tasks",
    component: MainTasks,
    name: "tasks",
  },
  {
    path: "/register",
    component: Register,
    name: "register",
  },
  {
    path: "/login",
    component: Login,
    name: "login",
  },
  {
    path: "/settings",
    component: Settings,
    name: "settings",
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

router.beforeEach(async (to, from) => {
  if (to.name === "home" || to.name === "login" || to.name === "register") {
    return true;
  }
  return isLoggedIn()
    .then(function (result) {
      return result;
    })
    .catch(function (error) {
      return false;
    });
});
export default router;
