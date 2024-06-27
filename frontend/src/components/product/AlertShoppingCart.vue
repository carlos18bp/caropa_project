<template>
    <div v-if="visible" class="w-screen h-14 bg-primary flex justify-between items-center px-16 text-white font-regular text-md shadow-2xl">
        <div>
            <p class="test-addShoppingCart-text">{{ $t('addShoppingCart').text }}</p>
        </div>
        <div class="flex gap-6">
            <a @click="shoppingCartToggle = true" class="cursor-pointer underline test-addShoppingCart-seeCart">{{ $t('addShoppingCart').seeCart }}</a>
            <XMarkIcon @click="closeModal()" class="w-6 h-6 cursor-pointer"></XMarkIcon>
        </div>
    </div>

    <!-- Shopping cart component -->
    <div v-if="shoppingCartToggle" class="fixed z-30 w-full h-screen top-0">
        <ShoppingCart :visible="shoppingCartToggle" @update:visible="shoppingCartToggle = $event"></ShoppingCart>
    </div>

</template>

<script setup>
    import { ref, watchEffect, computed } from 'vue';
    import { XMarkIcon } from "@heroicons/vue/24/outline";
    import ShoppingCart from './ShoppingCart.vue';

    import { useAppStore } from '@/stores/language.js';
    import enMessages from "@/locales/alerts/en";
    import esMessages from "@/locales/alerts/es";

    // Initialize app store to access the current language
    const appStore = useAppStore();
    const currentLanguage = computed(() => appStore.getCurrentLanguage);
    const messages = ref(enMessages)
    
    const shoppingCartToggle = ref(false)
    const props = defineProps({
        visible: {
            type: Boolean,
            default: false,
            requred: true
        }
    })

    const emit = defineEmits(["update:visible"]);

    const $t = (key) => messages.value[key];

    watchEffect(() => {
        messages.value = currentLanguage.value === "en" ? enMessages : esMessages;
    })

    const closeModal = () => {
        emit("update:visible", false);
    }
</script>