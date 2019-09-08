<template>
  <div id="header">
    <img alt="PlayV logo" id="logo" src="../assets/playvox.png">
  </div>
</template>

<script>
export default {
  name: 'Header'
}
</script>

<style scoped>
  #header{
    display: flex;
    justify-content: start;
    align-items: center;
    max-width: 100%;
    height: 50px;
    background-color: #fff; 
    padding: 10px;
/*     -webkit-box-shadow: 0px 0px 21px 0px rgba(0,0,0,0.4);
    -moz-box-shadow: 0px 0px 21px 0px rgba(0,0,0,0.4);
    box-shadow: 0px 0px 21px 0px rgba(0,0,0,0.4); */
  }

  #logo{
    height: 30px;
    width: auto;
  }
</style>
