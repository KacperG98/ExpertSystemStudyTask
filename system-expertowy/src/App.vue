<template>
    <header>
      <div class="text-center">
        <img src="./assets/languages.png" class="rounded languages" alt="languages.png">
      </div>
      <h1>Wybierzemy ci pierwszy język programowania</h1>
      <nav>
        <RouterLink class="btn btn-light btn-sm" to="/">Zacznij od nowa</RouterLink>
      </nav>
    </header>
    <main class="m-4">
      <RouterView />
    </main>
</template>


<script setup>

</script>


<style>
.languages{
  width: 20rem;
}
#button{
        font-size: 1.5rem;
        padding: 1rem 2rem;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
