<template>
    <header class="bg-white h-12 flex px-8 py-2 fixed top-0 left-0 w-full z-20 opacity-0 pointer-events-none transition-opacity duration-300 ease-in-out" ref="headerShort">
        <div class="inline-block">
            <div class="flex gap-3 items-center">
                <a class="text-black font-famil-semibold text-md cursor-pointer flex items-center"><span>EN</span></a>
                <span class="text-black font-semibold text-lg">|</span>
                <a class="text-black font-famil-semibold text-md cursor-pointer flex items-center"><span>ES</span></a>
            </div>
        </div>
        <div class="grow flex justify-center items-center gap-8">
            <a v-for="(category, index) in categories" :key="category.id" :class="{'inline-block font-famil-semibold text-lg cursor-pointer': true, 'inline-block font-famil-semibold text-lg text-primary': index === categories.length - 1}">{{ category.name }}</a>
        </div>
        <div class="flex items-center justify-end gap-6">
            <MagnifyingGlassIcon class="text-black size-6 cursor-pointer"></MagnifyingGlassIcon>
            <ShoppingBagIcon class="text-black size-6 cursor-pointer"></ShoppingBagIcon>
        </div>
    </header>
</template>

<script setup>
import { ShoppingBagIcon, MagnifyingGlassIcon } from '@heroicons/vue/24/outline';
import { useHomeStore } from '@/stores/home';
import { ref, onMounted } from 'vue';

const homeStore = useHomeStore();
const categories = ref([]);

onMounted(async () => {
    await homeStore.fetchHome();
    categories.value = homeStore.header_categories;
});
</script>
