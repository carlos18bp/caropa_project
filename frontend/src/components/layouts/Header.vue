<template>
    <header class="bg-white">
      <div class="w-full grid grid-cols-3 px-8">
        <div class="pt-2 text-md font-famil-semibold text-black flex gap-6">
            <a class="cursor-pointer">Shop</a>
            <a class="cursor-pointer"> Contact</a>
            <a class="cursor-pointer">About</a>
            <div>
                <div class="flex items-center gap-1 cursor-pointer">
                    Blue Mom
                    <div>
                        <img src="@/assets/images/icons/heart.png" alt="Icon blue heart">
                    </div>
                </div>
            </div>
        </div>
        <div class="flex items-center justify-center">
            <img class="h-full pt-2" src="@/assets/images/logo1.png" alt="Principal logo of Caropa Couture">
        </div>
        <div class="pt-2 flex justify-end gap-6">
            <div>
                <div class="flex items-center justify-center gap-3 cursor-pointer">
                    <MagnifyingGlassIcon class="text-black size-6"></MagnifyingGlassIcon>
                    <a class="text-md font-famil-semibold text-black">Search</a>
                </div>
            </div>
            <ShoppingBagIcon  class="text-black size-6 cursor-pointer"></ShoppingBagIcon>
            <div class="flex gap-3">
                <a class="text-black font-famil-semibold text-md cursor-pointer">EN</a>
                <span class="text-black font-semibold text-lg">|</span>
                <a class="text-black font-famil-semibold text-md cursor-pointer">ES</a>
            </div>
        </div>
      </div>
      <div class="py-4 flex justify-center items-center gap-8">
        <a v-for="(category, index) in categories" :key="category.id" :class="{'inline-block font-famil-semibold text-lg cursor-pointer': true, 'inline-block font-famil-semibold text-lg text-primary': index === categories.length - 1}">{{ category.name }}</a>
      </div>
    </header>
</template>

<script setup>
import { ShoppingBagIcon } from '@heroicons/vue/24/outline'
import { MagnifyingGlassIcon } from '@heroicons/vue/24/outline'
import { useHomeStore } from '@/stores/home'
import { ref, onMounted } from 'vue'

const homeStore = useHomeStore();
const categories = ref([]);

onMounted( async () => {
    await homeStore.fetchHomeData();
    categories.value = homeStore.header_categories;
})

</script>