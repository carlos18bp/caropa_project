<template>
    <div v-if="visible" class="w-screen h-14 bg-primary flex justify-between items-center px-16 text-white font-regular text-md shadow-2xl">
        <div>
            <p>Product added to shopping cart.</p>
        </div>
        <div class="flex gap-6">
            <a @click="shoppingCartToggle = true" class="cursor-pointer underline">See shopping cart</a>
            <XMarkIcon @click="closeModal()" class="w-6 h-6 cursor-pointer"></XMarkIcon>
        </div>
    </div>

    <!-- Shopping cart component -->
    <div v-if="shoppingCartToggle" class="fixed z-30 w-full h-screen top-0">
        <ShoppingCart :visible="shoppingCartToggle" @update:visible="shoppingCartToggle = $event"></ShoppingCart>
    </div>

</template>

<script setup>
    import { ref } from 'vue';
    import { gsap } from 'gsap'
    import { XMarkIcon } from "@heroicons/vue/24/outline";
    import ShoppingCart from './ShoppingCart.vue';
    
    const shoppingCartToggle = ref(false)
    const props = defineProps({
        visible: {
            type: Boolean,
            default: false,
            requred: true
        }
    })
    const emit = defineEmits(["update:visible"]);

    const closeModal = () => {
        emit("update:visible", false);
    }
</script>