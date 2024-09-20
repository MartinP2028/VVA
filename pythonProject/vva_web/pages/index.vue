<template>
  <div class="upload-container">
    <img src="../public/LogoF1.png" alt="F1 Logo" class="logo" />
    <div class="background">
      <div class="center">
        <div class="cube">
          <div class="file-upload">
            <input type="file" @change="handleFileUpload" id="fileInput" />
            <label for="fileInput" class="upload-label">
              <img
                src="../public/uploadfile.png"
                alt="Upload File"
                class="upload-image"
              />
            </label>
          </div>
        </div>
        <p>Upload your file to begin</p>
        <input type="file" @change="handleFileUpload" />
        <button class="suivant-btn" @click="goToPrintInfo">Suivant</button>
        <input type="file" @change="handleFileUpload" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

const handleFileUpload = async (event) => {
  const file = event.target.files[0];
  const formData = new FormData();
  formData.append("file", file);
  console.log(formData);

  try {
    const { data, error } = await useFetch("/api/upload", {
      method: "POST",
      body: formData,
    });

    if (error.value) {
      console.error("Erreur lors de l'upload", error.value);
    } else {
      console.log("Fichier uploadé avec succès", data.value);
    }
  } catch (error) {
    console.error("Erreur générale", error);
  }
};

const goToPrintInfo = () => {
  router.push("/print_info");
};
</script>

<style scoped>
.cube {
  width: 150px;
  height: 150px;
  background-color: #ffffff;
  border-radius: 10%;
  display: flex;
  justify-content: center;
}

.center {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
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

.logo {
  position: absolute;
  top: 20px;
  left: 20px;
  width: 300px;
  height: auto;
}

.file-upload {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-bottom: 20px;
}

input[type="file"] {
  display: none;
}

.upload-label {
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
}

.upload-image {
  padding-top: 25px;
  width: 100px;
  height: 100px;
}

p {
  padding: 30px;
  color: white;
  font-size: 15px; /* Adjusted size for better visibility */
  font-family: "Arial", sans-serif;
  text-align: center;
  font-weight: bold;
  width: 300px;
}

.suivant-btn {
  background-color: #ee0000;
  color: white;
  font-size: 15px;
  padding: 10px 40px;
  border: none;
  border-radius: 50px;
  cursor: pointer;
  font-weight: bold;
  border: 2px solid white;
}

.suivant-btn:hover {
  background-color: #ee0000;
}
</style>
