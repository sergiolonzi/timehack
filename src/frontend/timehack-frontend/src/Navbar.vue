<script setup>
</script>

<template>
<div class="container">
<nav class="navbar navbar-expand-lg" data-bs="light">
<div class="container-fluid px-4">
<RouterLink to="/">
	<img id="logo" class="align-baseline"> </img>
</RouterLink>
<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
<span class="navbar-toggler-icon"></span>
</button>
<div class="collapse navbar-collapse justify-content-end" id="navbarSupportedContent">
<ul class="navbar-nav mb-2 mb-lg-0">
<li class="nav-item">
<RouterLink to="/" class="nav-link active" aria-current="page" >Home</RouterLink> 
</li>
</ul>
<ul class="navbar-nav mb-2 mb-lg-0">
<li class="nav-item">
<RouterLink to="/tasks" class="nav-link active" aria-current="page" >To Do</RouterLink> 
</li>
</ul>
<ul class="navbar-nav mb-2 mb-lg-0">
<li class="nav-item">
<RouterLink to="/login" class="nav-link active" aria-current="page" >Login</RouterLink> 
</li>
</ul>
<ul class="navbar-nav mb-2 mb-lg-0">
<li class="nav-item">
<RouterLink class="nav-link active" aria-current="page"  to="/register">Register</RouterLink> 
</li>
</ul>
</div>


</div >
</nav >
</div>


</template>

<style>

</style>
