import fs from "fs";
import csv from "csv-parser";
import path from "path";
import { fileName } from '/upload.js'

export default defineEventHandler(async (event) => {
  const grid_pos = [];
  const csvFilePath = path.join(process.cwd(), "uploads", "data_test2.csv"); // Chemin vers ton fichier CSV

  return new Promise((resolve, reject) => {
    fs.createReadStream(csvFilePath)
      .pipe(csv())
      .on("data", (row) => {
        if (row.grid_pos) {
          grid_pos.push(row.grid_pos);
        }
      })
      .on("end", () => {
          resolve(grid_pos);
      })
      .on("error", (err) => {
        reject(err);
      });
  });
});