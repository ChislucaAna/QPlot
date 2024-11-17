/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './*.html',               // Include all HTML files in the root directory
    './**/*.html',            // Include all HTML files in subdirectories
    './templates/**/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
