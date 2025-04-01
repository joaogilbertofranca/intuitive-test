<template>
  <div id="app">
    <h1>Buscar Operadoras de Saúde</h1>
    <input v-model="termoBusca" @input="buscarOperadoras" placeholder="Digite um termo de busca..." />
    <ul>
      <li v-for="operadora in operadoras" :key="operadora.id">
        <strong>{{ operadora.razao_social }}</strong> ({{ operadora.nome_fantasia }}) - {{ operadora.cidade }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      termoBusca: '',
      operadoras: []
    };
  },
  methods: {
    buscarOperadoras() {
      if (this.termoBusca.length >= 3) {
        axios.get(`http://localhost:5000/api/buscar_operadoras?termo=${this.termoBusca}`)
          .then(response => {
            this.operadoras = response.data;
          })
          .catch(error => {
            console.error('Erro ao buscar operadoras:', error);
          });
      } else {
        this.operadoras = [];
      }
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  margin-top: 60px;
}

input {
  padding: 8px;
  margin-bottom: 20px;
  font-size: 16px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  padding: 8px;
  margin-bottom: 5px;
  background-color: #f4f4f4;
}
</style>
