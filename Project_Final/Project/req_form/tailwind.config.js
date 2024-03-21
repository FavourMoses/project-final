/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    'req/templates/**/*.html'
  ],
  theme: {
    extend: {
      fontFamily: {
        'mont': ['Montserrat', 'sans-serif']
      },
      width: {
        'request': '80rem',
      }
    },
  },
  plugins: [
    require('@tailwindcss/forms')
  ],
}

