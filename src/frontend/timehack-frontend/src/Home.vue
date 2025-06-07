<script setup>
import { ref } from "vue";
import FormLogin from "./auth/FormLogin.vue";
import Navbar from "./Navbar.vue";
</script>

<template>
  <Navbar />
  <div class="container">
    <div class="row align-items-center">
      <div class="col"></div>
    </div>
  </div>
  <div class="container py-5">
    <div class="row align-items-center">
      <div class="col-6 offset-3">
        <FormLogin />
      </div>
    </div>
  </div>
</template>
<style></style>
