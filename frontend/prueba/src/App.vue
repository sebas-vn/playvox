<template>
  <div id="app">
    <Header/>
    
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import Header from './components/Header.vue'

export default {
  name: 'app',
  components: {
    HelloWorld,
    Header
  }
}
</script>

<style>
html, body {
  height: 100%;
  margin: 0;
  padding: 0;
}



#app {
  text-align: center;
  background-color: #35495E;
  height: 100%;
}
</style>
