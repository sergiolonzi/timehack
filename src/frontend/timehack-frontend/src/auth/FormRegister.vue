<script setup>
import { ref } from "vue";
import { useAuthStore } from "./authStore";

const usernameValue = ref("");
const passwordValue = ref("");
const emailValue = ref("");
const passwordConfirmValue = ref("");
import Message from "../messages/Message.vue";
const authStore = useAuthStore();

function registerUser() {
  //Also Validate Email Format.

  authStore.registerUser({
    username: usernameValue.value,
    email: emailValue.value,
    password: passwordValue.value,
    passwordConfirm: passwordConfirmValue.value,
  });
}
</script>
<template>
  <form @submit.prevent="registerUser" class="border py-4 px-4">
    <Message />
    <div class="form-group my-3">
      <label for="username">Username</label>
      <input
        type="text"
        class="form-control"
        id="inputUsername"
        placeholder="Enter Username"
        v-model="usernameValue"
        name="username"
        required
      />
    </div>
    <div class="form-group my-3">
      <label for="email">Email</label>
      <input
        type="text"
        class="form-control"
        id="inputEmail"
        placeholder="Enter Email"
        v-model="emailValue"
        name="email"
        required
      />
    </div>
    <div class="form-group my-3">
      <label for="password">Password</label>
      <input
        type="password"
        class="form-control"
        id="inputPassword"
        placeholder="Enter Password"
        v-model="passwordValue"
        name="password"
        required
      />
    </div>
    <div class="form-group my-3">
      <label for="passwordConfirm">Password Confirm</label>
      <input
        type="password"
        class="form-control"
        id="inputPasswordConfirm"
        placeholder="Confirm Password"
        v-model="passwordConfirmValue"
        name="passwordConfirm"
        required
      />
    </div>
    <button class="btn btn-primary">Register</button>
  </form>
</template>
<style></style>
