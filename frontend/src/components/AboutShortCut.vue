<template>
    <!-- Container for the image and brand information section -->
    <div class="max-w-7xl px-8 mx-auto py-16">
        <div class="grid gap-6 lg:grid-cols-2">
            <!-- Main product image -->
            <div class="w-full">
                <img src="@/assets/images/product/image1.png" alt="Image 1" />
            </div>
            <!-- Brand information section -->
            <div class="flex flex-col justify-center items-center space-y-4">
                <!-- Brand logo -->
                <img src="@/assets/images/logo2.png" alt="Logo" class="w-56" />
                <!-- Brand description -->
                <p class="text-lg font-medium text-black text-center test-fourthSection-title">
                    {{ $t('fourthSection').title }}
                </p>
                <!-- Link to About Us page -->
                <p class="text-lg font-medium text-black">
                    <span class="test-fourthSection-subtitle">{{ $t('fourthSection').subtitle }}</span> |
                    <router-link :to="{ name: 'about_us' }" class="border-b-2 border-black test-fourthSection-about">
                        {{ $t('fourthSection').about }}
                    </router-link>
                </p>
            </div>
        </div>
    </div>
</template>

<script setup>
    import { ref, watchEffect, computed } from 'vue';
    import { useAppStore } from '@/stores/language.js';
    import enMessages from "@/locales/home/en";
    import esMessages from "@/locales/home/es";

    // Initialize app store to access the current language
    const appStore = useAppStore();
    const currentLanguage = computed(() => appStore.getCurrentLanguage);
    const messages = ref(enMessages)

    // Translation function
    const $t = (key) => messages.value[key];

    // Change messages in function to currently language
    watchEffect(() => {
        messages.value = currentLanguage.value === "en" ? enMessages : esMessages;
    });
</script>
