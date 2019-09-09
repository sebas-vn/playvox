<template>
  <b-container fluid>
    <!-- User Interface controls -->
    <b-row>
      <b-col lg="6" class="my-1">
        <b-form-group label="Filtro" label-cols-sm="3" label-align-sm="right" label-size="sm" label-for="filterInput" class="mb-0">
          <b-input-group size="sm">
            <b-form-input v-model="filter" type="search" id="filterInput" placeholder="Buscar"></b-form-input>
            <b-input-group-append>
              <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
            </b-input-group-append>
          </b-input-group>
        </b-form-group>
      </b-col>

      <b-col sm="5" md="6" class="my-1">
        <b-form-group label="Por Página" label-cols-sm="6" label-cols-md="4" label-cols-lg="3" label-align-sm="right" label-size="sm" label-for="perPageSelect" class="mb-0">
          <b-form-select v-model="perPage" id="perPageSelect" size="sm" :options="pageOptions"></b-form-select>
        </b-form-group>
      </b-col>
    </b-row>

    <!-- Main table element -->
    <b-table show-empty small stacked="md" :items="items" :fields="fields" :current-page="currentPage" :per-page="perPage" :filter="filter"
      :filterIncludedFields="filterOn"
      :dark="dark"
      :sort-by.sync="sortBy"
      :sort-desc.sync="sortDesc"
      :sort-direction="sortDirection"
      @filtered="onFiltered"
    >

      <template v-slot:cell(actions)="row">
        <b-button
          size="sm"
          @click="getNoteUser(row.item, row.button)"
          class="mr-1"
        >View Notes</b-button>
      </template>
    </b-table>
    <b-row>
      <b-col sm="12" md="12" class="my-1">
        <b-pagination
          v-model="currentPage"
          :total-rows="totalRows"
          :per-page="perPage"
          align="fill"
          size="sm"
          class="my-0"
        ></b-pagination>
      </b-col>
    </b-row>

    <!-- Info modal -->
    <b-modal :id="infoModal.id" :title="infoModal.title" ok-only @hide="resetInfoModal">
      <pre>{{ infoModal.content }}</pre>
    </b-modal>
  </b-container>
</template>

<script>
import axios from "axios";

export default {
  name: "TableUsers",
  data() {
    return {
      items: [],
      fields: [
        {
          key: "name",
          label: "Nombre",
          sortable: true,
          sortDirection: "desc"
        },
        {
          key: "last_name",
          label: "Apellido",
          sortable: true,
          sortDirection: "desc"
        },
        {
          key: "age",
          label: "Edad",
          sortable: true,
          class: "text-center"
        },
        {
          key: "email",
          label: "Correo",
          sortable: true,
          class: "text-center"
        },
        { key: "actions", label: "Actions" }
      ],
      totalRows: 1,
      currentPage: 1,
      perPage: 5,
      pageOptions: [5, 10, 15],
      sortBy: "",
      dark: "true",
      sortDesc: false,
      sortDirection: "asc",
      filter: null,
      filterOn: [],
      infoModal: {
        id: "info-modal",
        title: "",
        content: ""
      }
    };
  },
  computed: {
    sortOptions() {
      // Create an options list from our fields
      return this.fields
        .filter(f => f.sortable)
        .map(f => {
          return { text: f.label, value: f.key };
        });
    }
  },
  mounted() {
    this.getUsers()
  },
  methods: {
    getUsers() {
      axios
        .get("http://127.0.0.1:5000/api/v1/user/all")
        .then(res => {
          this.items = res.data;
          this.totalRows = this.items.length;
        })
        .catch(err => console.log(err));
    },
    getNoteUser(item, button){
      let id = item._id.$oid;
      axios.get(`http://127.0.0.1:5000/api/v1/note/${id}`)
        .then (res => {
          if(res.data.length < 1){
            this.infoModal.content = 'No notes for this user!'
          }
          else{
            this.infoModal.content = JSON.stringify(res.data, null, 2)
          }
          })
        .catch (err => this.infoModal.content = 'Petición erronea');
      this.infoModal.title = `Notes: ${item.name} ${item.last_name}`;
      this.$root.$emit('bv::show::modal', this.infoModal.id, button)
    },
    info(item, index, button) {
      this.infoModal.title = `Row index: ${index}`;
      this.infoModal.content = JSON.stringify(item, null, 2);
      this.$root.$emit("bv::show::modal", this.infoModal.id, button);
    },
    resetInfoModal() {
      this.infoModal.title = "";
      this.infoModal.content = "";
    },
    onFiltered(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    }
  }
};
</script>

<style scoped>
  .table{
    width: 100%;
    margin-bottom: 1rem;
    margin-top: 2rem;
    color: #fff;
    box-shadow: 0px 0px 25px rgba(0,0,0,0.4);
    border-radius: 5px;
  }
</style>