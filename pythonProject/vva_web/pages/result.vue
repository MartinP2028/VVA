<template>
  <div class="upload-container">
    <img src="../public/LogoF1.png" alt="F1 Logo" class="logo" />
    <div class="wrapper">
        <table>
      <thead>
        <tr>
          <th class="pilote">Classement Final</th>
          <th class="pilote">Pilotes</th>
          <th class="pilote">Prédictions</th>
        </tr>
      </thead>
      <tbody>
        <tr
          class="pilote"
          v-for="(result, index) in drivers"
          :key="index"
        >
          <td>{{ index + 1 }}</td>  <!-- Classement final -->
          <td>{{ result.driver_name }}</td>  <!-- Nom du pilote -->
          <td>{{ result.prediction.toFixed(2) }}</td>  <!-- Prédiction arrondie -->
        </tr>
      </tbody>
    </table>
      </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
// const drivers = ref([])
// // Fonction pour charger les données JSON
// const fetchData = async () => {
//   try {
//     const response = await fetch('/result.json')  // Chemin vers le fichier JSON
//     const data = await response.json()            // Lire et convertir le JSON en objet JavaScript
//     drivers.value = data                          // Stocker les données dans la variable réactive
//   } catch (error) {
//     console.error('Erreur lors de la récupération des données :', error)
//   }
// }
// // Appeler fetchData lorsque le composant est monté
// onMounted(() => {
//   fetchData()
// })
const drivers = ref([])
const fetchData = async () => {
  try {
    const response = await fetch('http://localhost:8000/api/drivers')  // Appel à l'API FastAPI
    const data = await response.json()  // Convertir la réponse en JSON
    drivers.value = data  // Mettre à jour la liste des pilotes
  } catch (error) {
    console.error('Erreur lors de la récupération des données :', error)
  }
}
onMounted(() => {
  fetchData()
})
</script>

<style scoped>
.logo {
  position: absolute;
  top: 20px;
  left: 20px;
  width: 300px;
  z-index: 1000;
  height: auto;
}
.upload-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: url("../public/f1_background.png") no-repeat center center/cover;
  position: relative;
  flex-direction: column;
  padding: 20px;
}
.table-container {
  margin: 20px 0;
  width: 15%;
  text-align: left;
  float: left;
  grid-column: 1 / 3;
  grid-row: 1;
}

h1 {
  font-weight: bold;
  color: #ffffff;
  width: 200%;
  padding-bottom: 10px;
}

table {
  width: 100%;
  border-collapse: collapse;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

th,
td {
  padding: 5px;
  border: 1px solid #ddd;
}

th {
  background-color: #ee0000;
  font-weight: bold;
  font-size: 0.7rem;
}

tr:nth-child(even) {
  background-color: #323232; /* Couleur pour les lignes paires */
}

tr:nth-child(odd) {
  background-color: #242424; /* Couleur pour les lignes impaires */
}
.pilote {
  color: white;
}

.wrapper {
  padding-top: 100px;
  width: 100%;
  height: 80vh;
  display: flex;
  align-items: center;
  justify-content: space-around;
}
</style>
