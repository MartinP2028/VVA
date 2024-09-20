<template>
  <div class="upload-container">
    <img src="/LogoF1.png" alt="F1 Logo" class="logo" />
    <div class="wrapper">
      <div class="table-container">
        <h1>Liste des Pilotes</h1>
        <table>
          <thead>
            <tr>
              <th class="pilote">grid position</th>
              <th class="pilote">Noms</th>
            </tr>
          </thead>
          <tbody>
            <tr
              class="pilote"
              v-for="(driver, index) in driverNames"
              :key="driver"
            >
              <td>{{ grid_pos[index] }}</td>
              <td>{{ driver }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <button class="suivant-btn" @click="goToResult">Start</button>
      <div class="circuit_container">
        <NuxtImg
          class="circuit"
          :src="get_circuit_path(circuit)"
          alt="Circuit"
        />
        <p class="circuit_name">{{ circuit }}</p>
      </div>
    </div>
  </div>
</template>


<script setup>
import { ref, onMounted } from "vue";
import { useFetch } from "#app";
import { useRouter } from "vue-router";

const router = useRouter();
const driverNames = ref([]);
const grid_pos = ref([]);
const circuit = ref("");

// Récupération du circuit via l'API
onMounted(async () => {
  try {
    const { data, error } = await useFetch("/api/circuit");

    if (error.value) {
      console.error("Erreur lors de la récupération du circuit", error.value);
    } else if (data.value) {
      circuit.value = String(data.value);
    }
  } catch (err) {
    console.error("Erreur générale", err);
  }
});

// Fonction pour obtenir le chemin de l'image du circuit
const get_circuit_path = (circuitName) => {
  let imagePath = "";
  switch (circuitName) {
    case "Abu Dhabi Grand Prix":
      imagePath = "/races/aboudhabi_circuit.avif";
      break;
    case "Australian Grand Prix":
      imagePath = "/races/australia_circuit.avif";
      break;
    case "Bahrain Grand Prix":
      imagePath = "/races/Bahrain Circuit.avif";
      break;
    case "Belgian Grand Prix":
      imagePath = "/races/Belgium Circuit.avif";
      break;
    case "Canadian Grand Prix":
      imagePath = "/races/canada_circuit.avif";
      break;
    case "70th Anniversary Grand Prix":
      imagePath = "/races/Circuit 70th Anniversary.png";
      break;
    case "Austrian Grand Prix":
      imagePath = "/races/Circuit Autriche.avif";
      break;
    case "Azerbaijan Grand Prix":
      imagePath = "/races/Circuit Baku.avif";
      break;
    case "Brazilian Grand Prix":
    case "São Paulo Grand Prix":
      imagePath = "/races/Circuit Brésil.avif";
      break;
    case "Chinese Grand Prix":
      imagePath = "/races/Circuit Chine.avif";
      break;
    case "Eifel Grand Prix":
      imagePath = "/races/Circuit Eifel Allemagne.avif";
      break;
    case "Emilia Romagna Grand Prix":
      imagePath = "/races/Circuit Emilia Romagna.avif";
      break;
    case "Spanish Grand Prix":
      imagePath = "/races/Circuit Espagne.avif";
      break;
    case "French Grand Prix":
      imagePath = "/races/Circuit France.avif";
      break;
    case "British Grand Prix":
      imagePath = "/races/Circuit Grande-Bretagne.avif";
      break;
    case "Hungarian Grand Prix":
      imagePath = "/races/Circuit Hongrie.avif";
      break;
    case "Italian Grand Prix":
      imagePath = "/races/Circuit Italie.avif";
      break;
    case "Japanese Grand Prix":
      imagePath = "/races/Circuit Japon.avif";
      break;
    case "Mexican Grand Prix":
    case "Mexico City Grand Prix":
      imagePath = "/races/Circuit Mexique.avif";
      break;
    case "Monaco Grand Prix":
      imagePath = "/races/Circuit Monaco.avif";
      break;
    case "Singapore Grand Prix":
      imagePath = "/races/Circuit Singapour.avif";
      break;
    case "Styrian Grand Prix":
      imagePath = "/races/Circuit Styria.avif";
      break;
    case "Tuscan Grand Prix":
      imagePath = "/races/Circuit Tuscany.avif";
      break;
    case "United States Grand Prix":
      imagePath = "/races/Circuit USA.avif";
      break;
    case "German Grand Prix":
    case "Dutch Grand Prix":
      imagePath = "/races/Hockenheim Circuit.avif";
      break;
    case "Las Vegas Grand Prix":
      imagePath = "/races/lasvegas_circuit.avif";
      break;
    case "Miami Grand Prix":
      imagePath = "/races/miami_circuit.avif";
      break;
    case "Portuguese Grand Prix":
      imagePath = "/races/portugal_circuit.png";
      break;
    case "Qatar Grand Prix":
      imagePath = "/races/quatar_circuit.avif";
      break;
    case "Russian Grand Prix":
      imagePath = "/races/Russia Circuit.avif";
      break;
    case "Sakhir Grand Prix":
      imagePath = "/races/sakhir_circuit.avif";
      break;
    case "Saudi Arabian Grand Prix":
      imagePath = "/races/Saudi Arabia Circuit.avif";
      break;
    case "Turkish Grand Prix":
      imagePath = "/races/turkey_circuit.avif";
      break;
  }
  return imagePath;
};

// Récupération des positions de grille via l'API
onMounted(async () => {
  try {
    const { data, error } = await useFetch("/api/grid_position");

    if (error.value) {
      console.error(
        "Erreur lors de la récupération des positions de la grille",
        error.value
      );
    } else if (data.value) {
      grid_pos.value = data.value;
    }
  } catch (err) {
    console.error("Erreur générale", err);
  }
});

// Récupération des noms des pilotes via l'API
onMounted(async () => {
  try {
    const { data, error } = await useFetch("/api/driver_names");
    if (error.value) {
      console.error(
        "Erreur lors de la récupération des noms des pilotes",
        error.value
      );
    } else {
      driverNames.value = data.value;
    }
  } catch (err) {
    console.error("Erreur générale", err);
  }
});

// Navigation vers la page des résultats
const goToResult = () => {
  router.push("/result");
};
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

.circuit_name {
  color: white;
  font-size: 35px;
}
.pilote{
  color: white;
}

.circuit {
  width: 400px;
  height: auto;
}
.circuit_container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  margin-top: 20px;

}
.wrapper {
  padding-top: 100px;
  width: 100%;
  height: 80vh;
  display: flex;
  align-items: center;
  justify-content: space-around
}
.suivant-btn {
  background-color: #ee0000;
  color: white;
  font-size: 15px;
  padding: 10px 65px;
  height: 50px;
  width: auto;
  border-radius: 50px;
  margin-left: 150px;
  cursor: pointer;
  font-weight: bold;
  border: 2px solid white;
}
.btn {
  grid-column: 2 / 4;
  grid-row: 1 / 3;
}
</style>
