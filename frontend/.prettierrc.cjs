module.exports = {
  singleQuote: false,
  plugins: ["prettier-plugin-svelte", "prettier-plugin-tailwindcss"].map(
    require.resolve,
  ),
};
