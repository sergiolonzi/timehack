<script setup>
import { ref } from "vue";
import FormRegister from "./FormRegister.vue";
import Navbar from "../Navbar.vue";
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
        <FormRegister />
      </div>
    </div>
  </div>
</template>
<style></style>
