<template>
  <div id="app">
    <Header />
    <div id="content">
      <div class="table_holder">
        <TableUsers />
      </div>
    </div>
  </div>
</template>

<script>
/* LIBS */
import axios from "axios";
import Vue from "vue";
import BootstrapVue from "bootstrap-vue";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

Vue.use(BootstrapVue);

/* COMPONENTS */
import Header from "./components/Header";
import TableUsers from "./components/TableUser";

export default {
  name: "app",
  components: {
    Header,
    TableUsers
  }
};
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Nunito+Sans&display=swap");

html,
body {
  display: flex;
  flex-direction: column;
  height: 100%;
  margin: 0;
  padding: 0;
  font-family: "Nunito Sans", sans-serif;
}

#content {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  width: 100%;
  height: calc(100% - 70px);
  align-self: center;
}

.table_holder{
  width: 90%;
  height: auto;
  padding: 50px;
  background-color: #4CC08B;
  box-shadow: 0px 0px 25px rgba(0,0,0,0.4);
  border-radius: 4px;
}

#app {
  text-align: center;
  background-color: #35495e;
  min-height: 100%;
}
</style>
