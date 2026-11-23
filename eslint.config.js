import js from "@eslint/js";
import globals from "globals";

export default [
    js.configs.recommended,
    {
        files: ["frontend/**/*.js"],
        languageOptions: {
            ecmaVersion: 2022,
            sourceType: "script",
            globals: globals.browser,
        },
        rules: {
            // funkcije iz app.js uporabljajo strani HTML, zato preverjamo samo lokalne spremenljivke
            "no-unused-vars": ["error", { vars: "local" }],
        },
    },
];