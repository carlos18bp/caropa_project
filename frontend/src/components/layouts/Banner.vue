<template>
    <div class="bg-black py-2">
        <Vue3Marquee class="bg-black">
        <div class="flex w-full justify-between">
            <h2 v-for="banner in banners" :key="banner.id" class="text-white font-famil-semibold text-md">
            {{ banner.text }}
            </h2>
        </div>
        </Vue3Marquee>
    </div>
</template>
  
<script setup>
    import { computed, onMounted } from 'vue'
    import { useHomeStore } from '@/stores/home'
    import { Vue3Marquee } from 'vue3-marquee'

    const homeStore = useHomeStore();
    const banners = computed(() => homeStore.banners);

    onMounted( async () => {
        await homeStore.fetchHome();
    })
</script>