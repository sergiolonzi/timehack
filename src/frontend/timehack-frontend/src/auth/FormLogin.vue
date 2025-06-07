<script setup>
import { ref } from "vue";
import { useAuthStore } from "./authStore";
import Message from "../messages/Message.vue";

// Initialize after loading
const authStore = useAuthStore();

const usernameValue = ref("");
const passwordValue = ref("");

function loginUser() {
  authStore.loginUser(usernameValue.value, passwordValue.value);
}
</script>
<template>
  <form @submit.prevent="loginUser" class="border py-4 px-4">
    <h1 class="greeting">Login</h1>
    <Message />

    <div class="form-group my-3">
      <label for="username">Username</label>
      <input
        type="text"
        class="form-control rounded-0"
        id="inputUsername"
        placeholder="Enter Username"
        v-model="usernameValue"
        name="username"
        required
      />
    </div>
    <div class="form-group my-3">
      <label for="password">Password</label>
      <input
        type="password"
        v-model="passwordValue"
        name="password"
        class="form-control rounded-0"
        id="inputPassword"
        placeholder="Enter Password"
        required
      />
    </div>
    <ul class="nav justify-content-center list-unstyled d-flex">
      <li class="ms-3">
        <button class="btn btn-primary rounded-0">Login</button>
      </li>
      <li class="ms-3 align-bottom">
        <RouterLink to="/register" class="nav-link"
          >Go to Registration</RouterLink
        >
      </li>
    </ul>
  </form>
</template>
<style></style>
