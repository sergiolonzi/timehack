<script setup>
import { ref } from "vue";
import { useAuthStore } from "./authStore";
import Message from "../messages/Message.vue";
import { onMounted } from "vue";

const passwordConfirmValue = ref("");
const passwordValue = ref("");
const emailValue = ref("");
const title = ref("User Settings");

const authStore = useAuthStore();

function updateUser() {
  //Also Validate Email Format.

  authStore.updateUser({
    password: passwordValue.value,
    passwordConfirm: passwordConfirmValue.value,
    email: emailValue.value,
  });
}
onMounted(() => {
  authStore.loadUserInfo();
});
</script>

<template>
  <div class="container">
    <div class="row align-items-center">
      <div class="col">
        <h1>{{ title }}</h1>
      </div>
    </div>
  </div>
  <div class="container py-5">
    <div class="row align-items-center">
      <div class="col">
        <form @submit.prevent="updateUser" class="border py-4 px-4">
          <Message />
          <div class="form-group my-3">
            <label>Username: </label>
            <p>{{ authStore.loginInfo.username }}</p>
          </div>
          <div class="form-group my-3">
            <label for="emailValue">Email</label>
            <input
              type="text"
              class="form-control"
              id="emailValue"
              placeholder="Enter New E-Mail"
              v-model="emailValue"
              name="Email"
            />
          </div>
          <div class="form-group my-3">
            <label for="passwordValue">Password</label>
            <input
              type="password"
              class="form-control"
              id="passwordValue"
              placeholder="Enter New Password"
              v-model="passwordValue"
              name="Password"
            />
          </div>
          <div class="form-group my-3">
            <label for="passwordConfirmValue">Password Confirm</label>
            <input
              type="password"
              class="form-control"
              id="passwordConfirmValue"
              placeholder="Confirm New Password"
              v-model="passwordConfirmValue"
              name="PasswordConfirm"
            />
          </div>
          <button class="btn btn-primary">Save</button>
        </form>
      </div>
    </div>
  </div>
</template>

<style></style>
