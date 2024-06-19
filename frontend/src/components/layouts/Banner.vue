<template>
    <div class="bg-black py-2">
        <Vue3Marquee class="bg-black">
            <div class="flex w-full justify-between">
                <!-- Iterating over banners to display text based on current language -->
                <h2 v-for="banner in banners" :key="banner.id" class="text-white font-famil-semibold text-md">
                    <!-- Display English text if current language is 'en' -->
                    <span v-if="currentLanguage === 'en'">{{ banner.text_en }}</span>
                    <!-- Display Spanish text otherwise -->
                    <span v-else>{{ banner.text_es }}</span>
                </h2>
            </div>
        </Vue3Marquee>
    </div>
</template>
  
<script setup>
    // Importing necessary modules and components
    import { computed, onMounted } from 'vue';
    import { useAppStore } from '@/stores/language.js';
    import { useHomeStore } from '@/stores/home';
    import { Vue3Marquee } from 'vue3-marquee';

    // Initialize the app store to access the current language
    const appStore = useAppStore();
    // Compute the current language from the app store
    const currentLanguage = computed(() => appStore.getCurrentLanguage);

    // Initialize the home store to access banners
    const homeStore = useHomeStore();
    // Compute the banners from the home store
    const banners = computed(() => homeStore.banners);

    // Fetch home data when the component is mounted
    onMounted(async () => {
        await homeStore.fetchHome();
    });
</script>
