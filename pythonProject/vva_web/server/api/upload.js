import fs from "fs";
import csv from "csv-parser";
import multer from "multer";
import path from "path";

// Configuration du stockage pour multer
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, "uploads/"); // Dossier de destination
  },
  filename: (req, file, cb) => {
    const originalName = file.originalname;
    cb(null, originalName); // Nom du fichier original
  },
});

// Initialisation de multer avec le stockage configuré
const upload = multer({ storage: storage });

export default defineEventHandler((event) => {
  return new Promise((resolve, reject) => {
    // Gestion de l'upload avec multer
    upload.single("file")(event.node.req, event.node.res, (err) => {
      if (err) return reject(err);

      // Récupération du nom du fichier après l'upload
      const fileName = event.node.req.file.originalname;

      // Chemin complet vers le fichier uploadé
      const uploadedFilePath = path.join("uploads", fileName);

      // Lecture du fichier CSV uploadé
      fs.createReadStream(uploadedFilePath)
        .pipe(csv())
        .on("data", (row) => {
          // Traitement de chaque ligne du CSV ici
          // console.log(row);
        })
        .on("end", () => {
          console.log("Le fichier CSV a été traité avec succès");
          resolve({ message: "Fichier uploadé et traité avec succès", fileName });
        })
        .on("error", (err) => {
          console.error("Erreur lors du traitement du fichier CSV:", err);
          reject(err);
        });
    });
  });
});

