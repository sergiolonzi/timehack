import { defineStore } from "pinia";
import axios from "axios";
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useMessageStore } from "../messages/messageStore";
import { useTaskStore } from "../tasks/taskStore";

function getCookie() {
  return axios
    .post("/api/csrf")
    .then(function (response) {
      let cookieValue = null;
      let name = "csrftoken";
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
    })
    .catch(function (error) {});
}

export const useAuthStore = defineStore("authStore", () => {
  const loginInfo = ref({ username: "" });
  const router = useRouter();
  const messageStore = useMessageStore();
  const taskStore = useTaskStore();

  function loginUser(username, password) {
    getCookie().then(function (csrftoken) {
      axios
        .post(
          "/api/login",
          {
            username: username,
            password: password,
          },
          {
            headers: { "X-CSRFToken": csrftoken }, /// Overide this to check Token
          }
        )
        .then(function (response) {
          loginInfo.value = response.data;
          router.push("/tasks");
        })
        .catch(function (error) {
          if (error.response) {
            let listOfErrors = error.response.data.errors;
            let errorMessage = { title: "Fix the Errors:", list: listOfErrors };
            messageStore.addError(errorMessage);
          }
        });
    });
  }

  function isLoggedIn() {
    getCookie().then(function (csrftoken) {
      axios
        .post(
          "/api/is-login",
          {},
          {
            headers: { "X-CSRFToken": csrftoken }, /// Overide this to check Token
          }
        )
        .then(function (response) {
          validUser = response.data;
          return validUser;
        })
        .catch(function (error) {
          if (error.response) {
            let listOfErrors = error.response.data.errors;
            let errorMessage = { title: "Fix the Errors:", list: listOfErrors };
            messageStore.addError(errorMessage);
          }
        });
    });
  }

  function registerUser(userIn) {
    getCookie().then(function (csrftoken) {
      axios
        .post(
          "/api/register",
          {
            username: userIn.username,
            password: userIn.password,
            password_confirm: userIn.passwordConfirm,
            email: userIn.email,
          },
          {
            headers: { "X-CSRFToken": csrftoken },
          }
        )
        .then(function (response) {
          router.push("/login");
        })
        .catch(function (error) {
          if (error.response) {
            let listOfErrors = error.response.data.errors;
            let errorMessage = { title: "Fix the Errors:", list: listOfErrors };
            messageStore.addError(errorMessage);
          }
        });
    });
  }

  function logoutUser() {
    getCookie().then(function (csrftoken) {
      axios
        .post(
          "/api/logout",
          {},
          {
            headers: { "X-CSRFToken": csrftoken },
          }
        )
        .then(function (response) {
          loginInfo.value = {};
          taskStore.cleanAll();
          router.push("/login");
        })
        .catch(function (error) {
          if (error.response) {
            let listOfErrors = error.response.data.errors;
            let errorMessage = { title: "Fix the Errors:", list: listOfErrors };
            messageStore.addError(errorMessage);
          }
        });
    });
  }

  function loadUserInfo() {
    getCookie().then(function (csrftoken) {
      axios
        .get(
          "/api/user-info",
          {},
          {
            headers: { "X-CSRFToken": csrftoken },
          }
        )
        .then(function (response) {
          loginInfo.value = response.data;
        })
        .catch(function (error) {
          if (error.response) {
            let listOfErrors = error.response.data.errors;
            let errorMessage = { title: "Fix the Errors:", list: listOfErrors };
            messageStore.addError(errorMessage);
          }
        });
    });
  }

  function updateUser(userIn) {
    getCookie().then(function (csrftoken) {
      axios
        .put(
          "/api/user/",
          {
            password: userIn.password,
            password_confirm: userIn.passwordConfirm,
            email: userIn.email,
          },
          {
            headers: { "X-CSRFToken": csrftoken },
          }
        )
        .then(function (response) {
          loginInfo.value = response.data;
          router.push("/tasks");
        })
        .catch(function (error) {
          if (error.response) {
            let listOfErrors = error.response.data.errors;
            let errorMessage = { title: "Fix the Errors:", list: listOfErrors };
            messageStore.addError(errorMessage);
          }
        });
    });
  }

  return {
    loginInfo,
    loginUser,
    logoutUser,
    registerUser,
    updateUser,
    isLoggedIn,
    loadUserInfo,
  };
});
