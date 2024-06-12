/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
    "./node_modules/flowbite/**/*.js",
  ],
  safelist: [
    'bg-rose-500', 'bg-blue-500', 'bg-yellow-500', 'bg-green-500', 'bg-orange-500', 'bg-violet-500', 'bg-black', 'bg-white', 'bg-pink-500', 'bg-red-500'
  ],
  theme: {
    colors: {
      'primary': '#DCB42C',
    },
    extend: {
      fontFamily: {
        'famil-semibold': ['FamiljenGrotesk-SemiBold'],
        'light': ['Poppins-Light'],
        'regular': ['Poppins-Regular'],
        'medium': ['Poppins-Medium'],
        'semibold': ['Poppins-Semibold'],
      }
    },
  },
  plugins: [
    require('flowbite/plugin'),
  ],
}

