import fs from "fs";
import csv from "csv-parser";
import path from "path";

export default defineEventHandler(async (event) => {
    const { fileName } = event.context.query;
    const csvFilePath = path.join(process.cwd(), "uploads", "data_test2.csv"); // Chemin vers ton fichier CSV
    return new Promise((resolve, reject) => {
        let circuitName = null;

        fs.createReadStream(csvFilePath)
            .pipe(csv())
            .on("data", (row) => {
                if (row.circuit_name && !circuitName) {
                    circuitName = row.circuit_name;
                    resolve(circuitName);
                    this.destroy();
                }
            })
            .on("end", () => {
                if (!circuitName) {
                    resolve(null);
                }
            })
            .on("error", (err) => {
                reject(err);
            });
    })
});