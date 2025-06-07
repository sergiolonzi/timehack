<script setup>
import { ref, computed } from "vue";
import { useAuthStore } from "./authStore";
import Message from "../messages/Message.vue";
import { onMounted } from "vue";

const passwordConfirmValue = ref("");
const passwordValue = ref("");
const emailValue = ref("");
const usernameValue = ref("");
const title = ref("User Settings");
import { useRouter } from "vue-router";
const authStore = useAuthStore();
const router = useRouter();

function updateUser() {
  //Also Validate Email Format.
  authStore.updateUser({
    password: passwordValue.value,
    passwordConfirm: passwordConfirmValue.value,
    email: emailValue.value,
  });
}

const nameValue = computed({
  // getter
  get() {
    return authStore.loginInfo.username;
  },
  // setter
  set(newValue) {
    usernameValue.value = newValue;
  },
});

const email = computed({
  // getter
  get() {
    return authStore.loginInfo.email;
  },
  // setter
  set(newValue) {
    emailValue.value = newValue;
  },
});

onMounted(() => {
  authStore.loadUserInfo();
});

function cancel() {
  router.push("/tasks");
}
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
      <div class="col-6 offset-3">
        <form @submit.prevent="updateUser" class="border py-4 px-4">
          <Message />
          <div class="form-group my-3">
            <label>Username: </label>
            <input
              type="text"
              class="form-control rounded-0"
              id="emailValue"
              v-model="nameValue"
              name="Email"
              readonly
            />
          </div>
          <div class="form-group my-3">
            <label for="emailValue">Email</label>
            <input
              type="text"
              class="form-control rounded-0"
              id="emailValue"
              placeholder="Enter New E-Mail"
              v-model="email"
              name="Email"
            />
          </div>
          <div class="form-group my-3">
            <label for="passwordValue">Password</label>
            <input
              type="password"
              autocomplete="off"
              class="form-control rounded-0"
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
              autocomplete="off"
              class="form-control rounded-0"
              id="passwordConfirmValue"
              placeholder="Confirm New Password"
              v-model="passwordConfirmValue"
              name="PasswordConfirm"
            />
          </div>

          <div class="d-grid gap-2 d-md-flex justify-content-end">
            <button class="btn btn-primary rounded-0">Save</button>
            <button
              class="btn btn-outline-secondary rounded-0"
              @click.prevent="cancel"
            >
              Cancel
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<style></style>
