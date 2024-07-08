<template>
    <div class="fixed inset-0 flex justify-end z-50">
        <div 
            class="absolute inset-0 bg-gray-500 bg-opacity-40 backdrop-blur-md">
        </div>
        <div class="w-screen h-screen flex justify-center items-center z-60">
            <Vue3Lottie :animationData="animationData" :height="600" :width="600" :loop="true" :autoplay="true"></Vue3Lottie>
        </div>
    </div>
</template>

<script setup>
    import { Vue3Lottie } from 'vue3-lottie';
    import animationData from '@/assets/animations/loadingWhite.json';
</script>