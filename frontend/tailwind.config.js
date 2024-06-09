/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  safelist: [
    'bg-rose-500', 'bg-blue-500', 'bg-yellow-500', 'bg-green-500', 'bg-orange-500', 'bg-violet-500', 'bg-black', 'bg-white'
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

