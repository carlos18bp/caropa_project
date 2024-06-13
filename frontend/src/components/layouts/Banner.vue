<template>
    <div class="bg-black py-2">
        <Vue3Marquee class="bg-black">
            <h2 v-for="banner in banners" class="text-white font-famil-semibold text-md">{{ banner.text }}</h2>
        </Vue3Marquee>
    </div>
</template>
<script setup>
import { ref, onMounted } from 'vue'
import { useHomeStore } from '@/stores/home'
import { Vue3Marquee } from 'vue3-marquee'

const homeStore = useHomeStore();
const banners = ref([])

onMounted( async () => {
    await homeStore.fetchHome();
    banners.value = homeStore.banners
})
</script>