/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
    "./node_modules/flowbite/**/*.js",
  ],
  safelist: [
    'bg-rose-500', 'bg-blue-500', 'bg-yellow-300', 'bg-green-500', 'bg-orange-500', 'bg-violet-500', 'bg-black', 'bg-white', 'bg-pink-500', 'bg-red-500'
  ],
  theme: {
    extend: {
      fontFamily: {
        'famil-semibold': ['FamiljenGrotesk-SemiBold'],
        'light': ['Poppins-Light'],
        'regular': ['Poppins-Regular'],
        'medium': ['Poppins-Medium'],
        'semibold': ['Poppins-Semibold'],
      },
      fontSize: {
        'xxs': '0.625rem',
      },
      colors: {
        'primary': '#DCB42C',
        'secondary': '#F3E393',
        'terciary': '#8B631D',
      },
    },
  },
  plugins: [
    require('flowbite/plugin'),
  ],
}

