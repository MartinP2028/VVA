import fs from "fs";
import csv from "csv-parser";
import path from "path";
import { fileName } from '/upload.js'

export default defineEventHandler(async (event) => {
  const driverNames = [];
  const csvFilePath = path.join(process.cwd(), "uploads", "data_test2.csv"); // Chemin vers ton fichier CSV

  return new Promise((resolve, reject) => {
    fs.createReadStream(csvFilePath)
      .pipe(csv())
      .on("data", (row) => {
        if (row.driver_name) {
          driverNames.push(row.driver_name); // Ajoute les noms des pilotes
        }
      })
      .on("end", () => {
        resolve(driverNames); // Renvoie la liste des noms des pilotes
      })
      .on("error", (err) => {
        reject(err); // Gérer les erreurs
      });
  });
});